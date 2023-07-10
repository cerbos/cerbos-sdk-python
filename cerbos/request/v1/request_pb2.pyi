from cerbos.engine.v1 import engine_pb2 as _engine_pb2
from cerbos.policy.v1 import policy_pb2 as _policy_pb2
from cerbos.schema.v1 import schema_pb2 as _schema_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlanResourcesRequest(_message.Message):
    __slots__ = ["request_id", "action", "principal", "resource", "aux_data", "include_meta"]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    AUX_DATA_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_META_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    action: str
    principal: _engine_pb2.Principal
    resource: _engine_pb2.PlanResourcesInput.Resource
    aux_data: AuxData
    include_meta: bool
    def __init__(self, request_id: _Optional[str] = ..., action: _Optional[str] = ..., principal: _Optional[_Union[_engine_pb2.Principal, _Mapping]] = ..., resource: _Optional[_Union[_engine_pb2.PlanResourcesInput.Resource, _Mapping]] = ..., aux_data: _Optional[_Union[AuxData, _Mapping]] = ..., include_meta: bool = ...) -> None: ...

class CheckResourceSetRequest(_message.Message):
    __slots__ = ["request_id", "actions", "principal", "resource", "include_meta", "aux_data"]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_META_FIELD_NUMBER: _ClassVar[int]
    AUX_DATA_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    actions: _containers.RepeatedScalarFieldContainer[str]
    principal: _engine_pb2.Principal
    resource: ResourceSet
    include_meta: bool
    aux_data: AuxData
    def __init__(self, request_id: _Optional[str] = ..., actions: _Optional[_Iterable[str]] = ..., principal: _Optional[_Union[_engine_pb2.Principal, _Mapping]] = ..., resource: _Optional[_Union[ResourceSet, _Mapping]] = ..., include_meta: bool = ..., aux_data: _Optional[_Union[AuxData, _Mapping]] = ...) -> None: ...

class ResourceSet(_message.Message):
    __slots__ = ["kind", "policy_version", "instances", "scope"]
    class InstancesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AttributesMap
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AttributesMap, _Mapping]] = ...) -> None: ...
    KIND_FIELD_NUMBER: _ClassVar[int]
    POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    kind: str
    policy_version: str
    instances: _containers.MessageMap[str, AttributesMap]
    scope: str
    def __init__(self, kind: _Optional[str] = ..., policy_version: _Optional[str] = ..., instances: _Optional[_Mapping[str, AttributesMap]] = ..., scope: _Optional[str] = ...) -> None: ...

class AttributesMap(_message.Message):
    __slots__ = ["attr"]
    class AttrEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    ATTR_FIELD_NUMBER: _ClassVar[int]
    attr: _containers.MessageMap[str, _struct_pb2.Value]
    def __init__(self, attr: _Optional[_Mapping[str, _struct_pb2.Value]] = ...) -> None: ...

class CheckResourceBatchRequest(_message.Message):
    __slots__ = ["request_id", "principal", "resources", "aux_data"]
    class BatchEntry(_message.Message):
        __slots__ = ["actions", "resource"]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_FIELD_NUMBER: _ClassVar[int]
        actions: _containers.RepeatedScalarFieldContainer[str]
        resource: _engine_pb2.Resource
        def __init__(self, actions: _Optional[_Iterable[str]] = ..., resource: _Optional[_Union[_engine_pb2.Resource, _Mapping]] = ...) -> None: ...
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    AUX_DATA_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    principal: _engine_pb2.Principal
    resources: _containers.RepeatedCompositeFieldContainer[CheckResourceBatchRequest.BatchEntry]
    aux_data: AuxData
    def __init__(self, request_id: _Optional[str] = ..., principal: _Optional[_Union[_engine_pb2.Principal, _Mapping]] = ..., resources: _Optional[_Iterable[_Union[CheckResourceBatchRequest.BatchEntry, _Mapping]]] = ..., aux_data: _Optional[_Union[AuxData, _Mapping]] = ...) -> None: ...

