from cerbos.audit.v1 import audit_pb2 as _audit_pb2
from cerbos.effect.v1 import effect_pb2 as _effect_pb2
from cerbos.engine.v1 import engine_pb2 as _engine_pb2
from cerbos.policy.v1 import policy_pb2 as _policy_pb2
from cerbos.schema.v1 import schema_pb2 as _schema_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlanResourcesResponse(_message.Message):
    __slots__ = ["request_id", "action", "resource_kind", "policy_version", "filter", "meta", "validation_errors"]
    class Meta(_message.Message):
        __slots__ = ["filter_debug", "matched_scope"]
        FILTER_DEBUG_FIELD_NUMBER: _ClassVar[int]
        MATCHED_SCOPE_FIELD_NUMBER: _ClassVar[int]
        filter_debug: str
        matched_scope: str
        def __init__(self, filter_debug: _Optional[str] = ..., matched_scope: _Optional[str] = ...) -> None: ...
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_KIND_FIELD_NUMBER: _ClassVar[int]
    POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    action: str
    resource_kind: str
    policy_version: str
    filter: _engine_pb2.PlanResourcesFilter
    meta: PlanResourcesResponse.Meta
    validation_errors: _containers.RepeatedCompositeFieldContainer[_schema_pb2.ValidationError]
    def __init__(self, request_id: _Optional[str] = ..., action: _Optional[str] = ..., resource_kind: _Optional[str] = ..., policy_version: _Optional[str] = ..., filter: _Optional[_Union[_engine_pb2.PlanResourcesFilter, _Mapping]] = ..., meta: _Optional[_Union[PlanResourcesResponse.Meta, _Mapping]] = ..., validation_errors: _Optional[_Iterable[_Union[_schema_pb2.ValidationError, _Mapping]]] = ...) -> None: ...

class CheckResourceSetResponse(_message.Message):
    __slots__ = ["request_id", "resource_instances", "meta"]
    class ActionEffectMap(_message.Message):
        __slots__ = ["actions", "validation_errors"]
        class ActionsEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _effect_pb2.Effect
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_effect_pb2.Effect, str]] = ...) -> None: ...
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        VALIDATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
        actions: _containers.ScalarMap[str, _effect_pb2.Effect]
        validation_errors: _containers.RepeatedCompositeFieldContainer[_schema_pb2.ValidationError]
        def __init__(self, actions: _Optional[_Mapping[str, _effect_pb2.Effect]] = ..., validation_errors: _Optional[_Iterable[_Union[_schema_pb2.ValidationError, _Mapping]]] = ...) -> None: ...
    class Meta(_message.Message):
        __slots__ = ["resource_instances"]
        class EffectMeta(_message.Message):
            __slots__ = ["matched_policy", "matched_scope"]
            MATCHED_POLICY_FIELD_NUMBER: _ClassVar[int]
            MATCHED_SCOPE_FIELD_NUMBER: _ClassVar[int]
            matched_policy: str
            matched_scope: str
            def __init__(self, matched_policy: _Optional[str] = ..., matched_scope: _Optional[str] = ...) -> None: ...
        class ActionMeta(_message.Message):
            __slots__ = ["actions", "effective_derived_roles"]
            class ActionsEntry(_message.Message):
                __slots__ = ["key", "value"]
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: CheckResourceSetResponse.Meta.EffectMeta
                def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CheckResourceSetResponse.Meta.EffectMeta, _Mapping]] = ...) -> None: ...
            ACTIONS_FIELD_NUMBER: _ClassVar[int]
            EFFECTIVE_DERIVED_ROLES_FIELD_NUMBER: _ClassVar[int]
            actions: _containers.MessageMap[str, CheckResourceSetResponse.Meta.EffectMeta]
            effective_derived_roles: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, actions: _Optional[_Mapping[str, CheckResourceSetResponse.Meta.EffectMeta]] = ..., effective_derived_roles: _Optional[_Iterable[str]] = ...) -> None: ...
        class ResourceInstancesEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: CheckResourceSetResponse.Meta.ActionMeta
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CheckResourceSetResponse.Meta.ActionMeta, _Mapping]] = ...) -> None: ...
        RESOURCE_INSTANCES_FIELD_NUMBER: _ClassVar[int]
        resource_instances: _containers.MessageMap[str, CheckResourceSetResponse.Meta.ActionMeta]
        def __init__(self, resource_instances: _Optional[_Mapping[str, CheckResourceSetResponse.Meta.ActionMeta]] = ...) -> None: ...
    class ResourceInstancesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CheckResourceSetResponse.ActionEffectMap
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CheckResourceSetResponse.ActionEffectMap, _Mapping]] = ...) -> None: ...
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    resource_instances: _containers.MessageMap[str, CheckResourceSetResponse.ActionEffectMap]
    meta: CheckResourceSetResponse.Meta
    def __init__(self, request_id: _Optional[str] = ..., resource_instances: _Optional[_Mapping[str, CheckResourceSetResponse.ActionEffectMap]] = ..., meta: _Optional[_Union[CheckResourceSetResponse.Meta, _Mapping]] = ...) -> None: ...

