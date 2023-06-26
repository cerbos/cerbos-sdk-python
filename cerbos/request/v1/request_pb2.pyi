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

class AddOrUpdatePolicyRequest(_message.Message):
    __slots__ = ["policies"]
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    policies: _containers.RepeatedCompositeFieldContainer[_policy_pb2.Policy]
    def __init__(self, policies: _Optional[_Iterable[_Union[_policy_pb2.Policy, _Mapping]]] = ...) -> None: ...

class AddOrUpdateSchemaRequest(_message.Message):
    __slots__ = ["schemas"]
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    schemas: _containers.RepeatedCompositeFieldContainer[_schema_pb2.Schema]
    def __init__(self, schemas: _Optional[_Iterable[_Union[_schema_pb2.Schema, _Mapping]]] = ...) -> None: ...

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

class AuxData(_message.Message):
    __slots__ = ["jwt"]
    class JWT(_message.Message):
        __slots__ = ["key_set_id", "token"]
        KEY_SET_ID_FIELD_NUMBER: _ClassVar[int]
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        key_set_id: str
        token: str
        def __init__(self, token: _Optional[str] = ..., key_set_id: _Optional[str] = ...) -> None: ...
    JWT_FIELD_NUMBER: _ClassVar[int]
    jwt: AuxData.JWT
    def __init__(self, jwt: _Optional[_Union[AuxData.JWT, _Mapping]] = ...) -> None: ...

class CheckResourceBatchRequest(_message.Message):
    __slots__ = ["aux_data", "principal", "request_id", "resources"]
    class BatchEntry(_message.Message):
        __slots__ = ["actions", "resource"]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_FIELD_NUMBER: _ClassVar[int]
        actions: _containers.RepeatedScalarFieldContainer[str]
        resource: _engine_pb2.Resource
        def __init__(self, actions: _Optional[_Iterable[str]] = ..., resource: _Optional[_Union[_engine_pb2.Resource, _Mapping]] = ...) -> None: ...
    AUX_DATA_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    aux_data: AuxData
    principal: _engine_pb2.Principal
    request_id: str
    resources: _containers.RepeatedCompositeFieldContainer[CheckResourceBatchRequest.BatchEntry]
    def __init__(self, request_id: _Optional[str] = ..., principal: _Optional[_Union[_engine_pb2.Principal, _Mapping]] = ..., resources: _Optional[_Iterable[_Union[CheckResourceBatchRequest.BatchEntry, _Mapping]]] = ..., aux_data: _Optional[_Union[AuxData, _Mapping]] = ...) -> None: ...

class CheckResourceSetRequest(_message.Message):
    __slots__ = ["actions", "aux_data", "include_meta", "principal", "request_id", "resource"]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    AUX_DATA_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_META_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedScalarFieldContainer[str]
    aux_data: AuxData
    include_meta: bool
    principal: _engine_pb2.Principal
    request_id: str
    resource: ResourceSet
    def __init__(self, request_id: _Optional[str] = ..., actions: _Optional[_Iterable[str]] = ..., principal: _Optional[_Union[_engine_pb2.Principal, _Mapping]] = ..., resource: _Optional[_Union[ResourceSet, _Mapping]] = ..., include_meta: bool = ..., aux_data: _Optional[_Union[AuxData, _Mapping]] = ...) -> None: ...

class CheckResourcesRequest(_message.Message):
    __slots__ = ["aux_data", "include_meta", "principal", "request_id", "resources"]
    class ResourceEntry(_message.Message):
        __slots__ = ["actions", "resource"]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_FIELD_NUMBER: _ClassVar[int]
        actions: _containers.RepeatedScalarFieldContainer[str]
        resource: _engine_pb2.Resource
        def __init__(self, actions: _Optional[_Iterable[str]] = ..., resource: _Optional[_Union[_engine_pb2.Resource, _Mapping]] = ...) -> None: ...
    AUX_DATA_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_META_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    aux_data: AuxData
    include_meta: bool
    principal: _engine_pb2.Principal
    request_id: str
    resources: _containers.RepeatedCompositeFieldContainer[CheckResourcesRequest.ResourceEntry]
    def __init__(self, request_id: _Optional[str] = ..., include_meta: bool = ..., principal: _Optional[_Union[_engine_pb2.Principal, _Mapping]] = ..., resources: _Optional[_Iterable[_Union[CheckResourcesRequest.ResourceEntry, _Mapping]]] = ..., aux_data: _Optional[_Union[AuxData, _Mapping]] = ...) -> None: ...

class DeleteSchemaRequest(_message.Message):
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

class File(_message.Message):
    __slots__ = ["contents", "file_name"]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    contents: bytes
    file_name: str
    def __init__(self, file_name: _Optional[str] = ..., contents: _Optional[bytes] = ...) -> None: ...

class GetPolicyRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[_Iterable[str]] = ...) -> None: ...

class GetSchemaRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[_Iterable[str]] = ...) -> None: ...

