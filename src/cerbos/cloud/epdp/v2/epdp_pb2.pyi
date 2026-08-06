import datetime

from buf.validate import validate_pb2 as _validate_pb2
from cerbos.audit.v1 import audit_pb2 as _audit_pb2
from cerbos.engine.v1 import engine_pb2 as _engine_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import code_pb2 as _code_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ("evaluator", "schema")
    class Evaluator(_message.Message):
        __slots__ = ("globals", "default_policy_version", "lenient_scope_search", "default_scope", "strict_evaluation")
        class GlobalsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _struct_pb2.Value
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
        GLOBALS_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
        LENIENT_SCOPE_SEARCH_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_SCOPE_FIELD_NUMBER: _ClassVar[int]
        STRICT_EVALUATION_FIELD_NUMBER: _ClassVar[int]
        globals: _containers.MessageMap[str, _struct_pb2.Value]
        default_policy_version: str
        lenient_scope_search: bool
        default_scope: str
        strict_evaluation: bool
        def __init__(self, globals: _Optional[_Mapping[str, _struct_pb2.Value]] = ..., default_policy_version: _Optional[str] = ..., lenient_scope_search: _Optional[bool] = ..., default_scope: _Optional[str] = ..., strict_evaluation: _Optional[bool] = ...) -> None: ...
    class Schema(_message.Message):
        __slots__ = ("enforcement",)
        class Enforcement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ENFORCEMENT_UNSPECIFIED: _ClassVar[Config.Schema.Enforcement]
            ENFORCEMENT_NONE: _ClassVar[Config.Schema.Enforcement]
            ENFORCEMENT_WARN: _ClassVar[Config.Schema.Enforcement]
            ENFORCEMENT_REJECT: _ClassVar[Config.Schema.Enforcement]
        ENFORCEMENT_UNSPECIFIED: Config.Schema.Enforcement
        ENFORCEMENT_NONE: Config.Schema.Enforcement
        ENFORCEMENT_WARN: Config.Schema.Enforcement
        ENFORCEMENT_REJECT: Config.Schema.Enforcement
        ENFORCEMENT_FIELD_NUMBER: _ClassVar[int]
        enforcement: Config.Schema.Enforcement
        def __init__(self, enforcement: _Optional[_Union[Config.Schema.Enforcement, str]] = ...) -> None: ...
    EVALUATOR_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    evaluator: Config.Evaluator
    schema: Config.Schema
    def __init__(self, evaluator: _Optional[_Union[Config.Evaluator, _Mapping]] = ..., schema: _Optional[_Union[Config.Schema, _Mapping]] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ("code", "message")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: _code_pb2.Code
    message: str
    def __init__(self, code: _Optional[_Union[_code_pb2.Code, str]] = ..., message: _Optional[str] = ...) -> None: ...

class Metadata(_message.Message):
    __slots__ = ("cerbos_version", "cerbos_commit_hash", "wasm_checksum", "built_at")
    CERBOS_VERSION_FIELD_NUMBER: _ClassVar[int]
    CERBOS_COMMIT_HASH_FIELD_NUMBER: _ClassVar[int]
    WASM_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    BUILT_AT_FIELD_NUMBER: _ClassVar[int]
    cerbos_version: str
    cerbos_commit_hash: str
    wasm_checksum: str
    built_at: _timestamp_pb2.Timestamp
    def __init__(self, cerbos_version: _Optional[str] = ..., cerbos_commit_hash: _Optional[str] = ..., wasm_checksum: _Optional[str] = ..., built_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class LoadRuleTableResponse(_message.Message):
    __slots__ = ("bundle_id",)
    BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
    bundle_id: str
    def __init__(self, bundle_id: _Optional[str] = ...) -> None: ...

class CheckResourcesRequest(_message.Message):
    __slots__ = ("inputs",)
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    inputs: _containers.RepeatedCompositeFieldContainer[_engine_pb2.CheckInput]
    def __init__(self, inputs: _Optional[_Iterable[_Union[_engine_pb2.CheckInput, _Mapping]]] = ...) -> None: ...

class CheckResourcesResponse(_message.Message):
    __slots__ = ("outputs", "audit_trail")
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    AUDIT_TRAIL_FIELD_NUMBER: _ClassVar[int]
    outputs: _containers.RepeatedCompositeFieldContainer[_engine_pb2.CheckOutput]
    audit_trail: _audit_pb2.AuditTrail
    def __init__(self, outputs: _Optional[_Iterable[_Union[_engine_pb2.CheckOutput, _Mapping]]] = ..., audit_trail: _Optional[_Union[_audit_pb2.AuditTrail, _Mapping]] = ...) -> None: ...

class PlanResourcesRequest(_message.Message):
    __slots__ = ("input",)
    INPUT_FIELD_NUMBER: _ClassVar[int]
    input: _engine_pb2.PlanResourcesInput
    def __init__(self, input: _Optional[_Union[_engine_pb2.PlanResourcesInput, _Mapping]] = ...) -> None: ...

class PlanResourcesResponse(_message.Message):
    __slots__ = ("output", "audit_trail")
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    AUDIT_TRAIL_FIELD_NUMBER: _ClassVar[int]
    output: _engine_pb2.PlanResourcesOutput
    audit_trail: _audit_pb2.AuditTrail
    def __init__(self, output: _Optional[_Union[_engine_pb2.PlanResourcesOutput, _Mapping]] = ..., audit_trail: _Optional[_Union[_audit_pb2.AuditTrail, _Mapping]] = ...) -> None: ...

class Bundle(_message.Message):
    __slots__ = ("metadata", "contents")
    class Metadata(_message.Message):
        __slots__ = ("bundle_id", "rule_revision")
        BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
        RULE_REVISION_FIELD_NUMBER: _ClassVar[int]
        bundle_id: str
        rule_revision: int
        def __init__(self, bundle_id: _Optional[str] = ..., rule_revision: _Optional[int] = ...) -> None: ...
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    metadata: Bundle.Metadata
    contents: bytes
    def __init__(self, metadata: _Optional[_Union[Bundle.Metadata, _Mapping]] = ..., contents: _Optional[bytes] = ...) -> None: ...

class GetBundleRequest(_message.Message):
    __slots__ = ("rule_id", "scopes", "if_modified_since")
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    IF_MODIFIED_SINCE_FIELD_NUMBER: _ClassVar[int]
    rule_id: str
    scopes: _containers.RepeatedScalarFieldContainer[str]
    if_modified_since: Bundle.Metadata
    def __init__(self, rule_id: _Optional[str] = ..., scopes: _Optional[_Iterable[str]] = ..., if_modified_since: _Optional[_Union[Bundle.Metadata, _Mapping]] = ...) -> None: ...

class GetBundleResponse(_message.Message):
    __slots__ = ("bundle", "not_modified")
    BUNDLE_FIELD_NUMBER: _ClassVar[int]
    NOT_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    bundle: Bundle
    not_modified: _empty_pb2.Empty
    def __init__(self, bundle: _Optional[_Union[Bundle, _Mapping]] = ..., not_modified: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ...) -> None: ...
