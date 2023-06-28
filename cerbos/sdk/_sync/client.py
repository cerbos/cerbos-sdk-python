# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import json
import logging
import os
import ssl
import uuid
from typing import Union
from urllib.parse import urlparse

import grpc
import httpx
from requests_toolbelt import user_agent

from cerbos.request.v1 import request_pb2
from cerbos.response.v1 import response_pb2
from cerbos.sdk import model
from cerbos.svc.v1 import svc_pb2_grpc

_PLAYGROUND_INSTANCE_KEY = "playground-instance"

_default_paths = ssl.get_default_verify_paths()
TLSVerify = Union[str, bool, ssl.SSLContext]


def get_cert(c: TLSVerify) -> bytes | None:
    # TODO(saml): error handling
    if isinstance(c, str):
        with open(c, "rb") as f:
            return f.read()
    elif isinstance(c, bool):
        filename = _default_paths.cafile
        if cf := os.getenv("SSL_CERT_FILE"):
            filename = cf
        # Attempt to retrieve the cert from the location specified at `SSL_CERT_FILE`
        # or the default location if not specified.
        with open(filename, "rb") as f:
            return f.read()
    elif isinstance(c, TLSVerify):
        # TODO(saml)
        raise NotImplementedError


class PlaygroundInstanceCredentials(grpc.AuthMetadataPlugin):
    def __init__(self, playground_instance: str):
        self._playground_instance = playground_instance

    def __call__(
        self,
        context: grpc.AuthMetadataContext,
        callback: grpc.AuthMetadataPluginCallback,
    ) -> None:
        callback(((_PLAYGROUND_INSTANCE_KEY, self._playground_instance),), None)