class CheckResourceBatchResponse(_message.Message):
    __slots__ = ["request_id", "results"]
    class ActionEffectMap(_message.Message):
        __slots__ = ["resource_id", "actions", "validation_errors"]
        class ActionsEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _effect_pb2.Effect
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_effect_pb2.Effect, str]] = ...) -> None: ...
        RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        VALIDATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
        resource_id: str
        actions: _containers.ScalarMap[str, _effect_pb2.Effect]
        validation_errors: _containers.RepeatedCompositeFieldContainer[_schema_pb2.ValidationError]
        def __init__(self, resource_id: _Optional[str] = ..., actions: _Optional[_Mapping[str, _effect_pb2.Effect]] = ..., validation_errors: _Optional[_Iterable[_Union[_schema_pb2.ValidationError, _Mapping]]] = ...) -> None: ...
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    results: _containers.RepeatedCompositeFieldContainer[CheckResourceBatchResponse.ActionEffectMap]
    def __init__(self, request_id: _Optional[str] = ..., results: _Optional[_Iterable[_Union[CheckResourceBatchResponse.ActionEffectMap, _Mapping]]] = ...) -> None: ...

class CheckResourcesResponse(_message.Message):
    __slots__ = ["request_id", "results"]
    class ResultEntry(_message.Message):
        __slots__ = ["resource", "actions", "validation_errors", "meta", "outputs"]
        class Resource(_message.Message):
            __slots__ = ["id", "kind", "policy_version", "scope"]
            ID_FIELD_NUMBER: _ClassVar[int]
            KIND_FIELD_NUMBER: _ClassVar[int]
            POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
            SCOPE_FIELD_NUMBER: _ClassVar[int]
            id: str
            kind: str
            policy_version: str
            scope: str
            def __init__(self, id: _Optional[str] = ..., kind: _Optional[str] = ..., policy_version: _Optional[str] = ..., scope: _Optional[str] = ...) -> None: ...
        class Meta(_message.Message):
            __slots__ = ["actions", "effective_derived_roles"]
            class EffectMeta(_message.Message):
                __slots__ = ["matched_policy", "matched_scope"]
                MATCHED_POLICY_FIELD_NUMBER: _ClassVar[int]
                MATCHED_SCOPE_FIELD_NUMBER: _ClassVar[int]
                matched_policy: str
                matched_scope: str
                def __init__(self, matched_policy: _Optional[str] = ..., matched_scope: _Optional[str] = ...) -> None: ...
            class ActionsEntry(_message.Message):
                __slots__ = ["key", "value"]
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: CheckResourcesResponse.ResultEntry.Meta.EffectMeta
                def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CheckResourcesResponse.ResultEntry.Meta.EffectMeta, _Mapping]] = ...) -> None: ...
            ACTIONS_FIELD_NUMBER: _ClassVar[int]
            EFFECTIVE_DERIVED_ROLES_FIELD_NUMBER: _ClassVar[int]
            actions: _containers.MessageMap[str, CheckResourcesResponse.ResultEntry.Meta.EffectMeta]
            effective_derived_roles: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, actions: _Optional[_Mapping[str, CheckResourcesResponse.ResultEntry.Meta.EffectMeta]] = ..., effective_derived_roles: _Optional[_Iterable[str]] = ...) -> None: ...
        class ActionsEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _effect_pb2.Effect
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_effect_pb2.Effect, str]] = ...) -> None: ...
        RESOURCE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        VALIDATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
        META_FIELD_NUMBER: _ClassVar[int]
        OUTPUTS_FIELD_NUMBER: _ClassVar[int]
        resource: CheckResourcesResponse.ResultEntry.Resource
        actions: _containers.ScalarMap[str, _effect_pb2.Effect]
        validation_errors: _containers.RepeatedCompositeFieldContainer[_schema_pb2.ValidationError]
        meta: CheckResourcesResponse.ResultEntry.Meta
        outputs: _containers.RepeatedCompositeFieldContainer[_engine_pb2.OutputEntry]
        def __init__(self, resource: _Optional[_Union[CheckResourcesResponse.ResultEntry.Resource, _Mapping]] = ..., actions: _Optional[_Mapping[str, _effect_pb2.Effect]] = ..., validation_errors: _Optional[_Iterable[_Union[_schema_pb2.ValidationError, _Mapping]]] = ..., meta: _Optional[_Union[CheckResourcesResponse.ResultEntry.Meta, _Mapping]] = ..., outputs: _Optional[_Iterable[_Union[_engine_pb2.OutputEntry, _Mapping]]] = ...) -> None: ...
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    results: _containers.RepeatedCompositeFieldContainer[CheckResourcesResponse.ResultEntry]
    def __init__(self, request_id: _Optional[str] = ..., results: _Optional[_Iterable[_Union[CheckResourcesResponse.ResultEntry, _Mapping]]] = ...) -> None: ...

