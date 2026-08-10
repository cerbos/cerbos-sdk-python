import datetime

from buf.validate import validate_pb2 as _validate_pb2
from cerbos.engine.v1 import engine_pb2 as _engine_pb2
from cerbos.policy.v1 import policy_pb2 as _policy_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccessLogEntry(_message.Message):
    __slots__ = ("call_id", "timestamp", "peer", "metadata", "method", "status_code", "oversized", "policy_source", "request_context")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
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
    OVERSIZED_FIELD_NUMBER: _ClassVar[int]
    POLICY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    call_id: str
    timestamp: _timestamp_pb2.Timestamp
    peer: Peer
    metadata: _containers.MessageMap[str, MetaValues]
    method: str
    status_code: int
    oversized: bool
    policy_source: PolicySource
    request_context: RequestContext
    def __init__(self, call_id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., peer: _Optional[_Union[Peer, _Mapping]] = ..., metadata: _Optional[_Mapping[str, MetaValues]] = ..., method: _Optional[str] = ..., status_code: _Optional[int] = ..., oversized: _Optional[bool] = ..., policy_source: _Optional[_Union[PolicySource, _Mapping]] = ..., request_context: _Optional[_Union[RequestContext, _Mapping]] = ...) -> None: ...

class DecisionLogEntry(_message.Message):
    __slots__ = ("call_id", "timestamp", "peer", "inputs", "outputs", "error", "check_resources", "plan_resources", "metadata", "audit_trail", "oversized", "policy_source", "request_context")
    class CheckResources(_message.Message):
        __slots__ = ("inputs", "outputs", "error")
        INPUTS_FIELD_NUMBER: _ClassVar[int]
        OUTPUTS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        inputs: _containers.RepeatedCompositeFieldContainer[_engine_pb2.CheckInput]
        outputs: _containers.RepeatedCompositeFieldContainer[_engine_pb2.CheckOutput]
        error: str
        def __init__(self, inputs: _Optional[_Iterable[_Union[_engine_pb2.CheckInput, _Mapping]]] = ..., outputs: _Optional[_Iterable[_Union[_engine_pb2.CheckOutput, _Mapping]]] = ..., error: _Optional[str] = ...) -> None: ...
    class PlanResources(_message.Message):
        __slots__ = ("input", "output", "error")
        INPUT_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        input: _engine_pb2.PlanResourcesInput
        output: _engine_pb2.PlanResourcesOutput
        error: str
        def __init__(self, input: _Optional[_Union[_engine_pb2.PlanResourcesInput, _Mapping]] = ..., output: _Optional[_Union[_engine_pb2.PlanResourcesOutput, _Mapping]] = ..., error: _Optional[str] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
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
    AUDIT_TRAIL_FIELD_NUMBER: _ClassVar[int]
    OVERSIZED_FIELD_NUMBER: _ClassVar[int]
    POLICY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    call_id: str
    timestamp: _timestamp_pb2.Timestamp
    peer: Peer
    inputs: _containers.RepeatedCompositeFieldContainer[_engine_pb2.CheckInput]
    outputs: _containers.RepeatedCompositeFieldContainer[_engine_pb2.CheckOutput]
    error: str
    check_resources: DecisionLogEntry.CheckResources
    plan_resources: DecisionLogEntry.PlanResources
    metadata: _containers.MessageMap[str, MetaValues]
    audit_trail: AuditTrail
    oversized: bool
    policy_source: PolicySource
    request_context: RequestContext
    def __init__(self, call_id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., peer: _Optional[_Union[Peer, _Mapping]] = ..., inputs: _Optional[_Iterable[_Union[_engine_pb2.CheckInput, _Mapping]]] = ..., outputs: _Optional[_Iterable[_Union[_engine_pb2.CheckOutput, _Mapping]]] = ..., error: _Optional[str] = ..., check_resources: _Optional[_Union[DecisionLogEntry.CheckResources, _Mapping]] = ..., plan_resources: _Optional[_Union[DecisionLogEntry.PlanResources, _Mapping]] = ..., metadata: _Optional[_Mapping[str, MetaValues]] = ..., audit_trail: _Optional[_Union[AuditTrail, _Mapping]] = ..., oversized: _Optional[bool] = ..., policy_source: _Optional[_Union[PolicySource, _Mapping]] = ..., request_context: _Optional[_Union[RequestContext, _Mapping]] = ...) -> None: ...

class MetaValues(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...

class Peer(_message.Message):
    __slots__ = ("address", "auth_info", "user_agent", "forwarded_for")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AUTH_INFO_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    FORWARDED_FOR_FIELD_NUMBER: _ClassVar[int]
    address: str
    auth_info: str
    user_agent: str
    forwarded_for: str
    def __init__(self, address: _Optional[str] = ..., auth_info: _Optional[str] = ..., user_agent: _Optional[str] = ..., forwarded_for: _Optional[str] = ...) -> None: ...

class AuditTrail(_message.Message):
    __slots__ = ("effective_policies",)
    class EffectivePoliciesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _policy_pb2.SourceAttributes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_policy_pb2.SourceAttributes, _Mapping]] = ...) -> None: ...
    EFFECTIVE_POLICIES_FIELD_NUMBER: _ClassVar[int]
    effective_policies: _containers.MessageMap[str, _policy_pb2.SourceAttributes]
    def __init__(self, effective_policies: _Optional[_Mapping[str, _policy_pb2.SourceAttributes]] = ...) -> None: ...

