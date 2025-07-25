from buf.validate import validate_pb2 as _validate_pb2
from cerbos.effect.v1 import effect_pb2 as _effect_pb2
from cerbos.engine.v1 import engine_pb2 as _engine_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    KIND_UNSPECIFIED: _ClassVar[Kind]
    KIND_DERIVED_ROLES: _ClassVar[Kind]
    KIND_EXPORT_VARIABLES: _ClassVar[Kind]
    KIND_PRINCIPAL: _ClassVar[Kind]
    KIND_RESOURCE: _ClassVar[Kind]
    KIND_ROLE_POLICY: _ClassVar[Kind]
    KIND_EXPORT_CONSTANTS: _ClassVar[Kind]

class ScopePermissions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SCOPE_PERMISSIONS_UNSPECIFIED: _ClassVar[ScopePermissions]
    SCOPE_PERMISSIONS_OVERRIDE_PARENT: _ClassVar[ScopePermissions]
    SCOPE_PERMISSIONS_REQUIRE_PARENTAL_CONSENT_FOR_ALLOWS: _ClassVar[ScopePermissions]
KIND_UNSPECIFIED: Kind
KIND_DERIVED_ROLES: Kind
KIND_EXPORT_VARIABLES: Kind
KIND_PRINCIPAL: Kind
KIND_RESOURCE: Kind
KIND_ROLE_POLICY: Kind
KIND_EXPORT_CONSTANTS: Kind
SCOPE_PERMISSIONS_UNSPECIFIED: ScopePermissions
SCOPE_PERMISSIONS_OVERRIDE_PARENT: ScopePermissions
SCOPE_PERMISSIONS_REQUIRE_PARENTAL_CONSENT_FOR_ALLOWS: ScopePermissions

class Policy(_message.Message):
    __slots__ = ["api_version", "disabled", "description", "metadata", "resource_policy", "principal_policy", "derived_roles", "export_variables", "role_policy", "export_constants", "variables", "json_schema"]
    class VariablesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POLICY_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_POLICY_FIELD_NUMBER: _ClassVar[int]
    DERIVED_ROLES_FIELD_NUMBER: _ClassVar[int]
    EXPORT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    ROLE_POLICY_FIELD_NUMBER: _ClassVar[int]
    EXPORT_CONSTANTS_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    JSON_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    api_version: str
    disabled: bool
    description: str
    metadata: Metadata
    resource_policy: ResourcePolicy
    principal_policy: PrincipalPolicy
    derived_roles: DerivedRoles
    export_variables: ExportVariables
    role_policy: RolePolicy
    export_constants: ExportConstants
    variables: _containers.ScalarMap[str, str]
    json_schema: str
    def __init__(self, api_version: _Optional[str] = ..., disabled: bool = ..., description: _Optional[str] = ..., metadata: _Optional[_Union[Metadata, _Mapping]] = ..., resource_policy: _Optional[_Union[ResourcePolicy, _Mapping]] = ..., principal_policy: _Optional[_Union[PrincipalPolicy, _Mapping]] = ..., derived_roles: _Optional[_Union[DerivedRoles, _Mapping]] = ..., export_variables: _Optional[_Union[ExportVariables, _Mapping]] = ..., role_policy: _Optional[_Union[RolePolicy, _Mapping]] = ..., export_constants: _Optional[_Union[ExportConstants, _Mapping]] = ..., variables: _Optional[_Mapping[str, str]] = ..., json_schema: _Optional[str] = ...) -> None: ...

class SourceAttributes(_message.Message):
    __slots__ = ["attributes"]
    class AttributesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.MessageMap[str, _struct_pb2.Value]
    def __init__(self, attributes: _Optional[_Mapping[str, _struct_pb2.Value]] = ...) -> None: ...

