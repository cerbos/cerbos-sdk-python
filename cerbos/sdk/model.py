# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, LetterCase
from enum import Enum
from typing import Any, Optional, Set, Dict, List


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

    def add_attr(self, name: str, value: Any):
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

    def add_attr(self, name: str, value: Any):
        self.attr[name] = value
        return self


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ResourceList:
    resources: List[Dict[str, Any]] = field(default_factory=list)

    def add(self, resource: Resource, actions: Set[str]):
        self.resources.append({"resource": resource, "actions": actions})
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
    resources: List[Dict[str, Any]] = field(default_factory=list)
    aux_data: Optional[AuxData] = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ValidationError:
    path: str
    message: str
    source: Source


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CheckResourcesResult:
    resource: Resource
    actions: Dict[str, Effect]
    validation_errors: Optional[List[ValidationError]] = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CheckResourcesResponse:
    request_id: str
    results: List[CheckResourcesResult]