class CheckResourcesRequest(_message.Message):
    __slots__ = ["request_id", "include_meta", "principal", "resources", "aux_data"]
    class ResourceEntry(_message.Message):
        __slots__ = ["actions", "resource"]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_FIELD_NUMBER: _ClassVar[int]
        actions: _containers.RepeatedScalarFieldContainer[str]
        resource: _engine_pb2.Resource
        def __init__(self, actions: _Optional[_Iterable[str]] = ..., resource: _Optional[_Union[_engine_pb2.Resource, _Mapping]] = ...) -> None: ...
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_META_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    AUX_DATA_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    include_meta: bool
    principal: _engine_pb2.Principal
    resources: _containers.RepeatedCompositeFieldContainer[CheckResourcesRequest.ResourceEntry]
    aux_data: AuxData
    def __init__(self, request_id: _Optional[str] = ..., include_meta: bool = ..., principal: _Optional[_Union[_engine_pb2.Principal, _Mapping]] = ..., resources: _Optional[_Iterable[_Union[CheckResourcesRequest.ResourceEntry, _Mapping]]] = ..., aux_data: _Optional[_Union[AuxData, _Mapping]] = ...) -> None: ...

class AuxData(_message.Message):
    __slots__ = ["jwt"]
    class JWT(_message.Message):
        __slots__ = ["token", "key_set_id"]
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        KEY_SET_ID_FIELD_NUMBER: _ClassVar[int]
        token: str
        key_set_id: str
        def __init__(self, token: _Optional[str] = ..., key_set_id: _Optional[str] = ...) -> None: ...
    JWT_FIELD_NUMBER: _ClassVar[int]
    jwt: AuxData.JWT
    def __init__(self, jwt: _Optional[_Union[AuxData.JWT, _Mapping]] = ...) -> None: ...

class File(_message.Message):
    __slots__ = ["file_name", "contents"]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    contents: bytes
    def __init__(self, file_name: _Optional[str] = ..., contents: _Optional[bytes] = ...) -> None: ...

class PlaygroundValidateRequest(_message.Message):
    __slots__ = ["playground_id", "files"]
    PLAYGROUND_ID_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    playground_id: str
    files: _containers.RepeatedCompositeFieldContainer[File]
    def __init__(self, playground_id: _Optional[str] = ..., files: _Optional[_Iterable[_Union[File, _Mapping]]] = ...) -> None: ...

class PlaygroundTestRequest(_message.Message):
    __slots__ = ["playground_id", "files"]
    PLAYGROUND_ID_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    playground_id: str
    files: _containers.RepeatedCompositeFieldContainer[File]
    def __init__(self, playground_id: _Optional[str] = ..., files: _Optional[_Iterable[_Union[File, _Mapping]]] = ...) -> None: ...

class PlaygroundEvaluateRequest(_message.Message):
    __slots__ = ["playground_id", "files", "principal", "resource", "actions", "aux_data"]
    PLAYGROUND_ID_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    AUX_DATA_FIELD_NUMBER: _ClassVar[int]
    playground_id: str
    files: _containers.RepeatedCompositeFieldContainer[File]
    principal: _engine_pb2.Principal
    resource: _engine_pb2.Resource
    actions: _containers.RepeatedScalarFieldContainer[str]
    aux_data: AuxData
    def __init__(self, playground_id: _Optional[str] = ..., files: _Optional[_Iterable[_Union[File, _Mapping]]] = ..., principal: _Optional[_Union[_engine_pb2.Principal, _Mapping]] = ..., resource: _Optional[_Union[_engine_pb2.Resource, _Mapping]] = ..., actions: _Optional[_Iterable[str]] = ..., aux_data: _Optional[_Union[AuxData, _Mapping]] = ...) -> None: ...

class PlaygroundProxyRequest(_message.Message):
    __slots__ = ["playground_id", "files", "check_resource_set", "check_resource_batch", "plan_resources", "check_resources"]
    PLAYGROUND_ID_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    CHECK_RESOURCE_SET_FIELD_NUMBER: _ClassVar[int]
    CHECK_RESOURCE_BATCH_FIELD_NUMBER: _ClassVar[int]
    PLAN_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    CHECK_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    playground_id: str
    files: _containers.RepeatedCompositeFieldContainer[File]
    check_resource_set: CheckResourceSetRequest
    check_resource_batch: CheckResourceBatchRequest
    plan_resources: PlanResourcesRequest
    check_resources: CheckResourcesRequest
    def __init__(self, playground_id: _Optional[str] = ..., files: _Optional[_Iterable[_Union[File, _Mapping]]] = ..., check_resource_set: _Optional[_Union[CheckResourceSetRequest, _Mapping]] = ..., check_resource_batch: _Optional[_Union[CheckResourceBatchRequest, _Mapping]] = ..., plan_resources: _Optional[_Union[PlanResourcesRequest, _Mapping]] = ..., check_resources: _Optional[_Union[CheckResourcesRequest, _Mapping]] = ...) -> None: ...