class Metadata(_message.Message):
    __slots__ = ["source_file", "annotations", "hash", "store_identifer", "store_identifier", "source_attributes"]
    class AnnotationsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SOURCE_FILE_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    STORE_IDENTIFER_FIELD_NUMBER: _ClassVar[int]
    STORE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    source_file: str
    annotations: _containers.ScalarMap[str, str]
    hash: _wrappers_pb2.UInt64Value
    store_identifer: str
    store_identifier: str
    source_attributes: SourceAttributes
    def __init__(self, source_file: _Optional[str] = ..., annotations: _Optional[_Mapping[str, str]] = ..., hash: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., store_identifer: _Optional[str] = ..., store_identifier: _Optional[str] = ..., source_attributes: _Optional[_Union[SourceAttributes, _Mapping]] = ...) -> None: ...

class ResourcePolicy(_message.Message):
    __slots__ = ["resource", "version", "import_derived_roles", "rules", "scope", "schemas", "variables", "scope_permissions", "constants"]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    IMPORT_DERIVED_ROLES_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    SCOPE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    CONSTANTS_FIELD_NUMBER: _ClassVar[int]
    resource: str
    version: str
    import_derived_roles: _containers.RepeatedScalarFieldContainer[str]
    rules: _containers.RepeatedCompositeFieldContainer[ResourceRule]
    scope: str
    schemas: Schemas
    variables: Variables
    scope_permissions: ScopePermissions
    constants: Constants
    def __init__(self, resource: _Optional[str] = ..., version: _Optional[str] = ..., import_derived_roles: _Optional[_Iterable[str]] = ..., rules: _Optional[_Iterable[_Union[ResourceRule, _Mapping]]] = ..., scope: _Optional[str] = ..., schemas: _Optional[_Union[Schemas, _Mapping]] = ..., variables: _Optional[_Union[Variables, _Mapping]] = ..., scope_permissions: _Optional[_Union[ScopePermissions, str]] = ..., constants: _Optional[_Union[Constants, _Mapping]] = ...) -> None: ...

class ResourceRule(_message.Message):
    __slots__ = ["actions", "derived_roles", "roles", "condition", "effect", "name", "output"]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    DERIVED_ROLES_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    EFFECT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedScalarFieldContainer[str]
    derived_roles: _containers.RepeatedScalarFieldContainer[str]
    roles: _containers.RepeatedScalarFieldContainer[str]
    condition: Condition
    effect: _effect_pb2.Effect
    name: str
    output: Output
    def __init__(self, actions: _Optional[_Iterable[str]] = ..., derived_roles: _Optional[_Iterable[str]] = ..., roles: _Optional[_Iterable[str]] = ..., condition: _Optional[_Union[Condition, _Mapping]] = ..., effect: _Optional[_Union[_effect_pb2.Effect, str]] = ..., name: _Optional[str] = ..., output: _Optional[_Union[Output, _Mapping]] = ...) -> None: ...

class RolePolicy(_message.Message):
    __slots__ = ["role", "parent_roles", "scope", "rules", "scope_permissions"]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    PARENT_ROLES_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    SCOPE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    role: str
    parent_roles: _containers.RepeatedScalarFieldContainer[str]
    scope: str
    rules: _containers.RepeatedCompositeFieldContainer[RoleRule]
    scope_permissions: ScopePermissions
    def __init__(self, role: _Optional[str] = ..., parent_roles: _Optional[_Iterable[str]] = ..., scope: _Optional[str] = ..., rules: _Optional[_Iterable[_Union[RoleRule, _Mapping]]] = ..., scope_permissions: _Optional[_Union[ScopePermissions, str]] = ...) -> None: ...

class RoleRule(_message.Message):
    __slots__ = ["resource", "allow_actions", "condition"]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    resource: str
    allow_actions: _containers.RepeatedScalarFieldContainer[str]
    condition: Condition
    def __init__(self, resource: _Optional[str] = ..., allow_actions: _Optional[_Iterable[str]] = ..., condition: _Optional[_Union[Condition, _Mapping]] = ...) -> None: ...

class PrincipalPolicy(_message.Message):
    __slots__ = ["principal", "version", "rules", "scope", "variables", "scope_permissions", "constants"]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    SCOPE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    CONSTANTS_FIELD_NUMBER: _ClassVar[int]
    principal: str
    version: str
    rules: _containers.RepeatedCompositeFieldContainer[PrincipalRule]
    scope: str
    variables: Variables
    scope_permissions: ScopePermissions
    constants: Constants
    def __init__(self, principal: _Optional[str] = ..., version: _Optional[str] = ..., rules: _Optional[_Iterable[_Union[PrincipalRule, _Mapping]]] = ..., scope: _Optional[str] = ..., variables: _Optional[_Union[Variables, _Mapping]] = ..., scope_permissions: _Optional[_Union[ScopePermissions, str]] = ..., constants: _Optional[_Union[Constants, _Mapping]] = ...) -> None: ...

