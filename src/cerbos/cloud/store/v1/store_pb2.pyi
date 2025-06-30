from buf.validate import validate_pb2 as _validate_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StringMatch(_message.Message):
    __slots__ = ["equals", "contains"]
    class InList(_message.Message):
        __slots__ = ["values"]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...
    EQUALS_FIELD_NUMBER: _ClassVar[int]
    CONTAINS_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    equals: str
    contains: str
    def __init__(self, equals: _Optional[str] = ..., contains: _Optional[str] = ..., **kwargs) -> None: ...

class FileFilter(_message.Message):
    __slots__ = ["path"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: StringMatch
    def __init__(self, path: _Optional[_Union[StringMatch, _Mapping]] = ...) -> None: ...

class ListFilesRequest(_message.Message):
    __slots__ = ["store_id", "filter"]
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    filter: FileFilter
    def __init__(self, store_id: _Optional[str] = ..., filter: _Optional[_Union[FileFilter, _Mapping]] = ...) -> None: ...

class ListFilesResponse(_message.Message):
    __slots__ = ["store_version", "files"]
    STORE_VERSION_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    store_version: int
    files: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, store_version: _Optional[int] = ..., files: _Optional[_Iterable[str]] = ...) -> None: ...

class GetFilesRequest(_message.Message):
    __slots__ = ["store_id", "files"]
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    files: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, store_id: _Optional[str] = ..., files: _Optional[_Iterable[str]] = ...) -> None: ...

class File(_message.Message):
    __slots__ = ["path", "contents"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    path: str
    contents: bytes
    def __init__(self, path: _Optional[str] = ..., contents: _Optional[bytes] = ...) -> None: ...

class GetFilesResponse(_message.Message):
    __slots__ = ["store_version", "files"]
    STORE_VERSION_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    store_version: int
    files: _containers.RepeatedCompositeFieldContainer[File]
    def __init__(self, store_version: _Optional[int] = ..., files: _Optional[_Iterable[_Union[File, _Mapping]]] = ...) -> None: ...

class ChangeDetails(_message.Message):
    __slots__ = ["description", "uploader", "git", "internal"]
    class Git(_message.Message):
        __slots__ = ["repo", "ref", "hash", "message", "committer", "commit_date", "author", "author_date"]
        REPO_FIELD_NUMBER: _ClassVar[int]
        REF_FIELD_NUMBER: _ClassVar[int]
        HASH_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        COMMITTER_FIELD_NUMBER: _ClassVar[int]
        COMMIT_DATE_FIELD_NUMBER: _ClassVar[int]
        AUTHOR_FIELD_NUMBER: _ClassVar[int]
        AUTHOR_DATE_FIELD_NUMBER: _ClassVar[int]
        repo: str
        ref: str
        hash: str
        message: str
        committer: str
        commit_date: _timestamp_pb2.Timestamp
        author: str
        author_date: _timestamp_pb2.Timestamp
        def __init__(self, repo: _Optional[str] = ..., ref: _Optional[str] = ..., hash: _Optional[str] = ..., message: _Optional[str] = ..., committer: _Optional[str] = ..., commit_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., author: _Optional[str] = ..., author_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Internal(_message.Message):
        __slots__ = ["source", "metadata"]
        class MetadataEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _struct_pb2.Value
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        METADATA_FIELD_NUMBER: _ClassVar[int]
        source: str
        metadata: _containers.MessageMap[str, _struct_pb2.Value]
        def __init__(self, source: _Optional[str] = ..., metadata: _Optional[_Mapping[str, _struct_pb2.Value]] = ...) -> None: ...
    class Uploader(_message.Message):
        __slots__ = ["name", "metadata"]
        class MetadataEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _struct_pb2.Value
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        METADATA_FIELD_NUMBER: _ClassVar[int]
        name: str
        metadata: _containers.MessageMap[str, _struct_pb2.Value]
        def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Mapping[str, _struct_pb2.Value]] = ...) -> None: ...
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UPLOADER_FIELD_NUMBER: _ClassVar[int]
    GIT_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_FIELD_NUMBER: _ClassVar[int]
    description: str
    uploader: ChangeDetails.Uploader
    git: ChangeDetails.Git
    internal: ChangeDetails.Internal
    def __init__(self, description: _Optional[str] = ..., uploader: _Optional[_Union[ChangeDetails.Uploader, _Mapping]] = ..., git: _Optional[_Union[ChangeDetails.Git, _Mapping]] = ..., internal: _Optional[_Union[ChangeDetails.Internal, _Mapping]] = ...) -> None: ...

class FileOp(_message.Message):
    __slots__ = ["add_or_update", "delete"]
    ADD_OR_UPDATE_FIELD_NUMBER: _ClassVar[int]
    DELETE_FIELD_NUMBER: _ClassVar[int]
    add_or_update: File
    delete: str
    def __init__(self, add_or_update: _Optional[_Union[File, _Mapping]] = ..., delete: _Optional[str] = ...) -> None: ...