class PlaygroundFailure(_message.Message):
    __slots__ = ["errors"]
    class Error(_message.Message):
        __slots__ = ["file", "error"]
        FILE_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        file: str
        error: str
        def __init__(self, file: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[PlaygroundFailure.Error]
    def __init__(self, errors: _Optional[_Iterable[_Union[PlaygroundFailure.Error, _Mapping]]] = ...) -> None: ...

class PlaygroundValidateResponse(_message.Message):
    __slots__ = ["playground_id", "failure", "success"]
    PLAYGROUND_ID_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    playground_id: str
    failure: PlaygroundFailure
    success: _empty_pb2.Empty
    def __init__(self, playground_id: _Optional[str] = ..., failure: _Optional[_Union[PlaygroundFailure, _Mapping]] = ..., success: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ...) -> None: ...

class PlaygroundTestResponse(_message.Message):
    __slots__ = ["playground_id", "failure", "success"]
    class TestResults(_message.Message):
        __slots__ = ["results"]
        RESULTS_FIELD_NUMBER: _ClassVar[int]
        results: _policy_pb2.TestResults
        def __init__(self, results: _Optional[_Union[_policy_pb2.TestResults, _Mapping]] = ...) -> None: ...
    PLAYGROUND_ID_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    playground_id: str
    failure: PlaygroundFailure
    success: PlaygroundTestResponse.TestResults
    def __init__(self, playground_id: _Optional[str] = ..., failure: _Optional[_Union[PlaygroundFailure, _Mapping]] = ..., success: _Optional[_Union[PlaygroundTestResponse.TestResults, _Mapping]] = ...) -> None: ...

class PlaygroundEvaluateResponse(_message.Message):
    __slots__ = ["playground_id", "failure", "success"]
    class EvalResult(_message.Message):
        __slots__ = ["action", "effect", "policy", "effective_derived_roles", "validation_errors"]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        EFFECT_FIELD_NUMBER: _ClassVar[int]
        POLICY_FIELD_NUMBER: _ClassVar[int]
        EFFECTIVE_DERIVED_ROLES_FIELD_NUMBER: _ClassVar[int]
        VALIDATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
        action: str
        effect: _effect_pb2.Effect
        policy: str
        effective_derived_roles: _containers.RepeatedScalarFieldContainer[str]
        validation_errors: _containers.RepeatedCompositeFieldContainer[_schema_pb2.ValidationError]
        def __init__(self, action: _Optional[str] = ..., effect: _Optional[_Union[_effect_pb2.Effect, str]] = ..., policy: _Optional[str] = ..., effective_derived_roles: _Optional[_Iterable[str]] = ..., validation_errors: _Optional[_Iterable[_Union[_schema_pb2.ValidationError, _Mapping]]] = ...) -> None: ...
    class EvalResultList(_message.Message):
        __slots__ = ["results", "effective_derived_roles", "validation_errors", "outputs"]
        RESULTS_FIELD_NUMBER: _ClassVar[int]
        EFFECTIVE_DERIVED_ROLES_FIELD_NUMBER: _ClassVar[int]
        VALIDATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
        OUTPUTS_FIELD_NUMBER: _ClassVar[int]
        results: _containers.RepeatedCompositeFieldContainer[PlaygroundEvaluateResponse.EvalResult]
        effective_derived_roles: _containers.RepeatedScalarFieldContainer[str]
        validation_errors: _containers.RepeatedCompositeFieldContainer[_schema_pb2.ValidationError]
        outputs: _containers.RepeatedCompositeFieldContainer[_engine_pb2.OutputEntry]
        def __init__(self, results: _Optional[_Iterable[_Union[PlaygroundEvaluateResponse.EvalResult, _Mapping]]] = ..., effective_derived_roles: _Optional[_Iterable[str]] = ..., validation_errors: _Optional[_Iterable[_Union[_schema_pb2.ValidationError, _Mapping]]] = ..., outputs: _Optional[_Iterable[_Union[_engine_pb2.OutputEntry, _Mapping]]] = ...) -> None: ...
    PLAYGROUND_ID_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    playground_id: str
    failure: PlaygroundFailure
    success: PlaygroundEvaluateResponse.EvalResultList
    def __init__(self, playground_id: _Optional[str] = ..., failure: _Optional[_Union[PlaygroundFailure, _Mapping]] = ..., success: _Optional[_Union[PlaygroundEvaluateResponse.EvalResultList, _Mapping]] = ...) -> None: ...

class PlaygroundProxyResponse(_message.Message):
    __slots__ = ["playground_id", "failure", "check_resource_set", "check_resource_batch", "plan_resources", "check_resources"]
    PLAYGROUND_ID_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    CHECK_RESOURCE_SET_FIELD_NUMBER: _ClassVar[int]
    CHECK_RESOURCE_BATCH_FIELD_NUMBER: _ClassVar[int]
    PLAN_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    CHECK_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    playground_id: str
    failure: PlaygroundFailure
    check_resource_set: CheckResourceSetResponse
    check_resource_batch: CheckResourceBatchResponse
    plan_resources: PlanResourcesResponse
    check_resources: CheckResourcesResponse
    def __init__(self, playground_id: _Optional[str] = ..., failure: _Optional[_Union[PlaygroundFailure, _Mapping]] = ..., check_resource_set: _Optional[_Union[CheckResourceSetResponse, _Mapping]] = ..., check_resource_batch: _Optional[_Union[CheckResourceBatchResponse, _Mapping]] = ..., plan_resources: _Optional[_Union[PlanResourcesResponse, _Mapping]] = ..., check_resources: _Optional[_Union[CheckResourcesResponse, _Mapping]] = ...) -> None: ...

class AddOrUpdatePolicyResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: _empty_pb2.Empty
    def __init__(self, success: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ...) -> None: ...

class ListAuditLogEntriesResponse(_message.Message):
    __slots__ = ["access_log_entry", "decision_log_entry"]
    ACCESS_LOG_ENTRY_FIELD_NUMBER: _ClassVar[int]
    DECISION_LOG_ENTRY_FIELD_NUMBER: _ClassVar[int]
    access_log_entry: _audit_pb2.AccessLogEntry
    decision_log_entry: _audit_pb2.DecisionLogEntry
    def __init__(self, access_log_entry: _Optional[_Union[_audit_pb2.AccessLogEntry, _Mapping]] = ..., decision_log_entry: _Optional[_Union[_audit_pb2.DecisionLogEntry, _Mapping]] = ...) -> None: ...

class ServerInfoResponse(_message.Message):
    __slots__ = ["version", "commit", "build_date"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    COMMIT_FIELD_NUMBER: _ClassVar[int]
    BUILD_DATE_FIELD_NUMBER: _ClassVar[int]
    version: str
    commit: str
    build_date: str
    def __init__(self, version: _Optional[str] = ..., commit: _Optional[str] = ..., build_date: _Optional[str] = ...) -> None: ...

class ListPoliciesResponse(_message.Message):
    __slots__ = ["policy_ids"]
    POLICY_IDS_FIELD_NUMBER: _ClassVar[int]
    policy_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, policy_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class GetPolicyResponse(_message.Message):
    __slots__ = ["policies"]
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    policies: _containers.RepeatedCompositeFieldContainer[_policy_pb2.Policy]
    def __init__(self, policies: _Optional[_Iterable[_Union[_policy_pb2.Policy, _Mapping]]] = ...) -> None: ...

class DisablePolicyResponse(_message.Message):
    __slots__ = ["disabled_policies"]
    DISABLED_POLICIES_FIELD_NUMBER: _ClassVar[int]
    disabled_policies: int
    def __init__(self, disabled_policies: _Optional[int] = ...) -> None: ...

class EnablePolicyResponse(_message.Message):
    __slots__ = ["enabled_policies"]
    ENABLED_POLICIES_FIELD_NUMBER: _ClassVar[int]
    enabled_policies: int
    def __init__(self, enabled_policies: _Optional[int] = ...) -> None: ...

class AddOrUpdateSchemaResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListSchemasResponse(_message.Message):
    __slots__ = ["schema_ids"]
    SCHEMA_IDS_FIELD_NUMBER: _ClassVar[int]
    schema_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, schema_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class GetSchemaResponse(_message.Message):
    __slots__ = ["schemas"]
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    schemas: _containers.RepeatedCompositeFieldContainer[_schema_pb2.Schema]
    def __init__(self, schemas: _Optional[_Iterable[_Union[_schema_pb2.Schema, _Mapping]]] = ...) -> None: ...

class DeleteSchemaResponse(_message.Message):
    __slots__ = ["deleted_schemas"]
    DELETED_SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    deleted_schemas: int
    def __init__(self, deleted_schemas: _Optional[int] = ...) -> None: ...

class ReloadStoreResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