class PrincipalRule(_message.Message):
    __slots__ = ["resource", "actions"]
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
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    resource: str
    actions: _containers.RepeatedCompositeFieldContainer[PrincipalRule.Action]
    def __init__(self, resource: _Optional[str] = ..., actions: _Optional[_Iterable[_Union[PrincipalRule.Action, _Mapping]]] = ...) -> None: ...

class DerivedRoles(_message.Message):
    __slots__ = ["name", "definitions", "variables", "constants"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    CONSTANTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    definitions: _containers.RepeatedCompositeFieldContainer[RoleDef]
    variables: Variables
    constants: Constants
    def __init__(self, name: _Optional[str] = ..., definitions: _Optional[_Iterable[_Union[RoleDef, _Mapping]]] = ..., variables: _Optional[_Union[Variables, _Mapping]] = ..., constants: _Optional[_Union[Constants, _Mapping]] = ...) -> None: ...

class RoleDef(_message.Message):
    __slots__ = ["name", "parent_roles", "condition"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_ROLES_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    name: str
    parent_roles: _containers.RepeatedScalarFieldContainer[str]
    condition: Condition
    def __init__(self, name: _Optional[str] = ..., parent_roles: _Optional[_Iterable[str]] = ..., condition: _Optional[_Union[Condition, _Mapping]] = ...) -> None: ...

class ExportConstants(_message.Message):
    __slots__ = ["name", "definitions"]
    class DefinitionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    definitions: _containers.MessageMap[str, _struct_pb2.Value]
    def __init__(self, name: _Optional[str] = ..., definitions: _Optional[_Mapping[str, _struct_pb2.Value]] = ...) -> None: ...

class Constants(_message.Message):
    __slots__ = ["local"]
    class LocalEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    IMPORT_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FIELD_NUMBER: _ClassVar[int]
    local: _containers.MessageMap[str, _struct_pb2.Value]
    def __init__(self, local: _Optional[_Mapping[str, _struct_pb2.Value]] = ..., **kwargs) -> None: ...

class ExportVariables(_message.Message):
    __slots__ = ["name", "definitions"]
    class DefinitionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    definitions: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., definitions: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Variables(_message.Message):
    __slots__ = ["local"]
    class LocalEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    IMPORT_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FIELD_NUMBER: _ClassVar[int]
    local: _containers.ScalarMap[str, str]
    def __init__(self, local: _Optional[_Mapping[str, str]] = ..., **kwargs) -> None: ...

class Condition(_message.Message):
    __slots__ = ["match", "script"]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    match: Match
    script: str
    def __init__(self, match: _Optional[_Union[Match, _Mapping]] = ..., script: _Optional[str] = ...) -> None: ...

class Match(_message.Message):
    __slots__ = ["all", "any", "none", "expr"]
    class ExprList(_message.Message):
        __slots__ = ["of"]
        OF_FIELD_NUMBER: _ClassVar[int]
        of: _containers.RepeatedCompositeFieldContainer[Match]
        def __init__(self, of: _Optional[_Iterable[_Union[Match, _Mapping]]] = ...) -> None: ...
    ALL_FIELD_NUMBER: _ClassVar[int]
    ANY_FIELD_NUMBER: _ClassVar[int]
    NONE_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    all: Match.ExprList
    any: Match.ExprList
    none: Match.ExprList
    expr: str
    def __init__(self, all: _Optional[_Union[Match.ExprList, _Mapping]] = ..., any: _Optional[_Union[Match.ExprList, _Mapping]] = ..., none: _Optional[_Union[Match.ExprList, _Mapping]] = ..., expr: _Optional[str] = ...) -> None: ...

class Output(_message.Message):
    __slots__ = ["expr", "when"]
    class When(_message.Message):
        __slots__ = ["rule_activated", "condition_not_met"]
        RULE_ACTIVATED_FIELD_NUMBER: _ClassVar[int]
        CONDITION_NOT_MET_FIELD_NUMBER: _ClassVar[int]
        rule_activated: str
        condition_not_met: str
        def __init__(self, rule_activated: _Optional[str] = ..., condition_not_met: _Optional[str] = ...) -> None: ...
    EXPR_FIELD_NUMBER: _ClassVar[int]
    WHEN_FIELD_NUMBER: _ClassVar[int]
    expr: str
    when: Output.When
    def __init__(self, expr: _Optional[str] = ..., when: _Optional[_Union[Output.When, _Mapping]] = ...) -> None: ...

class Schemas(_message.Message):
    __slots__ = ["principal_schema", "resource_schema"]
    class IgnoreWhen(_message.Message):
        __slots__ = ["actions"]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        actions: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, actions: _Optional[_Iterable[str]] = ...) -> None: ...
    class Schema(_message.Message):
        __slots__ = ["ref", "ignore_when"]
        REF_FIELD_NUMBER: _ClassVar[int]
        IGNORE_WHEN_FIELD_NUMBER: _ClassVar[int]
        ref: str
        ignore_when: Schemas.IgnoreWhen
        def __init__(self, ref: _Optional[str] = ..., ignore_when: _Optional[_Union[Schemas.IgnoreWhen, _Mapping]] = ...) -> None: ...
    PRINCIPAL_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    principal_schema: Schemas.Schema
    resource_schema: Schemas.Schema
    def __init__(self, principal_schema: _Optional[_Union[Schemas.Schema, _Mapping]] = ..., resource_schema: _Optional[_Union[Schemas.Schema, _Mapping]] = ...) -> None: ...

class TestFixture(_message.Message):
    __slots__ = []
    class Principals(_message.Message):
        __slots__ = ["principals", "json_schema", "principal_groups"]
        class PrincipalsEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _engine_pb2.Principal
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_engine_pb2.Principal, _Mapping]] = ...) -> None: ...
        class PrincipalGroupsEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: TestFixtureGroup.Principals
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TestFixtureGroup.Principals, _Mapping]] = ...) -> None: ...
        PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
        JSON_SCHEMA_FIELD_NUMBER: _ClassVar[int]
        PRINCIPAL_GROUPS_FIELD_NUMBER: _ClassVar[int]
        principals: _containers.MessageMap[str, _engine_pb2.Principal]
        json_schema: str
        principal_groups: _containers.MessageMap[str, TestFixtureGroup.Principals]
        def __init__(self, principals: _Optional[_Mapping[str, _engine_pb2.Principal]] = ..., json_schema: _Optional[str] = ..., principal_groups: _Optional[_Mapping[str, TestFixtureGroup.Principals]] = ...) -> None: ...
    class Resources(_message.Message):
        __slots__ = ["resources", "json_schema", "resource_groups"]
        class ResourcesEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _engine_pb2.Resource
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_engine_pb2.Resource, _Mapping]] = ...) -> None: ...
        class ResourceGroupsEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: TestFixtureGroup.Resources
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TestFixtureGroup.Resources, _Mapping]] = ...) -> None: ...
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        JSON_SCHEMA_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_GROUPS_FIELD_NUMBER: _ClassVar[int]
        resources: _containers.MessageMap[str, _engine_pb2.Resource]
        json_schema: str
        resource_groups: _containers.MessageMap[str, TestFixtureGroup.Resources]
        def __init__(self, resources: _Optional[_Mapping[str, _engine_pb2.Resource]] = ..., json_schema: _Optional[str] = ..., resource_groups: _Optional[_Mapping[str, TestFixtureGroup.Resources]] = ...) -> None: ...
    class AuxData(_message.Message):
        __slots__ = ["aux_data", "json_schema"]
        class AuxDataEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _engine_pb2.AuxData
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_engine_pb2.AuxData, _Mapping]] = ...) -> None: ...
        AUX_DATA_FIELD_NUMBER: _ClassVar[int]
        JSON_SCHEMA_FIELD_NUMBER: _ClassVar[int]
        aux_data: _containers.MessageMap[str, _engine_pb2.AuxData]
        json_schema: str
        def __init__(self, aux_data: _Optional[_Mapping[str, _engine_pb2.AuxData]] = ..., json_schema: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class TestFixtureGroup(_message.Message):
    __slots__ = []
    class Principals(_message.Message):
        __slots__ = ["principals"]
        PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
        principals: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, principals: _Optional[_Iterable[str]] = ...) -> None: ...
    class Resources(_message.Message):
        __slots__ = ["resources"]
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        resources: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, resources: _Optional[_Iterable[str]] = ...) -> None: ...
    def __init__(self) -> None: ...

