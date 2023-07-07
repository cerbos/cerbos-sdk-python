# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import json
import os
import ssl
import uuid
from functools import wraps
from typing import Any, List, Union

import grpc
from cerbos.sdk.grpc.utils import get_resource, is_allowed
from cerbos.sdk.model import CerbosTLSError, CerbosTypeError

from cerbos.engine.v1 import engine_pb2
from cerbos.request.v1 import request_pb2
from cerbos.response.v1 import response_pb2
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
    async def wrapper(*args, **kwargs):
        try:
            return await method(*args, **kwargs)
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


class AsyncCerbosClient:
    """Client for accessing the Cerbos API

    Args:
        host (str): The full address of the Cerbos API server (PDP)
        tls_verify (bool|str): If a path is passed it is used as the CA certificate. If True, we look for the path specified in `SSL_CERT_FILE` or at the default OS location. If False, server certificate verification is disabled
        playground_instance (str): Optional Cerbos Playground ID if testing against a Playground playground_instance
        timeout_secs (float): Optional request timeout in seconds (no timeout by default)
        request_retries (int): Optional maximum number of retries, including the original attempt. Anything below 2 will be treated as 0 (disabled)
        wait_for_ready (bool): Boolean specifying whether RPCs should wait until the connection is ready. Defaults to False

    Example:
        with CerbosClient("localhost:3593") as cerbos:
            if cerbos.is_allowed(
                "view",
                Principal(id="john", roles={"employee"}, attr={"geography": struct_pb2.Value(string_value="GB")}),
                Resource(id="XX125", "kind"="leave_request", attr={"geography": struct_pb2.Value(string_value="GB")})
                ):
                do_thing()
    """

    _channel: grpc.aio.Channel
    _client: svc_pb2_grpc.CerbosServiceStub

    def __init__(
        self,
        host: str,
        tls_verify: TLSVerify = False,
        playground_instance: str | None = None,
        timeout_secs: float | None = None,
        request_retries: int = 0,
        wait_for_ready: bool = False,
    ):
        if timeout_secs and not isinstance(timeout_secs, int | float):
            raise TypeError("timeout_secs must be a number type")

        if request_retries and not isinstance(request_retries, int | float):
            raise TypeError(
                "request_retries must be a number type. anything below 2 is treated as 0 (disabled)"
            )

        # grpc expectes a minimum of 2
        if request_retries < 2:
            request_retries = 0

        method_config: dict[Any, Any] = {
            "name": [
                {
                    "service": "svc.CerbosService",
                    "method": "CheckResources",
                },
                {"service": "svc.CerbosService", "method": "PlanResources"},
            ]
        }

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

        creds: grpc.ChannelCredentials | None = None
        if tls_verify:
            cert = get_cert(tls_verify)
            creds = grpc.ssl_channel_credentials(cert)

        if playground_instance:
            # `playground_instance` requires empty channel credentials even if tls is disabled
            if not creds:
                creds = grpc.ssl_channel_credentials()
            call_credentials = grpc.metadata_call_credentials(
                PlaygroundInstanceCredentials(playground_instance)
            )
            creds = grpc.composite_channel_credentials(creds, call_credentials)

        if creds:
            self._channel = grpc.aio.secure_channel(
                host,
                credentials=creds,
                options=options,
            )
        else:
            self._channel = grpc.aio.insecure_channel(host, options=options)

        self._client = svc_pb2_grpc.CerbosServiceStub(self._channel)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.close()

    @handle_errors
    async def check_resources(
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

        return await self._client.CheckResources(req)

    async def is_allowed(
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
        resp = await self.check_resources(
            principal=principal,
            resources=[
                request_pb2.CheckResourcesRequest.ResourceEntry(
                    actions=[action], resource=resource
                )
            ],
            request_id=request_id,
            aux_data=aux_data,
        )
        if (res := get_resource(resp, resource.id, resp.results)) is not None:
            return is_allowed(res, action)

        return False

    @handle_errors
    async def plan_resources(
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

        return await self._client.PlanResources(req)

    async def server_info(
        self,
    ) -> response_pb2.ServerInfoResponse:
        """Retrieve server info for the running PDP"""
        return await self._client.ServerInfo(request_pb2.ServerInfoRequest())

    def with_principal(
        self,
        principal: engine_pb2.Principal,
        aux_data: request_pb2.AuxData | None = None,
    ) -> "AsyncPrincipalContext":
        """Fixes the principal for subsequent requests"""

        return AsyncPrincipalContext(
            client=self,
            principal=principal,
            aux_data=aux_data,
        )

    async def close(self):
        await self._channel.close()


class AsyncPrincipalContext:
    """A special Cerbos client where the principal and auxData are fixed"""

    _client: AsyncCerbosClient
    _principal: engine_pb2.Principal
    _aux_data: request_pb2.AuxData | None

    def __init__(
        self,
        client: AsyncCerbosClient,
        principal: engine_pb2.Principal,
        aux_data: request_pb2.AuxData | None = None,
    ):
        self._client = client
        self._principal = principal
        self._aux_data = aux_data

    async def check_resources(
        self,
        resources: List[request_pb2.CheckResourcesRequest.ResourceEntry],
        request_id: str | None = None,
    ) -> response_pb2.CheckResourcesResponse:
        """Check permissions for a list of resources

        Args:
            resources (List[request_pb2.CheckResourcesRequest.ResourceEntry]): list of resources to check permissions for
            request_id (None|str): request ID for the request (default None)
        """

        return await self._client.check_resources(
            principal=self._principal,
            resources=resources,
            request_id=request_id,
            aux_data=self._aux_data,
        )

    async def plan_resources(
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

        return await self._client.plan_resources(
            action=action,
            principal=self._principal,
            resource=resource,
            request_id=request_id,
            aux_data=aux_data,
        )

    async def is_allowed(
        self, action: str, resource: engine_pb2.Resource, request_id: str | None = None
    ) -> bool:
        """Check permission for a single action

        Args:
            action (str): action being performed
            resource (engine_pb2.Resource): resource on which the action is being performed
            request_id (None|str): request ID for the request (default None)
        """

        return await self._client.is_allowed(
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
