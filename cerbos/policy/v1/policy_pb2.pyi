from cerbos.effect.v1 import effect_pb2 as _effect_pb2
from cerbos.engine.v1 import engine_pb2 as _engine_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Condition(_message.Message):
    __slots__ = ["match", "script"]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    match: Match
    script: str
    def __init__(self, match: _Optional[_Union[Match, _Mapping]] = ..., script: _Optional[str] = ...) -> None: ...

class DerivedRoles(_message.Message):
    __slots__ = ["definitions", "name"]
    DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    definitions: _containers.RepeatedCompositeFieldContainer[RoleDef]
    name: str
    def __init__(self, name: _Optional[str] = ..., definitions: _Optional[_Iterable[_Union[RoleDef, _Mapping]]] = ...) -> None: ...

class Match(_message.Message):
    __slots__ = ["all", "any", "expr", "none"]
    class ExprList(_message.Message):
        __slots__ = ["of"]
        OF_FIELD_NUMBER: _ClassVar[int]
        of: _containers.RepeatedCompositeFieldContainer[Match]
        def __init__(self, of: _Optional[_Iterable[_Union[Match, _Mapping]]] = ...) -> None: ...
    ALL_FIELD_NUMBER: _ClassVar[int]
    ANY_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    NONE_FIELD_NUMBER: _ClassVar[int]
    all: Match.ExprList
    any: Match.ExprList
    expr: str
    none: Match.ExprList
    def __init__(self, all: _Optional[_Union[Match.ExprList, _Mapping]] = ..., any: _Optional[_Union[Match.ExprList, _Mapping]] = ..., none: _Optional[_Union[Match.ExprList, _Mapping]] = ..., expr: _Optional[str] = ...) -> None: ...

class Metadata(_message.Message):
    __slots__ = ["annotations", "hash", "source_file", "store_identifer", "store_identifier"]
    class AnnotationsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FILE_FIELD_NUMBER: _ClassVar[int]
    STORE_IDENTIFER_FIELD_NUMBER: _ClassVar[int]
    STORE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    annotations: _containers.ScalarMap[str, str]
    hash: _wrappers_pb2.UInt64Value
    source_file: str
    store_identifer: str
    store_identifier: str
    def __init__(self, source_file: _Optional[str] = ..., annotations: _Optional[_Mapping[str, str]] = ..., hash: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., store_identifer: _Optional[str] = ..., store_identifier: _Optional[str] = ...) -> None: ...

class Output(_message.Message):
    __slots__ = ["expr"]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    expr: str
    def __init__(self, expr: _Optional[str] = ...) -> None: ...

class Policy(_message.Message):
    __slots__ = ["api_version", "derived_roles", "description", "disabled", "metadata", "principal_policy", "resource_policy", "variables"]
    class VariablesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    DERIVED_ROLES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_POLICY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POLICY_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    api_version: str
    derived_roles: DerivedRoles
    description: str
    disabled: bool
    metadata: Metadata
    principal_policy: PrincipalPolicy
    resource_policy: ResourcePolicy
    variables: _containers.ScalarMap[str, str]
    def __init__(self, api_version: _Optional[str] = ..., disabled: bool = ..., description: _Optional[str] = ..., metadata: _Optional[_Union[Metadata, _Mapping]] = ..., resource_policy: _Optional[_Union[ResourcePolicy, _Mapping]] = ..., principal_policy: _Optional[_Union[PrincipalPolicy, _Mapping]] = ..., derived_roles: _Optional[_Union[DerivedRoles, _Mapping]] = ..., variables: _Optional[_Mapping[str, str]] = ...) -> None: ...

class PrincipalPolicy(_message.Message):
    __slots__ = ["principal", "rules", "scope", "version"]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    principal: str
    rules: _containers.RepeatedCompositeFieldContainer[PrincipalRule]
    scope: str
    version: str
    def __init__(self, principal: _Optional[str] = ..., version: _Optional[str] = ..., rules: _Optional[_Iterable[_Union[PrincipalRule, _Mapping]]] = ..., scope: _Optional[str] = ...) -> None: ...

