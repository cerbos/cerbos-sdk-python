# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Set

import requests
from dataclasses_json import LetterCase, dataclass_json


class Effect(str, Enum):
    DENY = "EFFECT_DENY"
    ALLOW = "EFFECT_ALLOW"


class Source(str, Enum):
    PRINCIPAL = "SOURCE_PRINCIPAL"
    RESOURCE = "SOURCE_RESOURCE"


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Principal:
    id: str
    roles: Set[str]
    attr: Dict[str, Any] = field(default_factory=dict)
    policy_version: str = "default"
    scope: str = ""

    def add_attr(self, name: str, value: Any) -> "Principal":
        self.attr[name] = value
        return self


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Resource:
    id: str
    kind: str
    attr: Dict[str, Any] = field(default_factory=dict)
    policy_version: str = "default"
    scope: str = ""

    def add_attr(self, name: str, value: Any) -> "Resource":
        self.attr[name] = value
        return self


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ResourceAction:
    resource: Resource
    actions: Set[str]


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ResourceList:
    resources: List[ResourceAction] = field(default_factory=list)

    def add(self, resource: Resource, actions: Set[str]) -> "ResourceList":
        self.resources.append(ResourceAction(resource=resource, actions=actions))
        return self


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class JWT:
    token: str
    key_set_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AuxData:
    jwt: JWT


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CheckResourcesRequest:
    request_id: str
    principal: Principal
    resources: ResourceList
    aux_data: Optional[AuxData] = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ValidationError:
    path: str
    message: str
    source: Source


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class APIError:
    code: int
    message: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CheckResourcesResult:
    resource: Resource
    actions: Dict[str, Effect]
    validation_errors: Optional[List[ValidationError]] = None

    def is_allowed(self, action: str) -> bool:
        if action in self.actions:
            return self.actions[action] == Effect.ALLOW

        return False


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CheckResourcesResponse:
    request_id: str
    results: Optional[List[CheckResourcesResult]] = None
    status_code: int = requests.codes.ok
    status_msg: Optional[APIError] = None

    def failed(self) -> bool:
        return self.status_code != requests.codes.ok

    def raise_if_failed(self) -> "CheckResourcesResponse":
        if not self.failed():
            return self

        raise CerbosRequestException(self.status_msg)

    def get_resource(
        self, id: str, predicate: Callable[[Resource], bool] = lambda _: True
    ) -> Optional[CheckResourcesResult]:
        if self.failed():
            return None

        return next(
            (r for r in self.results if r.resource.id == id and predicate(r.resource)),
            None,
        )


class CerbosRequestException(Exception):
    def __init__(self, error: Optional[APIError]):
        msg = "unexpected error" if error is None else error.message
        super(CerbosRequestException, self).__init__(msg)

        self.error = error