class CerbosClient:
    """Client for accessing the Cerbos API

    Args:
        host (str): The full address of the Cerbos API server (PDP)
        timeout_secs (float): Request timeout in seconds (default is 2)
        tls_verify (bool|str|SSLContext): If False, disables server certificate verification. If a path is passed it is used as the CA certificate
        playground_instance (str): Optional Cerbos Playground ID if testing against a Playground playground_instance
        raise_on_error (bool): Raise an exception on unsuccessful requests (default is False)
        debug (bool): Log request and response
        logger (Logger): Logger to use for logging

    Example:
        with CerbosClient("http://localhost:3592") as cerbos:
            if cerbos.is_allowed(
                "view",
                Principal(id="john", roles={"employee"}, attr={"geography":"GB"}),
                Resource(id="XX125", "kind"="leave_request", attr={"geography":"GB"})
                ):
                do_thing()
    """

    _logger: logging.Logger
    _raise_on_error: bool
    _channel: grpc.Channel
    _client: svc_pb2_grpc.CerbosServiceStub

    def __init__(
        self,
        host: str,
        *,
        timeout_secs: float = 2.0,
        tls_verify: TLSVerify = False,
        playground_instance: str | None = None,
        raise_on_error: bool = False,
        request_retries: int = 2,  # grpc expectes a minimum of 2
        connection_retries: int = 0,
        debug: bool = False,
        logger: logging.Logger = logging.getLogger(__name__),
    ):
        self._logger = logger
        self._raise_on_error = raise_on_error

        # ua = user_agent("cerbos-python", cerbos.__version__)
        # headers = {"User-Agent": ua}

        # event_hooks = {"response": []}
        # if debug:
        #     event_hooks["response"].append(self._log_response)

        # if self._raise_on_error:
        #     event_hooks["response"].append(self._raise_on_status)

        # Historically, this client was built on top of HTTP, and the `host` argument would have explicitly
        # required the `http{s}://` scheme prefix. In order to maintain backwards compatibility, we still
        # accept these addresses but manually strip the prefix prior to building the url.
        base_url = host
        url = urlparse(base_url)
        if url.scheme in ["http", "https"]:
            base_url = base_url.removeprefix(url.scheme + "://")
            # TODO(saml) dedup
            if url.scheme == "https" and tls_verify is False:
                tls_verify = True
        #  We previously used `unix+http{s}` to indicate HTTP over UDS
        elif url.scheme in ["unix+http", "unix+https"]:
            base_url = "unix:" + url.netloc + url.path
            if url.scheme == "unix+https" and tls_verify is False:
                tls_verify = True

        service_config = {
            "methodConfig": [
                {
                    "name": [
                        {
                            "service": "svc.CerbosService",
                            "method": "CheckResources",
                        },
                        {"service": "svc.CerbosService", "method": "PlanResources"},
                    ],
                    "waitForReady": bool(
                        connection_retries
                    ),  # TODO(saml) rename and repurpose
                    "timeout": f"{timeout_secs}s",
                    "retryPolicy": {
                        "maxAttempts": request_retries,
                        "initialBackoff": "1s",
                        "maxBackoff": "10s",
                        "backoffMultiplier": 2,  # the http retry lib had it set to 1
                        "retryableStatusCodes": ["UNAVAILABLE"],
                    },
                }
            ]
        }
        options = [
            ("grpc.service_config", json.dumps(service_config)),
        ]
        if tls_verify:
            cert = get_cert(tls_verify)
            creds = grpc.ssl_channel_credentials(cert)
            if (
                playground_instance is not None
            ):  # TODO(saml) noop, or report requirement of TLS?
                call_credentials = grpc.metadata_call_credentials(
                    PlaygroundInstanceCredentials(playground_instance)
                )
                creds = grpc.composite_channel_credentials(creds, call_credentials)
            self._channel = grpc.secure_channel(
                base_url, credentials=creds, options=options
            )
        else:
            self._channel = grpc.insecure_channel(base_url, options=options)

        self._client = svc_pb2_grpc.CerbosServiceStub(self._channel)

    # TODO(saml) rethink
    def _raise_on_status(self, response: httpx.Response):
        if response is None:
            return
        # response.raise_for_status()

    # TODO(saml) rethink
    def _log_response(self, response: httpx.Response):
        if response is None:
            return

        req_prefix = "< "
        res_prefix = "> "
        request = response.request
        output = []

        response.read()

        output.append(f"{req_prefix}{request.method} {request.url}")

        for name, value in request.headers.items():
            output.append(f"{req_prefix}{name}: {value}")

        output.append(req_prefix)

        if isinstance(request.content, (str, bytes)):
            output.append(f"{req_prefix}{request.content}")
        else:
            output.append("<< Request body is not a string-like type >>")

        output.append("")

        output.append(f"{res_prefix}{response.status_code} {response.reason_phrase}")

        for name, value in response.headers.items():
            output.append(f"{res_prefix}{name}: {value}")

        output.append(res_prefix)

        output.append(f"{res_prefix}{response.text}")

        msg = "\n".join(output)
        self._logger.debug(msg)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def check_resources(
        self,
        principal: model.Principal,
        resources: model.ResourceList,
        request_id: str | None = None,
        aux_data: model.AuxData | None = None,
    ) -> response_pb2.CheckResourcesResponse:
        """Check permissions for a list of resources

        Args:
            principal (Principal): principal who is performing the action
            resources (ResourceList): list of resources to check permissions for
            request_id (None|str): request ID for the request (default None)
            aux_data (None|AuxData): auxiliary data for the request
        """

        req_id = _get_request_id(request_id)
        req = request_pb2.CheckResourcesRequest(
            request_id=req_id,
            principal=principal.to_proto(),
            resources=[
                request_pb2.CheckResourcesRequest.ResourceEntry(
                    resource=r.resource.to_proto(), actions=r.actions
                )
                for r in resources.resources
            ],
        )
        if aux_data:
            req.aux_data = aux_data.to_proto()

        try:
            return self._client.CheckResources(req)
        except grpc.RpcError as e:
            if self._raise_on_error:
                raise model.CerbosRequestException(
                    model.APIError(
                        code=e.code(),
                        message=e.details(),
                    )
                )
            # raise model.CerbosRequestException(
            #     request_id=req_id,
            #     status_code=e.code(),
            #     status_msg=model.APIError.from_dict(d),
            # )

    def is_allowed(
        self,
        action: str,
        principal: model.Principal,
        resource: model.Resource,
        request_id: str | None = None,
        aux_data: model.AuxData | None = None,
    ) -> bool:
        """Check permission for a single action

        Args:
            action (str): action being performed
            principal (Principal): principal who is performing the action
            resource (Resource): resource on which the action is being performed
            request_id (None|str): request ID for the request (default None)
            aux_data (None|AuxData): auxiliary data for the request
        """
        try:
            resp = self.check_resources(
                principal=principal,
                resources=model.ResourceList().add(resource, {action}),
                request_id=request_id,
                aux_data=aux_data,
            )

            if (res := model.get_resource(resp, resource.id, resp.results)) is not None:
                return model.is_allowed(res, action)
        except grpc.RpcError as e:
            if self._raise_on_error:
                raise model.CerbosRequestException(
                    model.APIError(
                        code=e.code(),
                        message=e.details(),
                    )
                )

        return False

    def plan_resources(
        self,
        action: str,
        principal: model.Principal,
        resource: model.ResourceDesc,
        request_id: str | None = None,
        aux_data: model.AuxData | None = None,
    ) -> response_pb2.PlanResourcesResponse:
        """Create a query plan for performing the given action on resources of the given kind

        Args:
            action (str): Action to perform
            principal (Principal): principal who is performing the action
            resource (ResourceDesc): information about the resource kind
            request_id (None|str): request ID for the request (default None)
            aux_data (None|AuxData): auxiliary data for the request
        """

        req_id = _get_request_id(request_id)
        req = request_pb2.PlanResourcesRequest(
            request_id=req_id,
            action=action,
            principal=principal.to_proto(),
            resource=resource.to_proto(),
        )
        if aux_data:
            req.aux_data = aux_data.to_proto()

        return self._client.PlanResources(req)

    def server_info(
        self,
    ) -> response_pb2.ServerInfoResponse:
        """Retrieve server info for the running PDP"""

        return self._client.ServerInfo(request_pb2.ServerInfoRequest())

    def is_healthy(self, *args) -> bool:
        """Checks the health of the Cerbos endpoint"""

        # TODO(saml) what to do here?
        return True

    def with_principal(
        self, principal: model.Principal, aux_data: model.AuxData | None = None
    ) -> "PrincipalContext":
        """Fixes the principal for subsequent requests"""

        return PrincipalContext(
            client=self,
            principal=principal,
            aux_data=aux_data,
        )

    def close(self):
        self._channel.close()