class AddOrUpdatePolicyRequest(_message.Message):
    __slots__ = ["policies"]
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    policies: _containers.RepeatedCompositeFieldContainer[_policy_pb2.Policy]
    def __init__(self, policies: _Optional[_Iterable[_Union[_policy_pb2.Policy, _Mapping]]] = ...) -> None: ...

class ListAuditLogEntriesRequest(_message.Message):
    __slots__ = ["kind", "tail", "between", "since", "lookup"]
    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        KIND_UNSPECIFIED: _ClassVar[ListAuditLogEntriesRequest.Kind]
        KIND_ACCESS: _ClassVar[ListAuditLogEntriesRequest.Kind]
        KIND_DECISION: _ClassVar[ListAuditLogEntriesRequest.Kind]
    KIND_UNSPECIFIED: ListAuditLogEntriesRequest.Kind
    KIND_ACCESS: ListAuditLogEntriesRequest.Kind
    KIND_DECISION: ListAuditLogEntriesRequest.Kind
    class TimeRange(_message.Message):
        __slots__ = ["start", "end"]
        START_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        start: _timestamp_pb2.Timestamp
        end: _timestamp_pb2.Timestamp
        def __init__(self, start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    KIND_FIELD_NUMBER: _ClassVar[int]
    TAIL_FIELD_NUMBER: _ClassVar[int]
    BETWEEN_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_FIELD_NUMBER: _ClassVar[int]
    kind: ListAuditLogEntriesRequest.Kind
    tail: int
    between: ListAuditLogEntriesRequest.TimeRange
    since: _duration_pb2.Duration
    lookup: str
    def __init__(self, kind: _Optional[_Union[ListAuditLogEntriesRequest.Kind, str]] = ..., tail: _Optional[int] = ..., between: _Optional[_Union[ListAuditLogEntriesRequest.TimeRange, _Mapping]] = ..., since: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., lookup: _Optional[str] = ...) -> None: ...

class ServerInfoRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListPoliciesRequest(_message.Message):
    __slots__ = ["include_disabled", "name_regexp", "scope_regexp", "version_regexp"]
    INCLUDE_DISABLED_FIELD_NUMBER: _ClassVar[int]
    NAME_REGEXP_FIELD_NUMBER: _ClassVar[int]
    SCOPE_REGEXP_FIELD_NUMBER: _ClassVar[int]
    VERSION_REGEXP_FIELD_NUMBER: _ClassVar[int]
    include_disabled: bool
    name_regexp: str
    scope_regexp: str
    version_regexp: str
    def __init__(self, include_disabled: bool = ..., name_regexp: _Optional[str] = ..., scope_regexp: _Optional[str] = ..., version_regexp: _Optional[str] = ...) -> None: ...

class GetPolicyRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[_Iterable[str]] = ...) -> None: ...

class DisablePolicyRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[_Iterable[str]] = ...) -> None: ...

class EnablePolicyRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[_Iterable[str]] = ...) -> None: ...

class AddOrUpdateSchemaRequest(_message.Message):
    __slots__ = ["schemas"]
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    schemas: _containers.RepeatedCompositeFieldContainer[_schema_pb2.Schema]
    def __init__(self, schemas: _Optional[_Iterable[_Union[_schema_pb2.Schema, _Mapping]]] = ...) -> None: ...

class ListSchemasRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetSchemaRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteSchemaRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[_Iterable[str]] = ...) -> None: ...

class ReloadStoreRequest(_message.Message):
    __slots__ = ["wait"]
    WAIT_FIELD_NUMBER: _ClassVar[int]
    wait: bool
    def __init__(self, wait: bool = ...) -> None: ...
