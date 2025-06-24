from buf.validate import validate_pb2 as _validate_pb2
from cerbos.audit.v1 import audit_pb2 as _audit_pb2
from cerbos.cloud.pdp.v1 import pdp_pb2 as _pdp_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IngestBatch(_message.Message):
    __slots__ = ["id", "entries"]
    class EntryKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        ENTRY_KIND_UNSPECIFIED: _ClassVar[IngestBatch.EntryKind]
        ENTRY_KIND_ACCESS_LOG: _ClassVar[IngestBatch.EntryKind]
        ENTRY_KIND_DECISION_LOG: _ClassVar[IngestBatch.EntryKind]
    ENTRY_KIND_UNSPECIFIED: IngestBatch.EntryKind
    ENTRY_KIND_ACCESS_LOG: IngestBatch.EntryKind
    ENTRY_KIND_DECISION_LOG: IngestBatch.EntryKind
    class Entry(_message.Message):
        __slots__ = ["kind", "timestamp", "access_log_entry", "decision_log_entry"]
        KIND_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        ACCESS_LOG_ENTRY_FIELD_NUMBER: _ClassVar[int]
        DECISION_LOG_ENTRY_FIELD_NUMBER: _ClassVar[int]
        kind: IngestBatch.EntryKind
        timestamp: _timestamp_pb2.Timestamp
        access_log_entry: _audit_pb2.AccessLogEntry
        decision_log_entry: _audit_pb2.DecisionLogEntry
        def __init__(self, kind: _Optional[_Union[IngestBatch.EntryKind, str]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., access_log_entry: _Optional[_Union[_audit_pb2.AccessLogEntry, _Mapping]] = ..., decision_log_entry: _Optional[_Union[_audit_pb2.DecisionLogEntry, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    entries: _containers.RepeatedCompositeFieldContainer[IngestBatch.Entry]
    def __init__(self, id: _Optional[str] = ..., entries: _Optional[_Iterable[_Union[IngestBatch.Entry, _Mapping]]] = ...) -> None: ...

class IngestRequest(_message.Message):
    __slots__ = ["pdp_id", "batch"]
    PDP_ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    pdp_id: _pdp_pb2.Identifier
    batch: IngestBatch
    def __init__(self, pdp_id: _Optional[_Union[_pdp_pb2.Identifier, _Mapping]] = ..., batch: _Optional[_Union[IngestBatch, _Mapping]] = ...) -> None: ...

class IngestResponse(_message.Message):
    __slots__ = ["success", "backoff"]
    class Backoff(_message.Message):
        __slots__ = ["duration"]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        duration: _duration_pb2.Duration
        def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    BACKOFF_FIELD_NUMBER: _ClassVar[int]
    success: _empty_pb2.Empty
    backoff: IngestResponse.Backoff
    def __init__(self, success: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., backoff: _Optional[_Union[IngestResponse.Backoff, _Mapping]] = ...) -> None: ...