class TestOptions(_message.Message):
    __slots__ = ["now", "lenient_scope_search", "globals", "default_policy_version"]
    class GlobalsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    NOW_FIELD_NUMBER: _ClassVar[int]
    LENIENT_SCOPE_SEARCH_FIELD_NUMBER: _ClassVar[int]
    GLOBALS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    now: _timestamp_pb2.Timestamp
    lenient_scope_search: bool
    globals: _containers.MessageMap[str, _struct_pb2.Value]
    default_policy_version: str
    def __init__(self, now: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., lenient_scope_search: bool = ..., globals: _Optional[_Mapping[str, _struct_pb2.Value]] = ..., default_policy_version: _Optional[str] = ...) -> None: ...

class TestSuite(_message.Message):
    __slots__ = ["name", "description", "skip", "skip_reason", "tests", "principals", "resources", "aux_data", "options", "json_schema", "principal_groups", "resource_groups"]
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
    class AuxDataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _engine_pb2.AuxData
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_engine_pb2.AuxData, _Mapping]] = ...) -> None: ...
    class PrincipalGroupsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TestFixtureGroup.Principals
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TestFixtureGroup.Principals, _Mapping]] = ...) -> None: ...
    class ResourceGroupsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TestFixtureGroup.Resources
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TestFixtureGroup.Resources, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    SKIP_REASON_FIELD_NUMBER: _ClassVar[int]
    TESTS_FIELD_NUMBER: _ClassVar[int]
    PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    AUX_DATA_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    JSON_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_GROUPS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    skip: bool
    skip_reason: str
    tests: _containers.RepeatedCompositeFieldContainer[TestTable]
    principals: _containers.MessageMap[str, _engine_pb2.Principal]
    resources: _containers.MessageMap[str, _engine_pb2.Resource]
    aux_data: _containers.MessageMap[str, _engine_pb2.AuxData]
    options: TestOptions
    json_schema: str
    principal_groups: _containers.MessageMap[str, TestFixtureGroup.Principals]
    resource_groups: _containers.MessageMap[str, TestFixtureGroup.Resources]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., skip: bool = ..., skip_reason: _Optional[str] = ..., tests: _Optional[_Iterable[_Union[TestTable, _Mapping]]] = ..., principals: _Optional[_Mapping[str, _engine_pb2.Principal]] = ..., resources: _Optional[_Mapping[str, _engine_pb2.Resource]] = ..., aux_data: _Optional[_Mapping[str, _engine_pb2.AuxData]] = ..., options: _Optional[_Union[TestOptions, _Mapping]] = ..., json_schema: _Optional[str] = ..., principal_groups: _Optional[_Mapping[str, TestFixtureGroup.Principals]] = ..., resource_groups: _Optional[_Mapping[str, TestFixtureGroup.Resources]] = ...) -> None: ...

