# Copyright 2021-2025 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

from collections.abc import Callable, Mapping
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Union

import httpx
from dataclasses_json import LetterCase, config, dataclass_json


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
    roles: set[str]
    attr: dict[str, Any] = field(default_factory=dict)
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
    attr: dict[str, Any] = field(default_factory=dict)
    policy_version: str = "default"
    scope: str = ""

    def add_attr(self, name: str, value: Any) -> "Resource":
        self.attr[name] = value
        return self


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ResourceAction:
    resource: Resource
    actions: set[str]


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ResourceList:
    resources: list[ResourceAction] = field(default_factory=list)

    def add(self, resource: Resource, actions: set[str]) -> "ResourceList":
        self.resources.append(ResourceAction(resource=resource, actions=actions))
        return self


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class JWT:
    token: str
    key_set_id: str | None = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AuxData:
    jwt: JWT | None = None
    jwts: Mapping[str, JWT] | None = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CheckResourcesRequest:
    request_id: str
    principal: Principal
    resources: ResourceList
    aux_data: AuxData | None = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ValidationError:
    message: str
    source: Source
    path: str | None = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class OutputEntry:
    src: str
    val: Any
    action: str
    error: str | None = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class APIError:
    code: int
    message: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CheckResourcesResult:
    resource: Resource
    actions: dict[str, Effect]
    validation_errors: list[ValidationError] | None = None
    outputs: list[OutputEntry] | None = None

    def is_allowed(self, action: str) -> bool:
        if action in self.actions:
            return self.actions[action] == Effect.ALLOW

        return False


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CheckResourcesResponse:
    request_id: str
    results: list[CheckResourcesResult] | None = None
    status_code: int = httpx.codes.OK
    status_msg: APIError | None = None

    def failed(self) -> bool:
        return self.status_code != httpx.codes.OK

    def raise_if_failed(self) -> "CheckResourcesResponse":
        if not self.failed():
            return self

        raise CerbosRequestException(self.status_msg)

    def get_resource(
        self, id: str, predicate: Callable[[Resource], bool] = lambda _: True
    ) -> CheckResourcesResult | None:
        if self.failed():
            return None

        return next(
            (r for r in self.results if r.resource.id == id and predicate(r.resource)),
            None,
        )


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ResourceDesc:
    kind: str
    attr: dict[str, Any] = field(default_factory=dict)
    policy_version: str = "default"
    scope: str = ""

    def add_attr(self, name: str, value: Any) -> "ResourceDesc":
        self.attr[name] = value
        return self


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PlanResourcesRequest:
    request_id: str
    actions: list[str]
    principal: Principal
    resource: ResourceDesc
    aux_data: AuxData | None = None


Operand = Union[
    "PlanResourcesValue", "PlanResourcesVariable", "PlanResourcesExpression"
]


class PlanResourcesFilterKind(str, Enum):
    ALWAYS_ALLOWED = "KIND_ALWAYS_ALLOWED"
    ALWAYS_DENIED = "KIND_ALWAYS_DENIED"
    CONDITIONAL = "KIND_CONDITIONAL"


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PlanResourcesValue:
    value: Any


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PlanResourcesVariable:
    variable: str


def decode_operand_list(val):
    if not isinstance(val, list):
        return val

    return [decode_operand(op) for op in val]


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PlanResourcesExpression:
    @dataclass_json(letter_case=LetterCase.CAMEL)
    @dataclass
    class Expr:
        operator: str
        operands: list[Operand] = field(metadata=config(decoder=decode_operand_list))

    expression: Expr


def decode_operand(val):
    if not isinstance(val, dict):
        return val

    if "value" in val:
        return PlanResourcesValue.from_dict(val)

    if "variable" in val:
        return PlanResourcesVariable.from_dict(val)

    if "expression" in val:
        return PlanResourcesExpression.from_dict(val)

    return val


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PlanResourcesFilter:
    kind: PlanResourcesFilterKind
    condition: Operand | None = field(
        default=None, metadata=config(decoder=decode_operand)
    )


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PlanResourcesResponse:
    request_id: str
    # `action` can be a list of strings, but we maintain the singular name for backwards compatibility
    action: str | list[str]
    resource_kind: str
    policy_version: str
    filter: PlanResourcesFilter | None = None
    validation_errors: list[ValidationError] | None = None
    status_code: int = httpx.codes.OK
    status_msg: APIError | None = None

    def failed(self) -> bool:
        return self.status_code != httpx.codes.OK

    def raise_if_failed(self) -> "PlanResourcesResponse":
        if not self.failed():
            return self

        raise CerbosRequestException(self.status_msg)


class CerbosRequestException(Exception):
    def __init__(self, error: APIError | None):
        msg = "unexpected error" if error is None else error.message
        super().__init__(msg)

        self.error = error


class CerbosTLSError(Exception): ...


class CerbosTypeError(Exception): ...
