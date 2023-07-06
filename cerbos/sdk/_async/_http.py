# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import logging
import ssl
import uuid
from typing import Optional, Union
from urllib.parse import urlparse

import httpx
from requests_toolbelt import user_agent
from tenacity import retry, stop_after_attempt, wait_exponential

import cerbos
from cerbos.sdk.model import *

TLSVerify = Union[str, bool, ssl.SSLContext]


class AsyncRetryClient(httpx.AsyncClient):
    def __init__(self, request_retries: int = 0, *args, **kwargs):
        self._client = httpx.AsyncClient(*args, **kwargs)

        fn = self._client.post
        if request_retries:
            # 1+n because 1 == the initial attempt
            self._post_fn = retry(
                stop=stop_after_attempt(1 + request_retries),
                wait=wait_exponential(multiplier=1, min=1, max=10),
            )(fn)
        else:
            self._post_fn = fn

    # By coincidence, we only want to allow retries on both of the `post` use cases on the http client, and
    # not any other methods. Therefore, we can conveniently globally wrap the `post` method.
    # We'll need to adapt this if we want more specificity in the future.
    def post(self, *args, **kwargs):
        return self._post_fn(*args, **kwargs)

    def __getattr__(self, attr):
        return getattr(self._client, attr)


class AsyncCerbosClient:
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

    _http: httpx.AsyncClient
    _logger: logging.Logger
    _raise_on_error: bool

    def __init__(
        self,
        host: str,
        *,
        timeout_secs: float = 2.0,
        tls_verify: TLSVerify = True,
        playground_instance: Optional[str] = None,
        raise_on_error: bool = False,
        request_retries: int = 0,
        connection_retries: int = 0,
        debug: bool = False,
        logger: logging.Logger = logging.getLogger(__name__),
    ):
        self._logger = logger
        self._raise_on_error = raise_on_error

        ua = user_agent("cerbos-python", cerbos.__version__)
        headers = {"User-Agent": ua}

        if playground_instance is not None:
            headers.update({"playground-instance": playground_instance})

        event_hooks = {"response": []}
        if debug:
            event_hooks["response"].append(self._log_response)

        if raise_on_error:
            event_hooks["response"].append(self._raise_on_status)

        transport_params = {}
        base_url = host

        url = urlparse(host)
        if url.scheme == "unix" or url.scheme == "unix+http":
            transport_params["uds"] = url.path
            base_url = "http://cerbos.sock"
        elif url.scheme == "unix+https":
            transport_params |= {"uds": url.path, "verify": tls_verify}
            base_url = "https://cerbos.sock"

        if connection_retries:
            transport_params["retries"] = connection_retries

        transport = None
        if transport_params:
            transport = httpx.AsyncHTTPTransport(**transport_params)

        self._http = AsyncRetryClient(
            base_url=base_url,
            headers=headers,
            timeout=timeout_secs,
            verify=tls_verify,
            event_hooks=event_hooks,
            transport=transport,
            request_retries=request_retries,
        )

    async def _raise_on_status(self, response: httpx.Response):
        if response is None:
            return

        response.raise_for_status()

    async def _log_response(self, response: httpx.Response):
        if response is None:
            return

        req_prefix = "< "
        res_prefix = "> "
        request = response.request
        output = []

        await response.aread()

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

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.close()

    async def check_resources(
        self,
        principal: Principal,
        resources: ResourceList,
        request_id: Optional[str] = None,
        aux_data: Optional[AuxData] = None,
    ) -> CheckResourcesResponse:
        """Check permissions for a list of resources

        Args:
            principal (Principal): principal who is performing the action
            resources (ResourceList): list of resources to check permissions for
            request_id (None|str): request ID for the request (default None)
            aux_data (None|AuxData): auxiliary data for the request
        """

        req_id = _get_request_id(request_id)
        req = CheckResourcesRequest(
            request_id=req_id,
            principal=principal,
            resources=resources.resources,
            aux_data=aux_data,
        )
        resp = await self._http.post("/api/check/resources", json=req.to_dict())
        if resp.is_error:
            if self._raise_on_error:
                raise CerbosRequestException(APIError.from_dict(resp.json()))

            return CheckResourcesResponse(
                request_id=req_id,
                status_code=resp.status_code,
                status_msg=APIError.from_dict(resp.json()),
            )

        return CheckResourcesResponse.from_dict(resp.json())

    async def is_allowed(
        self,
        action: str,
        principal: Principal,
        resource: Resource,
        request_id: Optional[str] = None,
        aux_data: Optional[AuxData] = None,
    ) -> bool:
        """Check permission for a single action

        Args:
            action (str): action being performed
            principal (Principal): principal who is performing the action
            resource (Resource): resource on which the action is being performed
            request_id (None|str): request ID for the request (default None)
            aux_data (None|AuxData): auxiliary data for the request
        """
        resp = await self.check_resources(
            principal=principal,
            resources=ResourceList().add(resource, {action}),
            request_id=request_id,
            aux_data=aux_data,
        )

        if (r := resp.get_resource(resource.id)) is not None:
            return r.is_allowed(action)

        return False

    async def plan_resources(
        self,
        action: str,
        principal: Principal,
        resource: ResourceDesc,
        request_id: Optional[str] = None,
        aux_data: Optional[AuxData] = None,
    ) -> PlanResourcesResponse:
        """Create a query plan for performing the given action on resources of the given kind

        Args:
            action (str): Action to perform
            principal (Principal): principal who is performing the action
            resource (ResourceDesc): information about the resource kind
            request_id (None|str): request ID for the request (default None)
            aux_data (None|AuxData): auxiliary data for the request
        """

        req_id = _get_request_id(request_id)
        req = PlanResourcesRequest(
            request_id=req_id,
            action=action,
            principal=principal,
            resource=resource,
            aux_data=aux_data,
        )

        resp = await self._http.post("/api/plan/resources", json=req.to_dict())
        if resp.is_error:
            if self._raise_on_error:
                raise CerbosRequestException(APIError.from_dict(resp.json()))

            return PlanResourcesResponse(
                request_id=req_id,
                status_code=resp.status_code,
                status_msg=APIError.from_dict(resp.json()),
                action=action,
                resource_kind=resource.kind,
                policy_version=resource.policy_version,
            )

        return PlanResourcesResponse.from_dict(resp.json())

    async def is_healthy(self, svc: Optional[str] = None) -> bool:
        """Checks the health of the Cerbos endpoint"""

        params = None if svc is None else {"service": svc}
        try:
            resp = await self._http.get("/_cerbos/health", params=params)
            return resp.is_success
        except Exception:
            return False

    def with_principal(
        self, principal: Principal, aux_data: Optional[AuxData] = None
    ) -> "AsyncPrincipalContext":
        """Fixes the principal for subsequent requests"""

        return AsyncPrincipalContext(self, principal, aux_data)

    async def close(self):
        await self._http.aclose()