class TestTable(_message.Message):
    __slots__ = ["name", "description", "skip", "skip_reason", "input", "expected", "options"]
    class Input(_message.Message):
        __slots__ = ["principals", "resources", "actions", "aux_data", "principal_groups", "resource_groups"]
        PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        AUX_DATA_FIELD_NUMBER: _ClassVar[int]
        PRINCIPAL_GROUPS_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_GROUPS_FIELD_NUMBER: _ClassVar[int]
        principals: _containers.RepeatedScalarFieldContainer[str]
        resources: _containers.RepeatedScalarFieldContainer[str]
        actions: _containers.RepeatedScalarFieldContainer[str]
        aux_data: str
        principal_groups: _containers.RepeatedScalarFieldContainer[str]
        resource_groups: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, principals: _Optional[_Iterable[str]] = ..., resources: _Optional[_Iterable[str]] = ..., actions: _Optional[_Iterable[str]] = ..., aux_data: _Optional[str] = ..., principal_groups: _Optional[_Iterable[str]] = ..., resource_groups: _Optional[_Iterable[str]] = ...) -> None: ...
    class OutputExpectations(_message.Message):
        __slots__ = ["action", "expected"]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_FIELD_NUMBER: _ClassVar[int]
        action: str
        expected: _containers.RepeatedCompositeFieldContainer[_engine_pb2.OutputEntry]
        def __init__(self, action: _Optional[str] = ..., expected: _Optional[_Iterable[_Union[_engine_pb2.OutputEntry, _Mapping]]] = ...) -> None: ...
    class Expectation(_message.Message):
        __slots__ = ["principal", "resource", "actions", "outputs", "principals", "resources", "principal_groups", "resource_groups"]
        class ActionsEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _effect_pb2.Effect
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_effect_pb2.Effect, str]] = ...) -> None: ...
        PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        OUTPUTS_FIELD_NUMBER: _ClassVar[int]
        PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        PRINCIPAL_GROUPS_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_GROUPS_FIELD_NUMBER: _ClassVar[int]
        principal: str
        resource: str
        actions: _containers.ScalarMap[str, _effect_pb2.Effect]
        outputs: _containers.RepeatedCompositeFieldContainer[TestTable.OutputExpectations]
        principals: _containers.RepeatedScalarFieldContainer[str]
        resources: _containers.RepeatedScalarFieldContainer[str]
        principal_groups: _containers.RepeatedScalarFieldContainer[str]
        resource_groups: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, principal: _Optional[str] = ..., resource: _Optional[str] = ..., actions: _Optional[_Mapping[str, _effect_pb2.Effect]] = ..., outputs: _Optional[_Iterable[_Union[TestTable.OutputExpectations, _Mapping]]] = ..., principals: _Optional[_Iterable[str]] = ..., resources: _Optional[_Iterable[str]] = ..., principal_groups: _Optional[_Iterable[str]] = ..., resource_groups: _Optional[_Iterable[str]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    SKIP_REASON_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    skip: bool
    skip_reason: str
    input: TestTable.Input
    expected: _containers.RepeatedCompositeFieldContainer[TestTable.Expectation]
    options: TestOptions
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., skip: bool = ..., skip_reason: _Optional[str] = ..., input: _Optional[_Union[TestTable.Input, _Mapping]] = ..., expected: _Optional[_Iterable[_Union[TestTable.Expectation, _Mapping]]] = ..., options: _Optional[_Union[TestOptions, _Mapping]] = ...) -> None: ...