class PrincipalRule(_message.Message):
    __slots__ = ["actions", "resource"]
    class Action(_message.Message):
        __slots__ = ["action", "condition", "effect", "name", "output"]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        CONDITION_FIELD_NUMBER: _ClassVar[int]
        EFFECT_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_FIELD_NUMBER: _ClassVar[int]
        action: str
        condition: Condition
        effect: _effect_pb2.Effect
        name: str
        output: Output
        def __init__(self, action: _Optional[str] = ..., condition: _Optional[_Union[Condition, _Mapping]] = ..., effect: _Optional[_Union[_effect_pb2.Effect, str]] = ..., name: _Optional[str] = ..., output: _Optional[_Union[Output, _Mapping]] = ...) -> None: ...
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[PrincipalRule.Action]
    resource: str
    def __init__(self, resource: _Optional[str] = ..., actions: _Optional[_Iterable[_Union[PrincipalRule.Action, _Mapping]]] = ...) -> None: ...

class ResourcePolicy(_message.Message):
    __slots__ = ["import_derived_roles", "resource", "rules", "schemas", "scope", "version"]
    IMPORT_DERIVED_ROLES_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    import_derived_roles: _containers.RepeatedScalarFieldContainer[str]
    resource: str
    rules: _containers.RepeatedCompositeFieldContainer[ResourceRule]
    schemas: Schemas
    scope: str
    version: str
    def __init__(self, resource: _Optional[str] = ..., version: _Optional[str] = ..., import_derived_roles: _Optional[_Iterable[str]] = ..., rules: _Optional[_Iterable[_Union[ResourceRule, _Mapping]]] = ..., scope: _Optional[str] = ..., schemas: _Optional[_Union[Schemas, _Mapping]] = ...) -> None: ...

class ResourceRule(_message.Message):
    __slots__ = ["actions", "condition", "derived_roles", "effect", "name", "output", "roles"]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    DERIVED_ROLES_FIELD_NUMBER: _ClassVar[int]
    EFFECT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedScalarFieldContainer[str]
    condition: Condition
    derived_roles: _containers.RepeatedScalarFieldContainer[str]
    effect: _effect_pb2.Effect
    name: str
    output: Output
    roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, actions: _Optional[_Iterable[str]] = ..., derived_roles: _Optional[_Iterable[str]] = ..., roles: _Optional[_Iterable[str]] = ..., condition: _Optional[_Union[Condition, _Mapping]] = ..., effect: _Optional[_Union[_effect_pb2.Effect, str]] = ..., name: _Optional[str] = ..., output: _Optional[_Union[Output, _Mapping]] = ...) -> None: ...

class RoleDef(_message.Message):
    __slots__ = ["condition", "name", "parent_roles"]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_ROLES_FIELD_NUMBER: _ClassVar[int]
    condition: Condition
    name: str
    parent_roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., parent_roles: _Optional[_Iterable[str]] = ..., condition: _Optional[_Union[Condition, _Mapping]] = ...) -> None: ...

class Schemas(_message.Message):
    __slots__ = ["principal_schema", "resource_schema"]
    class IgnoreWhen(_message.Message):
        __slots__ = ["actions"]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        actions: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, actions: _Optional[_Iterable[str]] = ...) -> None: ...
    class Schema(_message.Message):
        __slots__ = ["ignore_when", "ref"]
        IGNORE_WHEN_FIELD_NUMBER: _ClassVar[int]
        REF_FIELD_NUMBER: _ClassVar[int]
        ignore_when: Schemas.IgnoreWhen
        ref: str
        def __init__(self, ref: _Optional[str] = ..., ignore_when: _Optional[_Union[Schemas.IgnoreWhen, _Mapping]] = ...) -> None: ...
    PRINCIPAL_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    principal_schema: Schemas.Schema
    resource_schema: Schemas.Schema
    def __init__(self, principal_schema: _Optional[_Union[Schemas.Schema, _Mapping]] = ..., resource_schema: _Optional[_Union[Schemas.Schema, _Mapping]] = ...) -> None: ...