class PrincipalContext:
    """A special Cerbos client where the principal and auxData are fixed"""

    _client: CerbosClient
    _principal: model.Principal
    _aux_data: model.AuxData | None

    def __init__(
        self,
        client: CerbosClient,
        principal: model.Principal,
        aux_data: model.AuxData | None = None,
    ):
        self._client = client
        self._principal = principal
        self._aux_data = aux_data

    def check_resources(
        self, resources: model.ResourceList, request_id: str | None = None
    ) -> response_pb2.CheckResourcesResponse:
        """Check permissions for a list of resources

        Args:
            resources (ResourceList): list of resources to check permissions for
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
        resource: model.ResourceDesc,
        request_id: str | None = None,
        aux_data: model.AuxData | None = None,
    ) -> response_pb2.PlanResourcesResponse:
        """Create a query plan for performing the given action on resources of the given kind

        Args:
            action (str): Action to perform
            resource (ResourceDesc): information about the resource kind
            request_id (None|str): request ID for the request (default None)
            aux_data (None|AuxData): auxiliary data for the request
        """

        return self._client.plan_resources(
            action=action,
            principal=self._principal,
            resource=resource,
            request_id=request_id,
            aux_data=aux_data,
        )

    def is_allowed(
        self, action: str, resource: model.Resource, request_id: str | None = None
    ) -> bool:
        """Check permission for a single action

        Args:
            action (str): action being performed
            resource (Resource): resource on which the action is being performed
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
