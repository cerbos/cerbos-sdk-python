# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import base64
import json
import os
import ssl
import uuid
from dataclasses import dataclass
from functools import wraps
from typing import Any, Dict, List, Tuple, Union

import grpc
from google.protobuf import struct_pb2, timestamp_pb2

from cerbos.engine.v1 import engine_pb2
from cerbos.policy.v1 import policy_pb2
from cerbos.request.v1 import request_pb2
from cerbos.response.v1 import response_pb2
from cerbos.schema.v1 import schema_pb2
from cerbos.sdk.grpc.utils import get_resource, is_allowed
from cerbos.sdk.model import CerbosTLSError, CerbosTypeError
from cerbos.svc.v1 import svc_pb2_grpc

_PLAYGROUND_INSTANCE_KEY = "playground-instance"

_default_paths = ssl.get_default_verify_paths()
TLSVerify = Union[str, bool]


# TODO(saml) type errors generated from passing incorrect types to proto generated code currently
# aren't great, e.g. passing the incorrect Principal type to CheckResourcesRequest results in:
#     "Message must be initialized with a dict: cerbos.request.v1.CheckResourcesRequest".
# Investigate more useful TypeError returns.
def handle_errors(method):
    @wraps(method)
    def wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except TypeError as e:
            raise CerbosTypeError(str(e))

    return wrapper


def get_cert(c: TLSVerify) -> bytes | None:
    try:
        if isinstance(c, str):
            with open(c, "rb") as f:
                return f.read()
        elif isinstance(c, bool):
            # Attempt to retrieve the cert from the location specified at `SSL_CERT_FILE`
            # or the default location if not specified.
            filename = _default_paths.cafile
            if cf := os.getenv("SSL_CERT_FILE"):
                filename = cf
            with open(filename, "rb") as f:
                return f.read()
    except IOError:
        raise CerbosTLSError(f"Error reading certificate from file: {c}")
    except Exception:
        raise CerbosTLSError("Error retrieving certificate")

    raise TypeError("TLSVerify should be a string or boolean")


class PlaygroundInstanceCredentials(grpc.AuthMetadataPlugin):
    def __init__(self, playground_instance: str):
        self._playground_instance = playground_instance

    def __call__(
        self,
        context: grpc.AuthMetadataContext,
        callback: grpc.AuthMetadataPluginCallback,
    ) -> None:
        callback(((_PLAYGROUND_INSTANCE_KEY, self._playground_instance),), None)


class SyncClientBase:
    _channel: grpc.Channel

    def __init__(
        self,
        host: str,
        creds: grpc.ChannelCredentials,
        methods: List[Dict[str, str]] = None,
        tls_verify: TLSVerify = False,
        timeout_secs: float | None = None,
        request_retries: int = 0,
        wait_for_ready: bool = False,
    ):
        if timeout_secs and not isinstance(timeout_secs, (int, float)):
            raise TypeError("timeout_secs must be a number type")

        if request_retries and not isinstance(request_retries, (int, float)):
            raise TypeError(
                "request_retries must be a number type. anything below 2 is treated as 0 (disabled)"
            )

        if request_retries < 2:
            request_retries = 0

        method_config: dict[Any, Any] = {}

        if methods:
            method_config["name"] = methods

        if timeout_secs:
            method_config["timeout"] = f"{timeout_secs}s"

        if request_retries:
            method_config["retryPolicy"] = {
                "maxAttempts": request_retries,
                "initialBackoff": "1s",
                "maxBackoff": "10s",
                "backoffMultiplier": 2,
                "retryableStatusCodes": ["UNAVAILABLE"],
            }

        if wait_for_ready:
            method_config["waitForReady"] = wait_for_ready

        service_config = {"methodConfig": [method_config]}
        options = [
            ("grpc.service_config", json.dumps(service_config)),
        ]

        if tls_verify:
            self._channel = grpc.secure_channel(
                host,
                credentials=creds,
                options=options,
            )
        else:
            self._channel = grpc.insecure_channel(host, options=options)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        self._channel.close()