class ListAuditLogEntriesRequest(_message.Message):
    __slots__ = ["between", "kind", "lookup", "since", "tail"]
    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class TimeRange(_message.Message):
        __slots__ = ["end", "start"]
        END_FIELD_NUMBER: _ClassVar[int]
        START_FIELD_NUMBER: _ClassVar[int]
        end: _timestamp_pb2.Timestamp
        start: _timestamp_pb2.Timestamp
        def __init__(self, start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    BETWEEN_FIELD_NUMBER: _ClassVar[int]
    KIND_ACCESS: ListAuditLogEntriesRequest.Kind
    KIND_DECISION: ListAuditLogEntriesRequest.Kind
    KIND_FIELD_NUMBER: _ClassVar[int]
    KIND_UNSPECIFIED: ListAuditLogEntriesRequest.Kind
    LOOKUP_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    TAIL_FIELD_NUMBER: _ClassVar[int]
    between: ListAuditLogEntriesRequest.TimeRange
    kind: ListAuditLogEntriesRequest.Kind
    lookup: str
    since: _duration_pb2.Duration
    tail: int
    def __init__(self, kind: _Optional[_Union[ListAuditLogEntriesRequest.Kind, str]] = ..., tail: _Optional[int] = ..., between: _Optional[_Union[ListAuditLogEntriesRequest.TimeRange, _Mapping]] = ..., since: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., lookup: _Optional[str] = ...) -> None: ...

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

class ListSchemasRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PlanResourcesRequest(_message.Message):
    __slots__ = ["action", "aux_data", "include_meta", "principal", "request_id", "resource"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    AUX_DATA_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_META_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    action: str
    aux_data: AuxData
    include_meta: bool
    principal: _engine_pb2.Principal
    request_id: str
    resource: _engine_pb2.PlanResourcesInput.Resource
    def __init__(self, request_id: _Optional[str] = ..., action: _Optional[str] = ..., principal: _Optional[_Union[_engine_pb2.Principal, _Mapping]] = ..., resource: _Optional[_Union[_engine_pb2.PlanResourcesInput.Resource, _Mapping]] = ..., aux_data: _Optional[_Union[AuxData, _Mapping]] = ..., include_meta: bool = ...) -> None: ...

class PlaygroundEvaluateRequest(_message.Message):
    __slots__ = ["actions", "aux_data", "files", "playground_id", "principal", "resource"]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    AUX_DATA_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    PLAYGROUND_ID_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedScalarFieldContainer[str]
    aux_data: AuxData
    files: _containers.RepeatedCompositeFieldContainer[File]
    playground_id: str
    principal: _engine_pb2.Principal
    resource: _engine_pb2.Resource
    def __init__(self, playground_id: _Optional[str] = ..., files: _Optional[_Iterable[_Union[File, _Mapping]]] = ..., principal: _Optional[_Union[_engine_pb2.Principal, _Mapping]] = ..., resource: _Optional[_Union[_engine_pb2.Resource, _Mapping]] = ..., actions: _Optional[_Iterable[str]] = ..., aux_data: _Optional[_Union[AuxData, _Mapping]] = ...) -> None: ...

class PlaygroundProxyRequest(_message.Message):
    __slots__ = ["check_resource_batch", "check_resource_set", "check_resources", "files", "plan_resources", "playground_id"]
    CHECK_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    CHECK_RESOURCE_BATCH_FIELD_NUMBER: _ClassVar[int]
    CHECK_RESOURCE_SET_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    PLAN_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    PLAYGROUND_ID_FIELD_NUMBER: _ClassVar[int]
    check_resource_batch: CheckResourceBatchRequest
    check_resource_set: CheckResourceSetRequest
    check_resources: CheckResourcesRequest
    files: _containers.RepeatedCompositeFieldContainer[File]
    plan_resources: PlanResourcesRequest
    playground_id: str
    def __init__(self, playground_id: _Optional[str] = ..., files: _Optional[_Iterable[_Union[File, _Mapping]]] = ..., check_resource_set: _Optional[_Union[CheckResourceSetRequest, _Mapping]] = ..., check_resource_batch: _Optional[_Union[CheckResourceBatchRequest, _Mapping]] = ..., plan_resources: _Optional[_Union[PlanResourcesRequest, _Mapping]] = ..., check_resources: _Optional[_Union[CheckResourcesRequest, _Mapping]] = ...) -> None: ...

class PlaygroundTestRequest(_message.Message):
    __slots__ = ["files", "playground_id"]
    FILES_FIELD_NUMBER: _ClassVar[int]
    PLAYGROUND_ID_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[File]
    playground_id: str
    def __init__(self, playground_id: _Optional[str] = ..., files: _Optional[_Iterable[_Union[File, _Mapping]]] = ...) -> None: ...

class PlaygroundValidateRequest(_message.Message):
    __slots__ = ["files", "playground_id"]
    FILES_FIELD_NUMBER: _ClassVar[int]
    PLAYGROUND_ID_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[File]
    playground_id: str
    def __init__(self, playground_id: _Optional[str] = ..., files: _Optional[_Iterable[_Union[File, _Mapping]]] = ...) -> None: ...

class ReloadStoreRequest(_message.Message):
    __slots__ = ["wait"]
    WAIT_FIELD_NUMBER: _ClassVar[int]
    wait: bool
    def __init__(self, wait: bool = ...) -> None: ...

class ResourceSet(_message.Message):
    __slots__ = ["instances", "kind", "policy_version", "scope"]
    class InstancesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AttributesMap
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AttributesMap, _Mapping]] = ...) -> None: ...
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.MessageMap[str, AttributesMap]
    kind: str
    policy_version: str
    scope: str
    def __init__(self, kind: _Optional[str] = ..., policy_version: _Optional[str] = ..., instances: _Optional[_Mapping[str, AttributesMap]] = ..., scope: _Optional[str] = ...) -> None: ...

class ServerInfoRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