class ModifyFilesRequest(_message.Message):
    __slots__ = ["store_id", "condition", "operations", "change_details"]
    class Condition(_message.Message):
        __slots__ = ["store_version_must_equal"]
        STORE_VERSION_MUST_EQUAL_FIELD_NUMBER: _ClassVar[int]
        store_version_must_equal: int
        def __init__(self, store_version_must_equal: _Optional[int] = ...) -> None: ...
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    CHANGE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    condition: ModifyFilesRequest.Condition
    operations: _containers.RepeatedCompositeFieldContainer[FileOp]
    change_details: ChangeDetails
    def __init__(self, store_id: _Optional[str] = ..., condition: _Optional[_Union[ModifyFilesRequest.Condition, _Mapping]] = ..., operations: _Optional[_Iterable[_Union[FileOp, _Mapping]]] = ..., change_details: _Optional[_Union[ChangeDetails, _Mapping]] = ...) -> None: ...

class FileError(_message.Message):
    __slots__ = ["file", "cause", "details"]
    class Cause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        CAUSE_UNSPECIFIED: _ClassVar[FileError.Cause]
        CAUSE_INVALID_FILE_PATH: _ClassVar[FileError.Cause]
        CAUSE_UNSUPPORTED_FILE_EXTENSION: _ClassVar[FileError.Cause]
        CAUSE_INVALID_FILE_CONTENTS: _ClassVar[FileError.Cause]
        CAUSE_DUPLICATE_FILE_PATH: _ClassVar[FileError.Cause]
        CAUSE_FILE_TOO_LARGE: _ClassVar[FileError.Cause]
    CAUSE_UNSPECIFIED: FileError.Cause
    CAUSE_INVALID_FILE_PATH: FileError.Cause
    CAUSE_UNSUPPORTED_FILE_EXTENSION: FileError.Cause
    CAUSE_INVALID_FILE_CONTENTS: FileError.Cause
    CAUSE_DUPLICATE_FILE_PATH: FileError.Cause
    CAUSE_FILE_TOO_LARGE: FileError.Cause
    FILE_FIELD_NUMBER: _ClassVar[int]
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    file: str
    cause: FileError.Cause
    details: str
    def __init__(self, file: _Optional[str] = ..., cause: _Optional[_Union[FileError.Cause, str]] = ..., details: _Optional[str] = ...) -> None: ...

class ModifyFilesResponse(_message.Message):
    __slots__ = ["new_store_version"]
    NEW_STORE_VERSION_FIELD_NUMBER: _ClassVar[int]
    new_store_version: int
    def __init__(self, new_store_version: _Optional[int] = ...) -> None: ...

class ReplaceFilesRequest(_message.Message):
    __slots__ = ["store_id", "condition", "zipped_contents", "files", "change_details"]
    class Condition(_message.Message):
        __slots__ = ["store_version_must_equal"]
        STORE_VERSION_MUST_EQUAL_FIELD_NUMBER: _ClassVar[int]
        store_version_must_equal: int
        def __init__(self, store_version_must_equal: _Optional[int] = ...) -> None: ...
    class Files(_message.Message):
        __slots__ = ["files"]
        FILES_FIELD_NUMBER: _ClassVar[int]
        files: _containers.RepeatedCompositeFieldContainer[File]
        def __init__(self, files: _Optional[_Iterable[_Union[File, _Mapping]]] = ...) -> None: ...
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    ZIPPED_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    CHANGE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    condition: ReplaceFilesRequest.Condition
    zipped_contents: bytes
    files: ReplaceFilesRequest.Files
    change_details: ChangeDetails
    def __init__(self, store_id: _Optional[str] = ..., condition: _Optional[_Union[ReplaceFilesRequest.Condition, _Mapping]] = ..., zipped_contents: _Optional[bytes] = ..., files: _Optional[_Union[ReplaceFilesRequest.Files, _Mapping]] = ..., change_details: _Optional[_Union[ChangeDetails, _Mapping]] = ...) -> None: ...

class ErrDetailValidationFailure(_message.Message):
    __slots__ = ["errors"]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[FileError]
    def __init__(self, errors: _Optional[_Iterable[_Union[FileError, _Mapping]]] = ...) -> None: ...

class ErrDetailNoUsableFiles(_message.Message):
    __slots__ = ["ignored_files"]
    IGNORED_FILES_FIELD_NUMBER: _ClassVar[int]
    ignored_files: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ignored_files: _Optional[_Iterable[str]] = ...) -> None: ...

class ErrDetailConditionUnsatisfied(_message.Message):
    __slots__ = ["current_store_version"]
    CURRENT_STORE_VERSION_FIELD_NUMBER: _ClassVar[int]
    current_store_version: int
    def __init__(self, current_store_version: _Optional[int] = ...) -> None: ...

class ErrDetailOperationDiscarded(_message.Message):
    __slots__ = ["current_store_version", "ignored_files"]
    CURRENT_STORE_VERSION_FIELD_NUMBER: _ClassVar[int]
    IGNORED_FILES_FIELD_NUMBER: _ClassVar[int]
    current_store_version: int
    ignored_files: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, current_store_version: _Optional[int] = ..., ignored_files: _Optional[_Iterable[str]] = ...) -> None: ...

class ErrDetailCannotModifyGitConnectedStore(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ReplaceFilesResponse(_message.Message):
    __slots__ = ["new_store_version", "ignored_files"]
    NEW_STORE_VERSION_FIELD_NUMBER: _ClassVar[int]
    IGNORED_FILES_FIELD_NUMBER: _ClassVar[int]
    new_store_version: int
    ignored_files: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, new_store_version: _Optional[int] = ..., ignored_files: _Optional[_Iterable[str]] = ...) -> None: ...