class CerbosClient(SyncClientBase):
    """Client for accessing the Cerbos API

    Args:
        host (str): The full address of the Cerbos API server (PDP)
        tls_verify (bool|str): If a path is passed it is used as the CA certificate. If True, we look for the path specified in `SSL_CERT_FILE` or at the default OS location. If False, server certificate verification is disabled
        playground_instance (str): Optional Cerbos Playground ID if testing against a Playground playground_instance
        timeout_secs (float): Optional request timeout in seconds (no timeout by default)
        request_retries (int): Optional maximum number of retries, including the original attempt. Anything below 2 will be treated as 0 (disabled)
        wait_for_ready (bool): Boolean specifying whether RPCs should wait until the connection is ready. Defaults to False

    Example:
        with AsyncCerbosClient("localhost:3593") as cerbos:
            if cerbos.is_allowed(
                "view",
                Principal(id="john", roles={"employee"}, attr={"geography": struct_pb2.Value(string_value="GB")}),
                Resource(id="XX125", "kind"="leave_request", attr={"geography": struct_pb2.Value(string_value="GB")})
                ):
                do_thing()
    """

    _client: svc_pb2_grpc.CerbosServiceStub

    def __init__(
        self,
        host: str,
        tls_verify: TLSVerify = False,
        playground_instance: str = "",
        timeout_secs: float | None = None,
        request_retries: int = 0,
        wait_for_ready: bool = False,
    ):
        creds: grpc.ChannelCredentials = None
        if tls_verify:
            cert = get_cert(tls_verify)
            creds = grpc.ssl_channel_credentials(cert)

        if playground_instance:
            # insecure creds required for playground without TLS
            if not creds:
                creds = grpc.ssl_channel_credentials()
            call_credentials = grpc.metadata_call_credentials(
                PlaygroundInstanceCredentials(playground_instance)
            )
            creds = grpc.composite_channel_credentials(creds, call_credentials)

        methods = [
            {"service": "svc.CerbosService", "method": "CheckResources"},
            {"service": "svc.CerbosService", "method": "PlanResources"},
        ]

        super().__init__(
            host,
            creds,
            methods,
            tls_verify,
            timeout_secs,
            request_retries,
            wait_for_ready,
        )

        self._client = svc_pb2_grpc.CerbosServiceStub(self._channel)

    @handle_errors
    def check_resources(
        self,
        principal: engine_pb2.Principal,
        resources: List[request_pb2.CheckResourcesRequest.ResourceEntry],
        request_id: str | None = None,
        aux_data: request_pb2.AuxData | None = None,
    ) -> response_pb2.CheckResourcesResponse:
        """Check permissions for a list of resources

        Args:
            principal (engine_pb2.Principal): principal who is performing the action
            resources (List[request_pb2.CheckResourcesRequest.ResourceEntry]): list of resources to check permissions for
            request_id (None|str): request ID for the request (default None)
            aux_data (None|request_pb2.AuxData): auxiliary data for the request
        """

        req_id = _get_request_id(request_id)
        req = request_pb2.CheckResourcesRequest(
            request_id=req_id,
            principal=principal,
            resources=resources,
            aux_data=aux_data,
        )

        return self._client.CheckResources(req)

    def is_allowed(
        self,
        action: str,
        principal: engine_pb2.Principal,
        resource: engine_pb2.Resource,
        request_id: str | None = None,
        aux_data: request_pb2.AuxData | None = None,
    ) -> bool:
        """Check permission for a single action

        Args:
            action (str): action being performed
            principal (engine_pb2.Principal): principal who is performing the action
            resource (engine_pb2.Resource): resource on which the action is being performed
            request_id (None|str): request ID for the request (default None)
            aux_data (None|request_pb2.AuxData): auxiliary data for the request
        """
        resp = self.check_resources(
            principal=principal,
            resources=[
                request_pb2.CheckResourcesRequest.ResourceEntry(
                    actions=[action], resource=resource
                )
            ],
            request_id=request_id,
            aux_data=aux_data,
        )
        if (res := get_resource(resp, resource.id)) is not None:
            return is_allowed(res, action)

        return False

    @handle_errors
    def plan_resources(
        self,
        action: str,
        principal: engine_pb2.Principal,
        resource: engine_pb2.PlanResourcesInput.Resource,
        request_id: str | None = None,
        aux_data: request_pb2.AuxData | None = None,
    ) -> response_pb2.PlanResourcesResponse:
        """Create a query plan for performing the given action on resources of the given kind

        Args:
            action (str): Action to perform
            principal (engine_pb2.Principal): principal who is performing the action
            resource (engine_pb2.PlanResourcesInput.Resource): information about the resource kind
            request_id (None|str): request ID for the request (default None)
            aux_data (None|request_pb2.AuxData): auxiliary data for the request
        """

        req_id = _get_request_id(request_id)
        req = request_pb2.PlanResourcesRequest(
            request_id=req_id,
            action=action,
            principal=principal,
            resource=resource,
            aux_data=aux_data,
        )

        return self._client.PlanResources(req)

    def server_info(
        self,
    ) -> response_pb2.ServerInfoResponse:
        """Retrieve server info for the running PDP"""
        return self._client.ServerInfo(request_pb2.ServerInfoRequest())

    def with_principal(
        self,
        principal: engine_pb2.Principal,
        aux_data: request_pb2.AuxData | None = None,
    ) -> "PrincipalContext":
        """Fixes the principal for subsequent requests"""

        return PrincipalContext(
            client=self,
            principal=principal,
            aux_data=aux_data,
        )


