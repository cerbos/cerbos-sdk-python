from buf.validate import validate_pb2 as _validate_pb2
from cerbos.cloud.bundle.v1 import bundle_pb2 as _bundle_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PDPConfig(_message.Message):
    __slots__ = ["meta", "bundle_info"]
    class Meta(_message.Message):
        __slots__ = ["created_at", "commit_hash"]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        COMMIT_HASH_FIELD_NUMBER: _ClassVar[int]
        created_at: _timestamp_pb2.Timestamp
        commit_hash: str
        def __init__(self, created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., commit_hash: _Optional[str] = ...) -> None: ...
    META_FIELD_NUMBER: _ClassVar[int]
    BUNDLE_INFO_FIELD_NUMBER: _ClassVar[int]
    meta: PDPConfig.Meta
    bundle_info: _bundle_pb2.BundleInfo
    def __init__(self, meta: _Optional[_Union[PDPConfig.Meta, _Mapping]] = ..., bundle_info: _Optional[_Union[_bundle_pb2.BundleInfo, _Mapping]] = ...) -> None: ...
