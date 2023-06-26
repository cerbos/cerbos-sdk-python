from cerbos.effect.v1 import effect_pb2 as _effect_pb2
from cerbos.schema.v1 import schema_pb2 as _schema_pb2
from google.api.expr.v1alpha1 import checked_pb2 as _checked_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuxData(_message.Message):
    __slots__ = ["jwt"]
    class JwtEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    JWT_FIELD_NUMBER: _ClassVar[int]
    jwt: _containers.MessageMap[str, _struct_pb2.Value]
    def __init__(self, jwt: _Optional[_Mapping[str, _struct_pb2.Value]] = ...) -> None: ...

class CheckInput(_message.Message):
    __slots__ = ["actions", "aux_data", "principal", "request_id", "resource"]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    AUX_DATA_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedScalarFieldContainer[str]
    aux_data: AuxData
    principal: Principal
    request_id: str
    resource: Resource
    def __init__(self, request_id: _Optional[str] = ..., resource: _Optional[_Union[Resource, _Mapping]] = ..., principal: _Optional[_Union[Principal, _Mapping]] = ..., actions: _Optional[_Iterable[str]] = ..., aux_data: _Optional[_Union[AuxData, _Mapping]] = ...) -> None: ...

class CheckOutput(_message.Message):
    __slots__ = ["actions", "effective_derived_roles", "outputs", "request_id", "resource_id", "validation_errors"]
    class ActionEffect(_message.Message):
        __slots__ = ["effect", "policy", "scope"]
        EFFECT_FIELD_NUMBER: _ClassVar[int]
        POLICY_FIELD_NUMBER: _ClassVar[int]
        SCOPE_FIELD_NUMBER: _ClassVar[int]
        effect: _effect_pb2.Effect
        policy: str
        scope: str
        def __init__(self, effect: _Optional[_Union[_effect_pb2.Effect, str]] = ..., policy: _Optional[str] = ..., scope: _Optional[str] = ...) -> None: ...
    class ActionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CheckOutput.ActionEffect
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CheckOutput.ActionEffect, _Mapping]] = ...) -> None: ...
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_DERIVED_ROLES_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.MessageMap[str, CheckOutput.ActionEffect]
    effective_derived_roles: _containers.RepeatedScalarFieldContainer[str]
    outputs: _containers.RepeatedCompositeFieldContainer[OutputEntry]
    request_id: str
    resource_id: str
    validation_errors: _containers.RepeatedCompositeFieldContainer[_schema_pb2.ValidationError]
    def __init__(self, request_id: _Optional[str] = ..., resource_id: _Optional[str] = ..., actions: _Optional[_Mapping[str, CheckOutput.ActionEffect]] = ..., effective_derived_roles: _Optional[_Iterable[str]] = ..., validation_errors: _Optional[_Iterable[_Union[_schema_pb2.ValidationError, _Mapping]]] = ..., outputs: _Optional[_Iterable[_Union[OutputEntry, _Mapping]]] = ...) -> None: ...