class Test(_message.Message):
    __slots__ = ["name", "description", "skip", "skip_reason", "input", "expected", "options", "expected_outputs"]
    class TestName(_message.Message):
        __slots__ = ["test_table_name", "principal_key", "resource_key"]
        TEST_TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
        PRINCIPAL_KEY_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_KEY_FIELD_NUMBER: _ClassVar[int]
        test_table_name: str
        principal_key: str
        resource_key: str
        def __init__(self, test_table_name: _Optional[str] = ..., principal_key: _Optional[str] = ..., resource_key: _Optional[str] = ...) -> None: ...
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
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    SKIP_REASON_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    name: Test.TestName
    description: str
    skip: bool
    skip_reason: str
    input: _engine_pb2.CheckInput
    expected: _containers.ScalarMap[str, _effect_pb2.Effect]
    options: TestOptions
    expected_outputs: _containers.MessageMap[str, Test.OutputEntries]
    def __init__(self, name: _Optional[_Union[Test.TestName, _Mapping]] = ..., description: _Optional[str] = ..., skip: bool = ..., skip_reason: _Optional[str] = ..., input: _Optional[_Union[_engine_pb2.CheckInput, _Mapping]] = ..., expected: _Optional[_Mapping[str, _effect_pb2.Effect]] = ..., options: _Optional[_Union[TestOptions, _Mapping]] = ..., expected_outputs: _Optional[_Mapping[str, Test.OutputEntries]] = ...) -> None: ...

