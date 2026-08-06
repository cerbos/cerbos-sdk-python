from buf.validate import validate_pb2 as _validate_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Subject(_message.Message):
    __slots__ = ("type", "id", "properties")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    type: str
    id: str
    properties: _containers.MessageMap[str, _struct_pb2.Value]
    def __init__(self, type: _Optional[str] = ..., id: _Optional[str] = ..., properties: _Optional[_Mapping[str, _struct_pb2.Value]] = ...) -> None: ...

class Resource(_message.Message):
    __slots__ = ("type", "id", "properties")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    type: str
    id: str
    properties: _containers.MessageMap[str, _struct_pb2.Value]
    def __init__(self, type: _Optional[str] = ..., id: _Optional[str] = ..., properties: _Optional[_Mapping[str, _struct_pb2.Value]] = ...) -> None: ...

class Action(_message.Message):
    __slots__ = ("name", "properties")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    name: str
    properties: _containers.MessageMap[str, _struct_pb2.Value]
    def __init__(self, name: _Optional[str] = ..., properties: _Optional[_Mapping[str, _struct_pb2.Value]] = ...) -> None: ...

class AccessEvaluationRequest(_message.Message):
    __slots__ = ("subject", "resource", "action", "context")
    class ContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    subject: Subject
    resource: Resource
    action: Action
    context: _containers.MessageMap[str, _struct_pb2.Value]
    def __init__(self, subject: _Optional[_Union[Subject, _Mapping]] = ..., resource: _Optional[_Union[Resource, _Mapping]] = ..., action: _Optional[_Union[Action, _Mapping]] = ..., context: _Optional[_Mapping[str, _struct_pb2.Value]] = ...) -> None: ...

class AccessEvaluationResponse(_message.Message):
    __slots__ = ("decision", "context")
    class ContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    DECISION_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    decision: bool
    context: _containers.MessageMap[str, _struct_pb2.Value]
    def __init__(self, decision: _Optional[bool] = ..., context: _Optional[_Mapping[str, _struct_pb2.Value]] = ...) -> None: ...

class AccessEvaluationBatchRequest(_message.Message):
    __slots__ = ("subject", "resource", "action", "context", "evaluations", "options")
    class ContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    class Evaluation(_message.Message):
        __slots__ = ("subject", "resource", "action", "context")
        class ContextEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _struct_pb2.Value
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
        SUBJECT_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        subject: Subject
        resource: Resource
        action: Action
        context: _containers.MessageMap[str, _struct_pb2.Value]
        def __init__(self, subject: _Optional[_Union[Subject, _Mapping]] = ..., resource: _Optional[_Union[Resource, _Mapping]] = ..., action: _Optional[_Union[Action, _Mapping]] = ..., context: _Optional[_Mapping[str, _struct_pb2.Value]] = ...) -> None: ...
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    subject: Subject
    resource: Resource
    action: Action
    context: _containers.MessageMap[str, _struct_pb2.Value]
    evaluations: _containers.RepeatedCompositeFieldContainer[AccessEvaluationBatchRequest.Evaluation]
    options: AccessEvaluationsOptions
    def __init__(self, subject: _Optional[_Union[Subject, _Mapping]] = ..., resource: _Optional[_Union[Resource, _Mapping]] = ..., action: _Optional[_Union[Action, _Mapping]] = ..., context: _Optional[_Mapping[str, _struct_pb2.Value]] = ..., evaluations: _Optional[_Iterable[_Union[AccessEvaluationBatchRequest.Evaluation, _Mapping]]] = ..., options: _Optional[_Union[AccessEvaluationsOptions, _Mapping]] = ...) -> None: ...

class AccessEvaluationBatchResponse(_message.Message):
    __slots__ = ("evaluations",)
    EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    evaluations: _containers.RepeatedCompositeFieldContainer[AccessEvaluationResponse]
    def __init__(self, evaluations: _Optional[_Iterable[_Union[AccessEvaluationResponse, _Mapping]]] = ...) -> None: ...

class MetadataRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MetadataResponse(_message.Message):
    __slots__ = ("policy_decision_point", "access_evaluation_endpoint", "access_evaluations_endpoint")
    POLICY_DECISION_POINT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_EVALUATION_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_EVALUATIONS_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    policy_decision_point: str
    access_evaluation_endpoint: str
    access_evaluations_endpoint: str
    def __init__(self, policy_decision_point: _Optional[str] = ..., access_evaluation_endpoint: _Optional[str] = ..., access_evaluations_endpoint: _Optional[str] = ...) -> None: ...

class AccessEvaluationsOptions(_message.Message):
    __slots__ = ("evaluations_semantic",)
    EVALUATIONS_SEMANTIC_FIELD_NUMBER: _ClassVar[int]
    evaluations_semantic: str
    def __init__(self, evaluations_semantic: _Optional[str] = ...) -> None: ...
