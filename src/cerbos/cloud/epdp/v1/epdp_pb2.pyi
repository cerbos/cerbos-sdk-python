from cerbos.policy.v1 import policy_pb2 as _policy_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Metadata(_message.Message):
    __slots__ = ["version", "policies", "build_timestamp", "commit_hash", "source_attributes"]
    class SourceAttributesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _policy_pb2.SourceAttributes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_policy_pb2.SourceAttributes, _Mapping]] = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    BUILD_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    COMMIT_HASH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    version: str
    policies: _containers.RepeatedScalarFieldContainer[str]
    build_timestamp: int
    commit_hash: str
    source_attributes: _containers.MessageMap[str, _policy_pb2.SourceAttributes]
    def __init__(self, version: _Optional[str] = ..., policies: _Optional[_Iterable[str]] = ..., build_timestamp: _Optional[int] = ..., commit_hash: _Optional[str] = ..., source_attributes: _Optional[_Mapping[str, _policy_pb2.SourceAttributes]] = ...) -> None: ...