class Test(_message.Message):
    __slots__ = ["description", "expected", "expected_outputs", "input", "name", "options", "skip", "skip_reason"]
    class ExpectedEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _effect_pb2.Effect
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_effect_pb2.Effect, str]] = ...) -> None: ...
    class ExpectedOutputsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Test.OutputEntries
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Test.OutputEntries, _Mapping]] = ...) -> None: ...
    class OutputEntries(_message.Message):
        __slots__ = ["entries"]
        class EntriesEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _struct_pb2.Value
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.MessageMap[str, _struct_pb2.Value]
        def __init__(self, entries: _Optional[_Mapping[str, _struct_pb2.Value]] = ...) -> None: ...
    class TestName(_message.Message):
        __slots__ = ["principal_key", "resource_key", "test_table_name"]
        PRINCIPAL_KEY_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_KEY_FIELD_NUMBER: _ClassVar[int]
        TEST_TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
        principal_key: str
        resource_key: str
        test_table_name: str
        def __init__(self, test_table_name: _Optional[str] = ..., principal_key: _Optional[str] = ..., resource_key: _Optional[str] = ...) -> None: ...
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    SKIP_REASON_FIELD_NUMBER: _ClassVar[int]
    description: str
    expected: _containers.ScalarMap[str, _effect_pb2.Effect]
    expected_outputs: _containers.MessageMap[str, Test.OutputEntries]
    input: _engine_pb2.CheckInput
    name: Test.TestName
    options: TestOptions
    skip: bool
    skip_reason: str
    def __init__(self, name: _Optional[_Union[Test.TestName, _Mapping]] = ..., description: _Optional[str] = ..., skip: bool = ..., skip_reason: _Optional[str] = ..., input: _Optional[_Union[_engine_pb2.CheckInput, _Mapping]] = ..., expected: _Optional[_Mapping[str, _effect_pb2.Effect]] = ..., options: _Optional[_Union[TestOptions, _Mapping]] = ..., expected_outputs: _Optional[_Mapping[str, Test.OutputEntries]] = ...) -> None: ...

class TestFixture(_message.Message):
    __slots__ = []
    class AuxData(_message.Message):
        __slots__ = ["aux_data"]
        class AuxDataEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _engine_pb2.AuxData
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_engine_pb2.AuxData, _Mapping]] = ...) -> None: ...
        AUX_DATA_FIELD_NUMBER: _ClassVar[int]
        aux_data: _containers.MessageMap[str, _engine_pb2.AuxData]
        def __init__(self, aux_data: _Optional[_Mapping[str, _engine_pb2.AuxData]] = ...) -> None: ...
    class Principals(_message.Message):
        __slots__ = ["principals"]
        class PrincipalsEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _engine_pb2.Principal
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_engine_pb2.Principal, _Mapping]] = ...) -> None: ...
        PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
        principals: _containers.MessageMap[str, _engine_pb2.Principal]
        def __init__(self, principals: _Optional[_Mapping[str, _engine_pb2.Principal]] = ...) -> None: ...
    class Resources(_message.Message):
        __slots__ = ["resources"]
        class ResourcesEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _engine_pb2.Resource
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_engine_pb2.Resource, _Mapping]] = ...) -> None: ...
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        resources: _containers.MessageMap[str, _engine_pb2.Resource]
        def __init__(self, resources: _Optional[_Mapping[str, _engine_pb2.Resource]] = ...) -> None: ...
    def __init__(self) -> None: ...

