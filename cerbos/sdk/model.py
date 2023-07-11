# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Set, Union

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
class OutputEntry:
    src: str
    val: Any


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
    outputs: Optional[List[OutputEntry]] = None

    def is_allowed(self, action: str) -> bool:
        if action in self.actions:
            return self.actions[action] == Effect.ALLOW

        return False


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CheckResourcesResponse:
    request_id: str
    results: Optional[List[CheckResourcesResult]] = None
    status_code: int = httpx.codes.OK
    status_msg: Optional[APIError] = None

    def failed(self) -> bool:
        return self.status_code != httpx.codes.OK

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


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PlanResourcesRequest:
    request_id: str
    action: str
    principal: Principal
    resource: ResourceDesc
    aux_data: Optional[AuxData] = None


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
        operands: List[Operand] = field(metadata=config(decoder=decode_operand_list))

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
    condition: Optional[Operand] = field(
        default=None, metadata=config(decoder=decode_operand)
    )


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PlanResourcesResponse:
    request_id: str
    action: str
    resource_kind: str
    policy_version: str
    filter: Optional[PlanResourcesFilter] = None
    validation_errors: Optional[List[ValidationError]] = None
    status_code: int = httpx.codes.OK
    status_msg: Optional[APIError] = None

    def failed(self) -> bool:
        return self.status_code != httpx.codes.OK

    def raise_if_failed(self) -> "PlanResourcesResponse":
        if not self.failed():
            return self

        raise CerbosRequestException(self.status_msg)


class CerbosRequestException(Exception):
    def __init__(self, error: Optional[APIError]):
        msg = "unexpected error" if error is None else error.message
        super(CerbosRequestException, self).__init__(msg)

        self.error = error


class CerbosTLSError(Exception):
    ...


class CerbosTypeError(Exception):
    ...
