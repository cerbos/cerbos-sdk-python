from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Identifier(_message.Message):
    __slots__ = ["instance", "version"]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    instance: str
    version: str
    def __init__(self, instance: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...
