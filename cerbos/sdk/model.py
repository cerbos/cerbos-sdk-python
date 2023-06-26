# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Set, Union

import httpx
from dataclasses_json import LetterCase, config, dataclass_json
from google.protobuf import struct_pb2

from cerbos.effect.v1 import effect_pb2
from cerbos.engine.v1 import engine_pb2
from cerbos.request.v1 import request_pb2
from cerbos.response.v1 import response_pb2


def get_resource(
    resp: response_pb2.CheckResourcesResponse,
    resource_id: str,
    predicate=lambda _: True,
) -> response_pb2.CheckResourcesResponse.ResultEntry:
    return next(filter(lambda r: r.resource.id == resource_id, resp.results), None)


def is_allowed(
    entry: response_pb2.CheckResourcesResponse.ResultEntry, action: str
) -> bool:
    if action in entry.actions:
        return entry.actions[action] == effect_pb2.EFFECT_ALLOW
    return False


def create_value(v):
    if isinstance(v, str):
        return struct_pb2.Value(string_value=v)
    elif isinstance(v, bool):
        return struct_pb2.Value(bool_value=v)
    elif isinstance(v, int) or isinstance(v, float):
        return struct_pb2.Value(number_value=v)
    elif isinstance(v, list):
        return struct_pb2.ListValue(v)
    elif isinstance(v, dict):
        return struct_pb2.Struct(v)

    return struct_pb2.Value(null_value=None)


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

    def to_proto(self) -> engine_pb2.Principal:
        return engine_pb2.Principal(
            id=self.id,
            policy_version=self.policy_version,
            roles=self.roles,
            scope=self.scope,
            attr={k: create_value(v) for k, v in self.attr.items()},
        )


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

    def to_proto(self) -> engine_pb2.Resource:
        return engine_pb2.Resource(
            id=self.id,
            kind=self.kind,
            policy_version=self.policy_version,
            scope=self.scope,
            attr={k: create_value(v) for k, v in self.attr.items()},
        )


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

    def to_proto(self) -> request_pb2.AuxData:
        return request_pb2.AuxData(
            jwt=request_pb2.AuxData.JWT(
                key_set_id=self.jwt.key_set_id,
                token=self.jwt.token,
            )
        )


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
class ResourceDesc:
    kind: str
    attr: Dict[str, Any] = field(default_factory=dict)
    policy_version: str = "default"
    scope: str = ""

    def add_attr(self, name: str, value: Any) -> "ResourceDesc":
        self.attr[name] = value
        return self

    def to_proto(self) -> engine_pb2.PlanResourcesInput.Resource:
        return engine_pb2.PlanResourcesInput.Resource(
            kind=self.kind,
            attr={k: create_value(v) for k, v in self.attr.items()},
            policy_version=self.policy_version,
            scope=self.scope,
        )


class CerbosRequestException(Exception):
    def __init__(self, error: Optional[APIError]):
        msg = "unexpected error" if error is None else error.message
        super(CerbosRequestException, self).__init__(msg)

        self.error = error