class OutputEntry(_message.Message):
    __slots__ = ["src", "val"]
    SRC_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    src: str
    val: _struct_pb2.Value
    def __init__(self, src: _Optional[str] = ..., val: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...

class PlanResourcesAst(_message.Message):
    __slots__ = ["filter_ast"]
    class LogicalOperation(_message.Message):
        __slots__ = ["nodes", "operator"]
        class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        NODES_FIELD_NUMBER: _ClassVar[int]
        OPERATOR_AND: PlanResourcesAst.LogicalOperation.Operator
        OPERATOR_FIELD_NUMBER: _ClassVar[int]
        OPERATOR_NOT: PlanResourcesAst.LogicalOperation.Operator
        OPERATOR_OR: PlanResourcesAst.LogicalOperation.Operator
        OPERATOR_UNSPECIFIED: PlanResourcesAst.LogicalOperation.Operator
        nodes: _containers.RepeatedCompositeFieldContainer[PlanResourcesAst.Node]
        operator: PlanResourcesAst.LogicalOperation.Operator
        def __init__(self, operator: _Optional[_Union[PlanResourcesAst.LogicalOperation.Operator, str]] = ..., nodes: _Optional[_Iterable[_Union[PlanResourcesAst.Node, _Mapping]]] = ...) -> None: ...
    class Node(_message.Message):
        __slots__ = ["expression", "logical_operation"]
        EXPRESSION_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_OPERATION_FIELD_NUMBER: _ClassVar[int]
        expression: _checked_pb2.CheckedExpr
        logical_operation: PlanResourcesAst.LogicalOperation
        def __init__(self, logical_operation: _Optional[_Union[PlanResourcesAst.LogicalOperation, _Mapping]] = ..., expression: _Optional[_Union[_checked_pb2.CheckedExpr, _Mapping]] = ...) -> None: ...
    FILTER_AST_FIELD_NUMBER: _ClassVar[int]
    filter_ast: PlanResourcesAst.Node
    def __init__(self, filter_ast: _Optional[_Union[PlanResourcesAst.Node, _Mapping]] = ...) -> None: ...

class PlanResourcesFilter(_message.Message):
    __slots__ = ["condition", "kind"]
    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Expression(_message.Message):
        __slots__ = ["operands", "operator"]
        class Operand(_message.Message):
            __slots__ = ["expression", "value", "variable"]
            EXPRESSION_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            VARIABLE_FIELD_NUMBER: _ClassVar[int]
            expression: PlanResourcesFilter.Expression
            value: _struct_pb2.Value
            variable: str
            def __init__(self, value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., expression: _Optional[_Union[PlanResourcesFilter.Expression, _Mapping]] = ..., variable: _Optional[str] = ...) -> None: ...
        OPERANDS_FIELD_NUMBER: _ClassVar[int]
        OPERATOR_FIELD_NUMBER: _ClassVar[int]
        operands: _containers.RepeatedCompositeFieldContainer[PlanResourcesFilter.Expression.Operand]
        operator: str
        def __init__(self, operator: _Optional[str] = ..., operands: _Optional[_Iterable[_Union[PlanResourcesFilter.Expression.Operand, _Mapping]]] = ...) -> None: ...
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    KIND_ALWAYS_ALLOWED: PlanResourcesFilter.Kind
    KIND_ALWAYS_DENIED: PlanResourcesFilter.Kind
    KIND_CONDITIONAL: PlanResourcesFilter.Kind
    KIND_FIELD_NUMBER: _ClassVar[int]
    KIND_UNSPECIFIED: PlanResourcesFilter.Kind
    condition: PlanResourcesFilter.Expression.Operand
    kind: PlanResourcesFilter.Kind
    def __init__(self, kind: _Optional[_Union[PlanResourcesFilter.Kind, str]] = ..., condition: _Optional[_Union[PlanResourcesFilter.Expression.Operand, _Mapping]] = ...) -> None: ...

class PlanResourcesInput(_message.Message):
    __slots__ = ["action", "aux_data", "include_meta", "principal", "request_id", "resource"]
    class Resource(_message.Message):
        __slots__ = ["attr", "kind", "policy_version", "scope"]
        class AttrEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _struct_pb2.Value
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
        ATTR_FIELD_NUMBER: _ClassVar[int]
        KIND_FIELD_NUMBER: _ClassVar[int]
        POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
        SCOPE_FIELD_NUMBER: _ClassVar[int]
        attr: _containers.MessageMap[str, _struct_pb2.Value]
        kind: str
        policy_version: str
        scope: str
        def __init__(self, kind: _Optional[str] = ..., attr: _Optional[_Mapping[str, _struct_pb2.Value]] = ..., policy_version: _Optional[str] = ..., scope: _Optional[str] = ...) -> None: ...
    ACTION_FIELD_NUMBER: _ClassVar[int]
    AUX_DATA_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_META_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    action: str
    aux_data: AuxData
    include_meta: bool
    principal: Principal
    request_id: str
    resource: PlanResourcesInput.Resource
    def __init__(self, request_id: _Optional[str] = ..., action: _Optional[str] = ..., principal: _Optional[_Union[Principal, _Mapping]] = ..., resource: _Optional[_Union[PlanResourcesInput.Resource, _Mapping]] = ..., aux_data: _Optional[_Union[AuxData, _Mapping]] = ..., include_meta: bool = ...) -> None: ...

class PlanResourcesOutput(_message.Message):
    __slots__ = ["action", "filter", "filter_debug", "kind", "policy_version", "request_id", "scope", "validation_errors"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    FILTER_DEBUG_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    action: str
    filter: PlanResourcesFilter
    filter_debug: str
    kind: str
    policy_version: str
    request_id: str
    scope: str
    validation_errors: _containers.RepeatedCompositeFieldContainer[_schema_pb2.ValidationError]
    def __init__(self, request_id: _Optional[str] = ..., action: _Optional[str] = ..., kind: _Optional[str] = ..., policy_version: _Optional[str] = ..., scope: _Optional[str] = ..., filter: _Optional[_Union[PlanResourcesFilter, _Mapping]] = ..., filter_debug: _Optional[str] = ..., validation_errors: _Optional[_Iterable[_Union[_schema_pb2.ValidationError, _Mapping]]] = ...) -> None: ...

class Principal(_message.Message):
    __slots__ = ["attr", "id", "policy_version", "roles", "scope"]
    class AttrEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    ATTR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    attr: _containers.MessageMap[str, _struct_pb2.Value]
    id: str
    policy_version: str
    roles: _containers.RepeatedScalarFieldContainer[str]
    scope: str
    def __init__(self, id: _Optional[str] = ..., policy_version: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., attr: _Optional[_Mapping[str, _struct_pb2.Value]] = ..., scope: _Optional[str] = ...) -> None: ...

class Resource(_message.Message):
    __slots__ = ["attr", "id", "kind", "policy_version", "scope"]
    class AttrEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    ATTR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    attr: _containers.MessageMap[str, _struct_pb2.Value]
    id: str
    kind: str
    policy_version: str
    scope: str
    def __init__(self, kind: _Optional[str] = ..., policy_version: _Optional[str] = ..., id: _Optional[str] = ..., attr: _Optional[_Mapping[str, _struct_pb2.Value]] = ..., scope: _Optional[str] = ...) -> None: ...

class Trace(_message.Message):
    __slots__ = ["components", "event"]
    class Component(_message.Message):
        __slots__ = ["action", "derived_role", "expr", "index", "kind", "output", "policy", "resource", "rule", "scope", "variable"]
        class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        class Variable(_message.Message):
            __slots__ = ["expr", "name"]
            EXPR_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            expr: str
            name: str
            def __init__(self, name: _Optional[str] = ..., expr: _Optional[str] = ...) -> None: ...
        ACTION_FIELD_NUMBER: _ClassVar[int]
        DERIVED_ROLE_FIELD_NUMBER: _ClassVar[int]
        EXPR_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        KIND_ACTION: Trace.Component.Kind
        KIND_CONDITION: Trace.Component.Kind
        KIND_CONDITION_ALL: Trace.Component.Kind
        KIND_CONDITION_ANY: Trace.Component.Kind
        KIND_CONDITION_NONE: Trace.Component.Kind
        KIND_DERIVED_ROLE: Trace.Component.Kind
        KIND_EXPR: Trace.Component.Kind
        KIND_FIELD_NUMBER: _ClassVar[int]
        KIND_OUTPUT: Trace.Component.Kind
        KIND_POLICY: Trace.Component.Kind
        KIND_RESOURCE: Trace.Component.Kind
        KIND_RULE: Trace.Component.Kind
        KIND_SCOPE: Trace.Component.Kind
        KIND_UNSPECIFIED: Trace.Component.Kind
        KIND_VARIABLE: Trace.Component.Kind
        KIND_VARIABLES: Trace.Component.Kind
        OUTPUT_FIELD_NUMBER: _ClassVar[int]
        POLICY_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_FIELD_NUMBER: _ClassVar[int]
        RULE_FIELD_NUMBER: _ClassVar[int]
        SCOPE_FIELD_NUMBER: _ClassVar[int]
        VARIABLE_FIELD_NUMBER: _ClassVar[int]
        action: str
        derived_role: str
        expr: str
        index: int
        kind: Trace.Component.Kind
        output: str
        policy: str
        resource: str
        rule: str
        scope: str
        variable: Trace.Component.Variable
        def __init__(self, kind: _Optional[_Union[Trace.Component.Kind, str]] = ..., action: _Optional[str] = ..., derived_role: _Optional[str] = ..., expr: _Optional[str] = ..., index: _Optional[int] = ..., policy: _Optional[str] = ..., resource: _Optional[str] = ..., rule: _Optional[str] = ..., scope: _Optional[str] = ..., variable: _Optional[_Union[Trace.Component.Variable, _Mapping]] = ..., output: _Optional[str] = ...) -> None: ...
    class Event(_message.Message):
        __slots__ = ["effect", "error", "message", "result", "status"]
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        EFFECT_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        RESULT_FIELD_NUMBER: _ClassVar[int]
        STATUS_ACTIVATED: Trace.Event.Status
        STATUS_FIELD_NUMBER: _ClassVar[int]
        STATUS_SKIPPED: Trace.Event.Status
        STATUS_UNSPECIFIED: Trace.Event.Status
        effect: _effect_pb2.Effect
        error: str
        message: str
        result: _struct_pb2.Value
        status: Trace.Event.Status
        def __init__(self, status: _Optional[_Union[Trace.Event.Status, str]] = ..., effect: _Optional[_Union[_effect_pb2.Effect, str]] = ..., error: _Optional[str] = ..., message: _Optional[str] = ..., result: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    components: _containers.RepeatedCompositeFieldContainer[Trace.Component]
    event: Trace.Event
    def __init__(self, components: _Optional[_Iterable[_Union[Trace.Component, _Mapping]]] = ..., event: _Optional[_Union[Trace.Event, _Mapping]] = ...) -> None: ...