class PrincipalContext:
    """A special Cerbos client where the principal and auxData are fixed"""

    _client: CerbosClient
    _principal: engine_pb2.Principal
    _aux_data: request_pb2.AuxData | None

    def __init__(
        self,
        client: CerbosClient,
        principal: engine_pb2.Principal,
        aux_data: request_pb2.AuxData | None = None,
    ):
        self._client = client
        self._principal = principal
        self._aux_data = aux_data

    def check_resources(
        self,
        resources: List[request_pb2.CheckResourcesRequest.ResourceEntry],
        request_id: str | None = None,
    ) -> response_pb2.CheckResourcesResponse:
        """Check permissions for a list of resources

        Args:
            resources (List[request_pb2.CheckResourcesRequest.ResourceEntry]): list of resources to check permissions for
            request_id (None|str): request ID for the request (default None)
        """

        return self._client.check_resources(
            principal=self._principal,
            resources=resources,
            request_id=request_id,
            aux_data=self._aux_data,
        )

    def plan_resources(
        self,
        action: str,
        resource: engine_pb2.PlanResourcesInput.Resource,
        request_id: str | None = None,
        aux_data: request_pb2.AuxData | None = None,
    ) -> response_pb2.PlanResourcesResponse:
        """Create a query plan for performing the given action on resources of the given kind

        Args:
            action (str): Action to perform
            resource (engine_pb2.PlanResourcesInput.Resource): information about the resource kind
            request_id (None|str): request ID for the request (default None)
            aux_data (None|request_pb2.AuxData): auxiliary data for the request
        """

        return self._client.plan_resources(
            action=action,
            principal=self._principal,
            resource=resource,
            request_id=request_id,
            aux_data=aux_data,
        )

    def is_allowed(
        self, action: str, resource: engine_pb2.Resource, request_id: str | None = None
    ) -> bool:
        """Check permission for a single action

        Args:
            action (str): action being performed
            resource (engine_pb2.Resource): resource on which the action is being performed
            request_id (None|str): request ID for the request (default None)
        """

        return self._client.is_allowed(
            action=action,
            principal=self._principal,
            resource=resource,
            request_id=request_id,
            aux_data=self._aux_data,
        )


def _get_request_id(request_id: str | None) -> str:
    if request_id is None:
        return str(uuid.uuid4())

    return request_id


@dataclass
class AdminCredentials:
    username: str = "cerbos"
    password: str = "cerbosAdmin"

    def metadata(self):
        credentials = f"{self.username}:{self.password}"
        encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode(
            "utf-8"
        )
        return (("authorization", f"Basic {encoded_credentials}"),)


