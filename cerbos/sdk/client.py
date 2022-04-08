# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import logging
import uuid
from typing import Optional

import requests
from requests.packages.urllib3.util.retry import Retry
from requests_toolbelt import sessions, user_agent
from requests_toolbelt.utils import dump

import cerbos
from cerbos.sdk.model import *
from cerbos.sdk.util import TimeoutAdapter


class CerbosClient:
    """Client for accessing the Cerbos API

    Args:
        host (str): The full address of the Cerbos API server (PDP)
        timeout_secs (float): Request timeout in seconds (default is 2)
        retry_strategy (Retry): A urllib3 Retry object defining how to retry requests (default is None)
        tls_verify (bool|str): If False, disables server certificate verification. If a path is passed it is used as the CA certificate
        playground_instance (str): Optional Cerbos Playground ID if testing against a Playground playground_instance
        raise_on_error (bool): Raise an exception on unsuccessful requests (default is False)
        debug (bool): Log requests and responses (default is False)
        logger (logging.Logger): Logger to use for debug output (default is None)

    Example:
        with CerbosClient("http://localhost:3592") as cerbos:
            if cerbos.is_allowed(
                "view",
                Principal(id="john", roles={"employee"}, attr={"geography":"GB"}),
                Resource(id="XX125", "kind"="leave_request", attr={"geography":"GB"})
                ):
                do_thing()
    """

    _http: sessions.BaseUrlSession
    _logger: logging.Logger

    def __init__(
        self,
        host: str,
        *,
        timeout_secs: float = 2.0,
        retry_strategy: Optional[Retry] = None,
        tls_verify: Optional[Any] = None,
        playground_instance: Optional[str] = None,
        raise_on_error: bool = False,
        debug: bool = False,
        logger: Optional[logging.Logger] = None
    ):
        self._logger = logging.getLogger(__name__) if logger is None else logger
        http = sessions.BaseUrlSession(base_url=host)

        adapter = (
            TimeoutAdapter(timeout_secs=timeout_secs)
            if retry_strategy is None
            else TimeoutAdapter(timeout=timeout_secs, max_retries=retry_strategy)
        )
        http.mount("http://", adapter)
        http.mount("https://", adapter)

        ua = user_agent("cerbos-python", cerbos.__version__)
        http.headers.update({"User-Agent": ua})

        if playground_instance is not None:
            http.headers.update({"playground-instance": playground_instance})

        if tls_verify is not None:
            http.verify = tls_verify

        if debug:
            http.hooks["response"].append(
                lambda response, *args, **kwargs: self._logger.debug(
                    dump.dump_all(response).decode("utf-8")
                )
            )

        # This must go last to let the other hooks execute
        if raise_on_error:
            http.hooks["response"].append(
                lambda response, *args, **kwargs: response.raise_for_status()
            )

        self._http = http

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def check_resources(
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
        resp = self._http.post("/api/check/resources", data=req.to_json())
        if resp.status_code != requests.codes.ok:
            return CheckResourcesResponse(
                request_id=req_id,
                status_code=resp.status_code,
                status_msg=APIError.from_dict(resp.json()),
            )

        return CheckResourcesResponse.from_dict(resp.json())

    def is_allowed(
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
        resp = self.check_resources(
            principal=principal,
            resources=ResourceList().add(resource, {action}),
            request_id=request_id,
            aux_data=aux_data,
        )

        return resp.get_resource(resource.id).is_allowed(action)

    def is_healthy(self, svc: Optional[str] = None) -> bool:
        """Checks the health of the Cerbos endpoint"""

        params = None if svc is None else {"service": svc}
        try:
            resp = self._http.get("/_cerbos/health", params=params)
            return resp.status_code == requests.codes.ok
        except Exception:
            return False

    def with_principal(
        self, principal: Principal, aux_data: Optional[AuxData] = None
    ) -> "PrincipalContext":
        """Fixes the principal for subsequent requests"""

        return PrincipalContext(self, principal, aux_data)

    def close(self):
        self._http.close()


def _get_request_id(request_id: Optional[str]) -> str:
    if request_id is None:
        return str(uuid.uuid4())

    return request_id


class PrincipalContext:
    """A special Cerbos client where the principal and auxData are fixed"""

    _client: CerbosClient
    _principal: Principal
    _aux_data: Optional[AuxData]

    def __init__(
        self,
        client: CerbosClient,
        principal: Principal,
        aux_data: Optional[AuxData] = None,
    ):
        self._client = client
        self._principal = principal
        self._aux_data = aux_data

    def check_resources(
        self, resources: ResourceList, request_id: Optional[str] = None
    ) -> CheckResourcesResponse:
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

    def is_allowed(
        self, action: str, resource: Resource, request_id: Optional[str] = None
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