class TestOptions(_message.Message):
    __slots__ = ["now"]
    NOW_FIELD_NUMBER: _ClassVar[int]
    now: _timestamp_pb2.Timestamp
    def __init__(self, now: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class TestResults(_message.Message):
    __slots__ = ["suites", "summary"]
    class Result(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Action(_message.Message):
        __slots__ = ["details", "name"]
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        details: TestResults.Details
        name: str
        def __init__(self, name: _Optional[str] = ..., details: _Optional[_Union[TestResults.Details, _Mapping]] = ...) -> None: ...
    class Details(_message.Message):
        __slots__ = ["engine_trace", "error", "failure", "result"]
        ENGINE_TRACE_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        FAILURE_FIELD_NUMBER: _ClassVar[int]
        RESULT_FIELD_NUMBER: _ClassVar[int]
        engine_trace: _containers.RepeatedCompositeFieldContainer[_engine_pb2.Trace]
        error: str
        failure: TestResults.Failure
        result: TestResults.Result
        def __init__(self, result: _Optional[_Union[TestResults.Result, str]] = ..., failure: _Optional[_Union[TestResults.Failure, _Mapping]] = ..., error: _Optional[str] = ..., engine_trace: _Optional[_Iterable[_Union[_engine_pb2.Trace, _Mapping]]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ["actual", "expected", "outputs"]
        ACTUAL_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_FIELD_NUMBER: _ClassVar[int]
        OUTPUTS_FIELD_NUMBER: _ClassVar[int]
        actual: _effect_pb2.Effect
        expected: _effect_pb2.Effect
        outputs: _containers.RepeatedCompositeFieldContainer[TestResults.OutputFailure]
        def __init__(self, expected: _Optional[_Union[_effect_pb2.Effect, str]] = ..., actual: _Optional[_Union[_effect_pb2.Effect, str]] = ..., outputs: _Optional[_Iterable[_Union[TestResults.OutputFailure, _Mapping]]] = ...) -> None: ...
    class OutputFailure(_message.Message):
        __slots__ = ["mismatched", "missing", "src"]
        class MismatchedValue(_message.Message):
            __slots__ = ["actual", "expected"]
            ACTUAL_FIELD_NUMBER: _ClassVar[int]
            EXPECTED_FIELD_NUMBER: _ClassVar[int]
            actual: _struct_pb2.Value
            expected: _struct_pb2.Value
            def __init__(self, expected: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., actual: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
        class MissingValue(_message.Message):
            __slots__ = ["expected"]
            EXPECTED_FIELD_NUMBER: _ClassVar[int]
            expected: _struct_pb2.Value
            def __init__(self, expected: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
        MISMATCHED_FIELD_NUMBER: _ClassVar[int]
        MISSING_FIELD_NUMBER: _ClassVar[int]
        SRC_FIELD_NUMBER: _ClassVar[int]
        mismatched: TestResults.OutputFailure.MismatchedValue
        missing: TestResults.OutputFailure.MissingValue
        src: str
        def __init__(self, src: _Optional[str] = ..., mismatched: _Optional[_Union[TestResults.OutputFailure.MismatchedValue, _Mapping]] = ..., missing: _Optional[_Union[TestResults.OutputFailure.MissingValue, _Mapping]] = ...) -> None: ...
    class Principal(_message.Message):
        __slots__ = ["name", "resources"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        name: str
        resources: _containers.RepeatedCompositeFieldContainer[TestResults.Resource]
        def __init__(self, name: _Optional[str] = ..., resources: _Optional[_Iterable[_Union[TestResults.Resource, _Mapping]]] = ...) -> None: ...
    class Resource(_message.Message):
        __slots__ = ["actions", "name"]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        actions: _containers.RepeatedCompositeFieldContainer[TestResults.Action]
        name: str
        def __init__(self, name: _Optional[str] = ..., actions: _Optional[_Iterable[_Union[TestResults.Action, _Mapping]]] = ...) -> None: ...
    class Suite(_message.Message):
        __slots__ = ["description", "error", "file", "name", "principals", "summary", "test_cases"]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        FILE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
        SUMMARY_FIELD_NUMBER: _ClassVar[int]
        TEST_CASES_FIELD_NUMBER: _ClassVar[int]
        description: str
        error: str
        file: str
        name: str
        principals: _containers.RepeatedCompositeFieldContainer[TestResults.Principal]
        summary: TestResults.Summary
        test_cases: _containers.RepeatedCompositeFieldContainer[TestResults.TestCase]
        def __init__(self, file: _Optional[str] = ..., name: _Optional[str] = ..., principals: _Optional[_Iterable[_Union[TestResults.Principal, _Mapping]]] = ..., summary: _Optional[_Union[TestResults.Summary, _Mapping]] = ..., error: _Optional[str] = ..., test_cases: _Optional[_Iterable[_Union[TestResults.TestCase, _Mapping]]] = ..., description: _Optional[str] = ...) -> None: ...
    class Summary(_message.Message):
        __slots__ = ["overall_result", "result_counts", "tests_count"]
        OVERALL_RESULT_FIELD_NUMBER: _ClassVar[int]
        RESULT_COUNTS_FIELD_NUMBER: _ClassVar[int]
        TESTS_COUNT_FIELD_NUMBER: _ClassVar[int]
        overall_result: TestResults.Result
        result_counts: _containers.RepeatedCompositeFieldContainer[TestResults.Tally]
        tests_count: int
        def __init__(self, overall_result: _Optional[_Union[TestResults.Result, str]] = ..., tests_count: _Optional[int] = ..., result_counts: _Optional[_Iterable[_Union[TestResults.Tally, _Mapping]]] = ...) -> None: ...
    class Tally(_message.Message):
        __slots__ = ["count", "result"]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        RESULT_FIELD_NUMBER: _ClassVar[int]
        count: int
        result: TestResults.Result
        def __init__(self, result: _Optional[_Union[TestResults.Result, str]] = ..., count: _Optional[int] = ...) -> None: ...
    class TestCase(_message.Message):
        __slots__ = ["name", "principals"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
        name: str
        principals: _containers.RepeatedCompositeFieldContainer[TestResults.Principal]
        def __init__(self, name: _Optional[str] = ..., principals: _Optional[_Iterable[_Union[TestResults.Principal, _Mapping]]] = ...) -> None: ...
    RESULT_ERRORED: TestResults.Result
    RESULT_FAILED: TestResults.Result
    RESULT_PASSED: TestResults.Result
    RESULT_SKIPPED: TestResults.Result
    RESULT_UNSPECIFIED: TestResults.Result
    SUITES_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    suites: _containers.RepeatedCompositeFieldContainer[TestResults.Suite]
    summary: TestResults.Summary
    def __init__(self, suites: _Optional[_Iterable[_Union[TestResults.Suite, _Mapping]]] = ..., summary: _Optional[_Union[TestResults.Summary, _Mapping]] = ...) -> None: ...

class TestSuite(_message.Message):
    __slots__ = ["aux_data", "description", "name", "options", "principals", "resources", "skip", "skip_reason", "tests"]
    class AuxDataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _engine_pb2.AuxData
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_engine_pb2.AuxData, _Mapping]] = ...) -> None: ...
    class PrincipalsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _engine_pb2.Principal
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_engine_pb2.Principal, _Mapping]] = ...) -> None: ...
    class ResourcesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _engine_pb2.Resource
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_engine_pb2.Resource, _Mapping]] = ...) -> None: ...
    AUX_DATA_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    SKIP_REASON_FIELD_NUMBER: _ClassVar[int]
    TESTS_FIELD_NUMBER: _ClassVar[int]
    aux_data: _containers.MessageMap[str, _engine_pb2.AuxData]
    description: str
    name: str
    options: TestOptions
    principals: _containers.MessageMap[str, _engine_pb2.Principal]
    resources: _containers.MessageMap[str, _engine_pb2.Resource]
    skip: bool
    skip_reason: str
    tests: _containers.RepeatedCompositeFieldContainer[TestTable]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., skip: bool = ..., skip_reason: _Optional[str] = ..., tests: _Optional[_Iterable[_Union[TestTable, _Mapping]]] = ..., principals: _Optional[_Mapping[str, _engine_pb2.Principal]] = ..., resources: _Optional[_Mapping[str, _engine_pb2.Resource]] = ..., aux_data: _Optional[_Mapping[str, _engine_pb2.AuxData]] = ..., options: _Optional[_Union[TestOptions, _Mapping]] = ...) -> None: ...

