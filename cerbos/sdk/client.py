# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

from typing import Optional
from cerbos.sdk.model import *
from requests.packages.urllib3.util.retry import Retry
from requests_toolbelt import sessions
from requests_toolbelt.utils import dump
from cerbos.sdk.util import TimeoutAdapter
from cerbos.sdk.model import *
import logging
import uuid


class Client:
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
        http.hooks["response"].append(
            lambda response, *args, **kwargs: response.raise_for_status()
        )

        self._http = http

    def check_resources(
        self,
        principal: Principal,
        resources: ResourceList,
        request_id: Optional[str] = None,
        aux_data: Optional[AuxData] = None,
    ) -> CheckResourcesResponse:
        req_id = _get_request_id(request_id)
        req = CheckResourcesRequest(
            request_id=req_id,
            principal=principal,
            resources=resources.resources,
            aux_data=aux_data,
        )
        resp = self._http.post("/api/check/resources", data=req.to_json())

        return CheckResourcesResponse.from_dict(resp.json())

    def is_allowed(
        self,
        action: str,
        principal: Principal,
        resource: Resource,
        request_id: Optional[str] = None,
        aux_data: Optional[AuxData] = None,
    ) -> bool:
        resources = ResourceList().add(resource, {action})
        resp = self.check_resources(
            principal=principal,
            resources=resources,
            request_id=request_id,
            aux_data=aux_data,
        )

        return resp.results[0].actions[action] == Effect.ALLOW


def _get_request_id(request_id: Optional[str]) -> str:
    if request_id is None:
        return str(uuid.uuid4())

    return request_id


class PrincipalContext:
    _client: Client
    _principal: Principal
    _aux_data: Optional[AuxData]

    def __init__(
        self, client: Client, principal: Principal, aux_data: Optional[AuxData] = None
    ):
        self._client = client
        self._principal = principal
        self._aux_data = aux_data

    def check_resources(
        self, resources: ResourceList, request_id: Optional[str] = None
    ) -> CheckResourcesResponse:
        return self._client.check_resources(
            principal=self._principal,
            resources=resources,
            request_id=request_id,
            aux_data=self._aux_data,
        )

    def is_allowed(
        self, action: str, resource: Resource, request_id: Optional[str] = None
    ) -> bool:
        return self._client.is_allowed(
            action=action,
            principal=self._principal,
            resource=resource,
            request_id=request_id,
            aux_data=self._aux_data,
        )
