from cerbos.engine.v1 import engine_pb2 as _engine_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccessLogEntry(_message.Message):
    __slots__ = ["call_id", "timestamp", "peer", "metadata", "method", "status_code"]
    class MetadataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MetaValues
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MetaValues, _Mapping]] = ...) -> None: ...
    CALL_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PEER_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    call_id: str
    timestamp: _timestamp_pb2.Timestamp
    peer: Peer
    metadata: _containers.MessageMap[str, MetaValues]
    method: str
    status_code: int
    def __init__(self, call_id: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., peer: _Optional[_Union[Peer, _Mapping]] = ..., metadata: _Optional[_Mapping[str, MetaValues]] = ..., method: _Optional[str] = ..., status_code: _Optional[int] = ...) -> None: ...

class DecisionLogEntry(_message.Message):
    __slots__ = ["call_id", "timestamp", "peer", "inputs", "outputs", "error", "check_resources", "plan_resources", "metadata"]
    class CheckResources(_message.Message):
        __slots__ = ["inputs", "outputs", "error"]
        INPUTS_FIELD_NUMBER: _ClassVar[int]
        OUTPUTS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        inputs: _containers.RepeatedCompositeFieldContainer[_engine_pb2.CheckInput]
        outputs: _containers.RepeatedCompositeFieldContainer[_engine_pb2.CheckOutput]
        error: str
        def __init__(self, inputs: _Optional[_Iterable[_Union[_engine_pb2.CheckInput, _Mapping]]] = ..., outputs: _Optional[_Iterable[_Union[_engine_pb2.CheckOutput, _Mapping]]] = ..., error: _Optional[str] = ...) -> None: ...
    class PlanResources(_message.Message):
        __slots__ = ["input", "output", "error"]
        INPUT_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        input: _engine_pb2.PlanResourcesInput
        output: _engine_pb2.PlanResourcesOutput
        error: str
        def __init__(self, input: _Optional[_Union[_engine_pb2.PlanResourcesInput, _Mapping]] = ..., output: _Optional[_Union[_engine_pb2.PlanResourcesOutput, _Mapping]] = ..., error: _Optional[str] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MetaValues
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MetaValues, _Mapping]] = ...) -> None: ...
    CALL_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PEER_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CHECK_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    PLAN_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    call_id: str
    timestamp: _timestamp_pb2.Timestamp
    peer: Peer
    inputs: _containers.RepeatedCompositeFieldContainer[_engine_pb2.CheckInput]
    outputs: _containers.RepeatedCompositeFieldContainer[_engine_pb2.CheckOutput]
    error: str
    check_resources: DecisionLogEntry.CheckResources
    plan_resources: DecisionLogEntry.PlanResources
    metadata: _containers.MessageMap[str, MetaValues]
    def __init__(self, call_id: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., peer: _Optional[_Union[Peer, _Mapping]] = ..., inputs: _Optional[_Iterable[_Union[_engine_pb2.CheckInput, _Mapping]]] = ..., outputs: _Optional[_Iterable[_Union[_engine_pb2.CheckOutput, _Mapping]]] = ..., error: _Optional[str] = ..., check_resources: _Optional[_Union[DecisionLogEntry.CheckResources, _Mapping]] = ..., plan_resources: _Optional[_Union[DecisionLogEntry.PlanResources, _Mapping]] = ..., metadata: _Optional[_Mapping[str, MetaValues]] = ...) -> None: ...

class MetaValues(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...

class Peer(_message.Message):
    __slots__ = ["address", "auth_info", "user_agent", "forwarded_for"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AUTH_INFO_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    FORWARDED_FOR_FIELD_NUMBER: _ClassVar[int]
    address: str
    auth_info: str
    user_agent: str
    forwarded_for: str
    def __init__(self, address: _Optional[str] = ..., auth_info: _Optional[str] = ..., user_agent: _Optional[str] = ..., forwarded_for: _Optional[str] = ...) -> None: ...