class PolicySource(_message.Message):
    __slots__ = ("blob", "database", "disk", "git", "hub", "embedded_pdp")
    class Blob(_message.Message):
        __slots__ = ("bucket_url", "prefix")
        BUCKET_URL_FIELD_NUMBER: _ClassVar[int]
        PREFIX_FIELD_NUMBER: _ClassVar[int]
        bucket_url: str
        prefix: str
        def __init__(self, bucket_url: _Optional[str] = ..., prefix: _Optional[str] = ...) -> None: ...
    class Database(_message.Message):
        __slots__ = ("driver",)
        class Driver(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DRIVER_UNSPECIFIED: _ClassVar[PolicySource.Database.Driver]
            DRIVER_MYSQL: _ClassVar[PolicySource.Database.Driver]
            DRIVER_POSTGRES: _ClassVar[PolicySource.Database.Driver]
            DRIVER_SQLITE3: _ClassVar[PolicySource.Database.Driver]
        DRIVER_UNSPECIFIED: PolicySource.Database.Driver
        DRIVER_MYSQL: PolicySource.Database.Driver
        DRIVER_POSTGRES: PolicySource.Database.Driver
        DRIVER_SQLITE3: PolicySource.Database.Driver
        DRIVER_FIELD_NUMBER: _ClassVar[int]
        driver: PolicySource.Database.Driver
        def __init__(self, driver: _Optional[_Union[PolicySource.Database.Driver, str]] = ...) -> None: ...
    class Disk(_message.Message):
        __slots__ = ("directory",)
        DIRECTORY_FIELD_NUMBER: _ClassVar[int]
        directory: str
        def __init__(self, directory: _Optional[str] = ...) -> None: ...
    class EmbeddedPDP(_message.Message):
        __slots__ = ("url", "commit_hash", "built_at")
        URL_FIELD_NUMBER: _ClassVar[int]
        COMMIT_HASH_FIELD_NUMBER: _ClassVar[int]
        BUILT_AT_FIELD_NUMBER: _ClassVar[int]
        url: str
        commit_hash: str
        built_at: _timestamp_pb2.Timestamp
        def __init__(self, url: _Optional[str] = ..., commit_hash: _Optional[str] = ..., built_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Git(_message.Message):
        __slots__ = ("repository_url", "branch", "subdirectory", "hash")
        REPOSITORY_URL_FIELD_NUMBER: _ClassVar[int]
        BRANCH_FIELD_NUMBER: _ClassVar[int]
        SUBDIRECTORY_FIELD_NUMBER: _ClassVar[int]
        HASH_FIELD_NUMBER: _ClassVar[int]
        repository_url: str
        branch: str
        subdirectory: str
        hash: str
        def __init__(self, repository_url: _Optional[str] = ..., branch: _Optional[str] = ..., subdirectory: _Optional[str] = ..., hash: _Optional[str] = ...) -> None: ...
    class Hub(_message.Message):
        __slots__ = ("label", "deployment_id", "playground_id", "local_bundle", "embedded_bundle", "remote_bundle")
        class EmbeddedBundle(_message.Message):
            __slots__ = ("rule_id", "scopes", "bundle_id")
            RULE_ID_FIELD_NUMBER: _ClassVar[int]
            SCOPES_FIELD_NUMBER: _ClassVar[int]
            BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
            rule_id: str
            scopes: _containers.RepeatedScalarFieldContainer[str]
            bundle_id: str
            def __init__(self, rule_id: _Optional[str] = ..., scopes: _Optional[_Iterable[str]] = ..., bundle_id: _Optional[str] = ...) -> None: ...
        class LocalBundle(_message.Message):
            __slots__ = ("path", "bundle_id")
            PATH_FIELD_NUMBER: _ClassVar[int]
            BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
            path: str
            bundle_id: str
            def __init__(self, path: _Optional[str] = ..., bundle_id: _Optional[str] = ...) -> None: ...
        class RemoteBundle(_message.Message):
            __slots__ = ("deployment_id", "bundle_id")
            DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
            BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
            deployment_id: str
            bundle_id: str
            def __init__(self, deployment_id: _Optional[str] = ..., bundle_id: _Optional[str] = ...) -> None: ...
        LABEL_FIELD_NUMBER: _ClassVar[int]
        DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
        PLAYGROUND_ID_FIELD_NUMBER: _ClassVar[int]
        LOCAL_BUNDLE_FIELD_NUMBER: _ClassVar[int]
        EMBEDDED_BUNDLE_FIELD_NUMBER: _ClassVar[int]
        REMOTE_BUNDLE_FIELD_NUMBER: _ClassVar[int]
        label: str
        deployment_id: str
        playground_id: str
        local_bundle: PolicySource.Hub.LocalBundle
        embedded_bundle: PolicySource.Hub.EmbeddedBundle
        remote_bundle: PolicySource.Hub.RemoteBundle
        def __init__(self, label: _Optional[str] = ..., deployment_id: _Optional[str] = ..., playground_id: _Optional[str] = ..., local_bundle: _Optional[_Union[PolicySource.Hub.LocalBundle, _Mapping]] = ..., embedded_bundle: _Optional[_Union[PolicySource.Hub.EmbeddedBundle, _Mapping]] = ..., remote_bundle: _Optional[_Union[PolicySource.Hub.RemoteBundle, _Mapping]] = ...) -> None: ...
    BLOB_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    DISK_FIELD_NUMBER: _ClassVar[int]
    GIT_FIELD_NUMBER: _ClassVar[int]
    HUB_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_PDP_FIELD_NUMBER: _ClassVar[int]
    blob: PolicySource.Blob
    database: PolicySource.Database
    disk: PolicySource.Disk
    git: PolicySource.Git
    hub: PolicySource.Hub
    embedded_pdp: PolicySource.EmbeddedPDP
    def __init__(self, blob: _Optional[_Union[PolicySource.Blob, _Mapping]] = ..., database: _Optional[_Union[PolicySource.Database, _Mapping]] = ..., disk: _Optional[_Union[PolicySource.Disk, _Mapping]] = ..., git: _Optional[_Union[PolicySource.Git, _Mapping]] = ..., hub: _Optional[_Union[PolicySource.Hub, _Mapping]] = ..., embedded_pdp: _Optional[_Union[PolicySource.EmbeddedPDP, _Mapping]] = ...) -> None: ...

class RequestContext(_message.Message):
    __slots__ = ("annotations",)
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    annotations: _containers.MessageMap[str, _struct_pb2.Value]
    def __init__(self, annotations: _Optional[_Mapping[str, _struct_pb2.Value]] = ...) -> None: ...