class CerbosAdminClient(SyncClientBase):
    """Client for accessing the Cerbos Admin API

    Args:
        host (str): The full address of the Cerbos API server (PDP)
        admin_credentials (AdminCredentials): Mandatory basic auth credentials for accessing the Admin API. Defaults to username=`cerbos` and password=`cerbosAdmin`
        tls_verify (bool|str): If a path is passed it is used as the CA certificate. If True, we look for the path specified in `SSL_CERT_FILE` or at the default OS location. If False, server certificate verification is disabled
        timeout_secs (float): Optional request timeout in seconds (no timeout by default)
        request_retries (int): Optional maximum number of retries, including the original attempt. Anything below 2 will be treated as 0 (disabled)
        wait_for_ready (bool): Boolean specifying whether RPCs should wait until the connection is ready. Defaults to False

    Example:
        with AsyncCerbosAdminClient("localhost:3593", admin_credentials=AdminCredentials("admin", "some_password")) as cerbos:
            if cerbos.add_or_update_policy(
                "view",
                Principal(id="john", roles={"employee"}, attr={"geography": struct_pb2.Value(string_value="GB")}),
                Resource(id="XX125", "kind"="leave_request", attr={"geography": struct_pb2.Value(string_value="GB")})
                ):
                do_thing()
    """

    _client: svc_pb2_grpc.CerbosAdminServiceStub
    _creds_metadata: Tuple[Tuple[str, str]]

    def __init__(
        self,
        host: str,
        admin_credentials: AdminCredentials | None = None,
        tls_verify: TLSVerify = False,
        timeout_secs: float | None = None,
        request_retries: int = 0,
        wait_for_ready: bool = False,
    ):
        admin_credentials = admin_credentials or AdminCredentials()
        self._creds_metadata = admin_credentials.metadata()

        creds: grpc.ChannelCredentials = None
        if tls_verify:
            cert = get_cert(tls_verify)
            creds = grpc.ssl_channel_credentials(cert)

        methods = [
            {"service": "svc.CerbosAdminService", "method": "AddOrUpdatePolicy"},
            {"service": "svc.CerbosAdminService", "method": "ListPolicies"},
            {"service": "svc.CerbosAdminService", "method": "GetPolicy"},
            {"service": "svc.CerbosAdminService", "method": "DisablePolicy"},
            {"service": "svc.CerbosAdminService", "method": "EnablePolicy"},
            {"service": "svc.CerbosAdminService", "method": "AddOrUpdateSchema"},
            {"service": "svc.CerbosAdminService", "method": "DeleteSchema"},
            {"service": "svc.CerbosAdminService", "method": "ListSchemas"},
            {"service": "svc.CerbosAdminService", "method": "GetSchema"},
            {"service": "svc.CerbosAdminService", "method": "ReloadStore"},
            # {"service": "svc.CerbosAdminService", "method": "AuditLogs"},
        ]

        super().__init__(
            host,
            creds,
            methods,
            tls_verify,
            timeout_secs,
            request_retries,
            wait_for_ready,
        )

        self._client = svc_pb2_grpc.CerbosAdminServiceStub(self._channel)

    def _call(self, method, *args, **kwargs):
        """
        Wrapper to call a method with the credentials metadata attached.

        Args:
            method: The gRPC method to call.
            *args: Positional arguments to pass to the method.
            **kwargs: Keyword arguments to pass to the method.
        """
        return method(*args, metadata=self._creds_metadata, **kwargs)

    @handle_errors
    def add_or_update_policy(
        self, policies: List[policy_pb2.Policy]
    ) -> response_pb2.AddOrUpdatePolicyResponse:
        """Add or update a set of policies in the mutable store

        Args:
            policies (List[policy_pb2.Policy]): list of policies to update
        """
        req = request_pb2.AddOrUpdatePolicyRequest(policies=policies)
        return self._call(self._client.AddOrUpdatePolicy, req)

    @handle_errors
    def list_policies(
        self,
        include_disabled: bool = False,
        name_regexp: str = "",
        scope_regexp: str = "",
        version_regexp: str = "",
    ) -> response_pb2.ListPoliciesResponse:
        """List policies with optional filters

        Args:
            include_disabled (bool): include disabled policies in the response. Defaults to False
            name_regexp (str): filter the policy name with case insensitive regular expression
            scope_regexp (str): filter the policy scope with case insensitive regular expression
            version_regexp (str): filter the policy version with case insensitive regular expression
        """
        req = request_pb2.ListPoliciesRequest(
            include_disabled=include_disabled,
            name_regexp=name_regexp,
            scope_regexp=scope_regexp,
            version_regexp=version_regexp,
        )
        return self._call(self._client.ListPolicies, req)

    @handle_errors
    def get_policy(self, ids: List[str]) -> response_pb2.GetPolicyResponse:
        """Retrieve policy details for each given id

        Args:
            ids (List[str]): list of policy IDs to retrieve details for
        """
        req = request_pb2.GetPolicyRequest(id=ids)
        return self._call(self._client.GetPolicy, req)

    @handle_errors
    def disable_policy(self, ids: List[str]) -> response_pb2.DisablePolicyResponse:
        """Disable a set of policies by id

        Args:
            ids (List[str]): list of policies to disable
        """
        req = request_pb2.DisablePolicyRequest(id=ids)
        return self._call(self._client.DisablePolicy, req)

    @handle_errors
    def enable_policy(self, ids: List[str]) -> response_pb2.EnablePolicyResponse:
        """Enable a set of policies by id

        Args:
            ids (List[str]): list of policies to enable
        """
        req = request_pb2.EnablePolicyRequest(id=ids)
        return self._call(self._client.EnablePolicy, req)

    @handle_errors
    def add_or_update_schema(
        self, schemas: List[schema_pb2.Schema]
    ) -> response_pb2.AddOrUpdateSchemaResponse:
        """Add or update a set of schemas in the mutable store

        Args:
            schemas (List[schema_pb2.Schema]): list of schemas to update
        """
        req = request_pb2.AddOrUpdateSchemaRequest(schemas=schemas)
        return self._call(self._client.AddOrUpdateSchema, req)

    @handle_errors
    def delete_schema(self, ids: List[str]) -> response_pb2.DeleteSchemaResponse:
        """Delete a set of schemas by id

        Args:
            ids (List[str]): list of schemas to delete
        """
        req = request_pb2.DeleteSchemaRequest(id=ids)
        return self._call(self._client.DeleteSchema, req)

    @handle_errors
    def list_schemas(
        self,
    ) -> response_pb2.ListSchemasResponse:
        """List schemas"""
        req = request_pb2.ListSchemasRequest()
        return self._call(self._client.ListSchemas, req)

    @handle_errors
    def get_schema(self, ids: List[str]) -> response_pb2.GetSchemaResponse:
        """Retrieve schema details for each given id

        Args:
            ids (List[str]): list of schema IDs to retrieve details for
        """
        req = request_pb2.GetSchemaRequest(id=ids)
        return self._call(self._client.GetSchema, req)

    @handle_errors
    def reload_store(self, wait: bool = False) -> response_pb2.ReloadStoreResponse:
        """Reload the store

        Args:
            wait (bool): if true, the request will block until it finishes
        """
        req = request_pb2.ReloadStoreRequest(wait=wait)
        return self._call(self._client.ReloadStore, req)

    # TODO(saml) basic auth is handled differently with the streaming API, figure out how and re-enable
    # @handle_errors
    # async def list_audit_logs(
    #     self,
    #     start_time: datetime | None = None,
    #     end_time: datetime | None = None,
    #     lookup: str = "",
    #     tail: int = 0,
    #     kind: request_pb2.ListAuditLogEntriesRequest.Kind = request_pb2.ListAuditLogEntriesRequest.KIND_ACCESS,
    # ) -> response_pb2.CheckResourcesResponse:
    #     """Check permissions for a list of resources

    #     Args:
    #         resources (List[request_pb2.CheckResourcesRequest.ResourceEntry]): list of resources to check permissions for
    #         request_id (None|str): request ID for the request (default None)
    #     """
    #     req = request_pb2.ListAuditLogEntriesRequest(
    #         kind=kind,
    #     )

    #     if tail > 0:
    #         # req.tail = struct_pb2.Value(number_value=tail)
    #         req.tail = tail
    #     elif start_time:
    #         if not end_time:
    #             end_time = datetime.now()
    #         req.between = request_pb2.ListAuditLogEntriesRequest.TimeRange(
    #             start=timestamp_pb2.Timestamp(seconds=start_time.timestamp()),
    #             end=timestamp_pb2.Timestamp(seconds=end_time),
    #         )
    #     elif lookup != "":
    #         req.lookup = lookup

    #     # UnaryStreamCall can't be used in 'await' expression
    #     log_stream = self._client.ListAuditLogEntries(req)
    #     while True:
    #         resp = await log_stream.read()
    #         if resp == grpc.EOF:
    #             break
    #         print(resp.message)

    #     return self._client.ListAuditLogEntries(req)
