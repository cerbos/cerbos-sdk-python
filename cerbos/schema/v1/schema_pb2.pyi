from google.api import field_behavior_pb2 as _field_behavior_pb2
from protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValidationError(_message.Message):
    __slots__ = ["path", "message", "source"]
    class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        SOURCE_UNSPECIFIED: _ClassVar[ValidationError.Source]
        SOURCE_PRINCIPAL: _ClassVar[ValidationError.Source]
        SOURCE_RESOURCE: _ClassVar[ValidationError.Source]
    SOURCE_UNSPECIFIED: ValidationError.Source
    SOURCE_PRINCIPAL: ValidationError.Source
    SOURCE_RESOURCE: ValidationError.Source
    PATH_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    path: str
    message: str
    source: ValidationError.Source
    def __init__(self, path: _Optional[str] = ..., message: _Optional[str] = ..., source: _Optional[_Union[ValidationError.Source, str]] = ...) -> None: ...

class Schema(_message.Message):
    __slots__ = ["id", "definition"]
    ID_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_FIELD_NUMBER: _ClassVar[int]
    id: str
    definition: bytes
    def __init__(self, id: _Optional[str] = ..., definition: _Optional[bytes] = ...) -> None: ...