class TestTable(_message.Message):
    __slots__ = ["description", "expected", "input", "name", "options", "skip", "skip_reason"]
    class Expectation(_message.Message):
        __slots__ = ["actions", "outputs", "principal", "resource"]
        class ActionsEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _effect_pb2.Effect
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_effect_pb2.Effect, str]] = ...) -> None: ...
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        OUTPUTS_FIELD_NUMBER: _ClassVar[int]
        PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_FIELD_NUMBER: _ClassVar[int]
        actions: _containers.ScalarMap[str, _effect_pb2.Effect]
        outputs: _containers.RepeatedCompositeFieldContainer[TestTable.OutputExpectations]
        principal: str
        resource: str
        def __init__(self, principal: _Optional[str] = ..., resource: _Optional[str] = ..., actions: _Optional[_Mapping[str, _effect_pb2.Effect]] = ..., outputs: _Optional[_Iterable[_Union[TestTable.OutputExpectations, _Mapping]]] = ...) -> None: ...
    class Input(_message.Message):
        __slots__ = ["actions", "aux_data", "principals", "resources"]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        AUX_DATA_FIELD_NUMBER: _ClassVar[int]
        PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        actions: _containers.RepeatedScalarFieldContainer[str]
        aux_data: str
        principals: _containers.RepeatedScalarFieldContainer[str]
        resources: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, principals: _Optional[_Iterable[str]] = ..., resources: _Optional[_Iterable[str]] = ..., actions: _Optional[_Iterable[str]] = ..., aux_data: _Optional[str] = ...) -> None: ...
    class OutputExpectations(_message.Message):
        __slots__ = ["action", "expected"]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_FIELD_NUMBER: _ClassVar[int]
        action: str
        expected: _containers.RepeatedCompositeFieldContainer[_engine_pb2.OutputEntry]
        def __init__(self, action: _Optional[str] = ..., expected: _Optional[_Iterable[_Union[_engine_pb2.OutputEntry, _Mapping]]] = ...) -> None: ...
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    SKIP_REASON_FIELD_NUMBER: _ClassVar[int]
    description: str
    expected: _containers.RepeatedCompositeFieldContainer[TestTable.Expectation]
    input: TestTable.Input
    name: str
    options: TestOptions
    skip: bool
    skip_reason: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., skip: bool = ..., skip_reason: _Optional[str] = ..., input: _Optional[_Union[TestTable.Input, _Mapping]] = ..., expected: _Optional[_Iterable[_Union[TestTable.Expectation, _Mapping]]] = ..., options: _Optional[_Union[TestOptions, _Mapping]] = ...) -> None: ...