class AsyncPrincipalContext:
    """A special Cerbos client where the principal and auxData are fixed"""

    _client: AsyncCerbosClient
    _principal: Principal
    _aux_data: Optional[AuxData]

    def __init__(
        self,
        client: AsyncCerbosClient,
        principal: Principal,
        aux_data: Optional[AuxData] = None,
    ):
        self._client = client
        self._principal = principal
        self._aux_data = aux_data

    async def check_resources(
        self, resources: ResourceList, request_id: Optional[str] = None
    ) -> CheckResourcesResponse:
        """Check permissions for a list of resources

        Args:
            resources (ResourceList): list of resources to check permissions for
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
        resource: ResourceDesc,
        request_id: Optional[str] = None,
        aux_data: Optional[AuxData] = None,
    ) -> PlanResourcesResponse:
        """Create a query plan for performing the given action on resources of the given kind

        Args:
            action (str): Action to perform
            resource (ResourceDesc): information about the resource kind
            request_id (None|str): request ID for the request (default None)
            aux_data (None|AuxData): auxiliary data for the request
        """

        return await self._client.plan_resources(
            action=action,
            principal=self._principal,
            resource=resource,
            request_id=request_id,
            aux_data=aux_data,
        )

    async def is_allowed(
        self, action: str, resource: Resource, request_id: Optional[str] = None
    ) -> bool:
        """Check permission for a single action

        Args:
            action (str): action being performed
            resource (Resource): resource on which the action is being performed
            request_id (None|str): request ID for the request (default None)
        """

        return await self._client.is_allowed(
            action=action,
            principal=self._principal,
            resource=resource,
            request_id=request_id,
            aux_data=self._aux_data,
        )


def _get_request_id(request_id: Optional[str]) -> str:
    if request_id is None:
        return str(uuid.uuid4())

    return request_id