class TestResults(_message.Message):
    __slots__ = ["suites", "summary"]
    class Result(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        RESULT_UNSPECIFIED: _ClassVar[TestResults.Result]
        RESULT_SKIPPED: _ClassVar[TestResults.Result]
        RESULT_PASSED: _ClassVar[TestResults.Result]
        RESULT_FAILED: _ClassVar[TestResults.Result]
        RESULT_ERRORED: _ClassVar[TestResults.Result]
    RESULT_UNSPECIFIED: TestResults.Result
    RESULT_SKIPPED: TestResults.Result
    RESULT_PASSED: TestResults.Result
    RESULT_FAILED: TestResults.Result
    RESULT_ERRORED: TestResults.Result
    class Tally(_message.Message):
        __slots__ = ["result", "count"]
        RESULT_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        result: TestResults.Result
        count: int
        def __init__(self, result: _Optional[_Union[TestResults.Result, str]] = ..., count: _Optional[int] = ...) -> None: ...
    class Summary(_message.Message):
        __slots__ = ["overall_result", "tests_count", "result_counts"]
        OVERALL_RESULT_FIELD_NUMBER: _ClassVar[int]
        TESTS_COUNT_FIELD_NUMBER: _ClassVar[int]
        RESULT_COUNTS_FIELD_NUMBER: _ClassVar[int]
        overall_result: TestResults.Result
        tests_count: int
        result_counts: _containers.RepeatedCompositeFieldContainer[TestResults.Tally]
        def __init__(self, overall_result: _Optional[_Union[TestResults.Result, str]] = ..., tests_count: _Optional[int] = ..., result_counts: _Optional[_Iterable[_Union[TestResults.Tally, _Mapping]]] = ...) -> None: ...
    class Suite(_message.Message):
        __slots__ = ["file", "name", "principals", "summary", "error", "test_cases", "description", "skip_reason"]
        FILE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
        SUMMARY_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        TEST_CASES_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        SKIP_REASON_FIELD_NUMBER: _ClassVar[int]
        file: str
        name: str
        principals: _containers.RepeatedCompositeFieldContainer[TestResults.Principal]
        summary: TestResults.Summary
        error: str
        test_cases: _containers.RepeatedCompositeFieldContainer[TestResults.TestCase]
        description: str
        skip_reason: str
        def __init__(self, file: _Optional[str] = ..., name: _Optional[str] = ..., principals: _Optional[_Iterable[_Union[TestResults.Principal, _Mapping]]] = ..., summary: _Optional[_Union[TestResults.Summary, _Mapping]] = ..., error: _Optional[str] = ..., test_cases: _Optional[_Iterable[_Union[TestResults.TestCase, _Mapping]]] = ..., description: _Optional[str] = ..., skip_reason: _Optional[str] = ...) -> None: ...
    class TestCase(_message.Message):
        __slots__ = ["name", "principals"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
        name: str
        principals: _containers.RepeatedCompositeFieldContainer[TestResults.Principal]
        def __init__(self, name: _Optional[str] = ..., principals: _Optional[_Iterable[_Union[TestResults.Principal, _Mapping]]] = ...) -> None: ...
    class Principal(_message.Message):
        __slots__ = ["name", "resources"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        name: str
        resources: _containers.RepeatedCompositeFieldContainer[TestResults.Resource]
        def __init__(self, name: _Optional[str] = ..., resources: _Optional[_Iterable[_Union[TestResults.Resource, _Mapping]]] = ...) -> None: ...
    class Resource(_message.Message):
        __slots__ = ["name", "actions"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        name: str
        actions: _containers.RepeatedCompositeFieldContainer[TestResults.Action]
        def __init__(self, name: _Optional[str] = ..., actions: _Optional[_Iterable[_Union[TestResults.Action, _Mapping]]] = ...) -> None: ...
    class Action(_message.Message):
        __slots__ = ["name", "details"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        name: str
        details: TestResults.Details
        def __init__(self, name: _Optional[str] = ..., details: _Optional[_Union[TestResults.Details, _Mapping]] = ...) -> None: ...
    class Details(_message.Message):
        __slots__ = ["result", "failure", "error", "success", "skip_reason", "engine_trace"]
        RESULT_FIELD_NUMBER: _ClassVar[int]
        FAILURE_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        SKIP_REASON_FIELD_NUMBER: _ClassVar[int]
        ENGINE_TRACE_FIELD_NUMBER: _ClassVar[int]
        result: TestResults.Result
        failure: TestResults.Failure
        error: str
        success: TestResults.Success
        skip_reason: str
        engine_trace: _containers.RepeatedCompositeFieldContainer[_engine_pb2.Trace]
        def __init__(self, result: _Optional[_Union[TestResults.Result, str]] = ..., failure: _Optional[_Union[TestResults.Failure, _Mapping]] = ..., error: _Optional[str] = ..., success: _Optional[_Union[TestResults.Success, _Mapping]] = ..., skip_reason: _Optional[str] = ..., engine_trace: _Optional[_Iterable[_Union[_engine_pb2.Trace, _Mapping]]] = ...) -> None: ...
    class OutputFailure(_message.Message):
        __slots__ = ["src", "mismatched", "missing"]
        class MismatchedValue(_message.Message):
            __slots__ = ["expected", "actual"]
            EXPECTED_FIELD_NUMBER: _ClassVar[int]
            ACTUAL_FIELD_NUMBER: _ClassVar[int]
            expected: _struct_pb2.Value
            actual: _struct_pb2.Value
            def __init__(self, expected: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., actual: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
        class MissingValue(_message.Message):
            __slots__ = ["expected"]
            EXPECTED_FIELD_NUMBER: _ClassVar[int]
            expected: _struct_pb2.Value
            def __init__(self, expected: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
        SRC_FIELD_NUMBER: _ClassVar[int]
        MISMATCHED_FIELD_NUMBER: _ClassVar[int]
        MISSING_FIELD_NUMBER: _ClassVar[int]
        src: str
        mismatched: TestResults.OutputFailure.MismatchedValue
        missing: TestResults.OutputFailure.MissingValue
        def __init__(self, src: _Optional[str] = ..., mismatched: _Optional[_Union[TestResults.OutputFailure.MismatchedValue, _Mapping]] = ..., missing: _Optional[_Union[TestResults.OutputFailure.MissingValue, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ["expected", "actual", "outputs"]
        EXPECTED_FIELD_NUMBER: _ClassVar[int]
        ACTUAL_FIELD_NUMBER: _ClassVar[int]
        OUTPUTS_FIELD_NUMBER: _ClassVar[int]
        expected: _effect_pb2.Effect
        actual: _effect_pb2.Effect
        outputs: _containers.RepeatedCompositeFieldContainer[TestResults.OutputFailure]
        def __init__(self, expected: _Optional[_Union[_effect_pb2.Effect, str]] = ..., actual: _Optional[_Union[_effect_pb2.Effect, str]] = ..., outputs: _Optional[_Iterable[_Union[TestResults.OutputFailure, _Mapping]]] = ...) -> None: ...
    class Success(_message.Message):
        __slots__ = ["effect", "outputs"]
        EFFECT_FIELD_NUMBER: _ClassVar[int]
        OUTPUTS_FIELD_NUMBER: _ClassVar[int]
        effect: _effect_pb2.Effect
        outputs: _containers.RepeatedCompositeFieldContainer[_engine_pb2.OutputEntry]
        def __init__(self, effect: _Optional[_Union[_effect_pb2.Effect, str]] = ..., outputs: _Optional[_Iterable[_Union[_engine_pb2.OutputEntry, _Mapping]]] = ...) -> None: ...
    SUITES_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    suites: _containers.RepeatedCompositeFieldContainer[TestResults.Suite]
    summary: TestResults.Summary
    def __init__(self, suites: _Optional[_Iterable[_Union[TestResults.Suite, _Mapping]]] = ..., summary: _Optional[_Union[TestResults.Summary, _Mapping]] = ...) -> None: ...
