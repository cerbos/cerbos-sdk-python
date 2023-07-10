from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServerLaunch(_message.Message):
    __slots__ = ["version", "source", "features", "stats"]
    class Cerbos(_message.Message):
        __slots__ = ["version", "commit", "build_date", "module_version", "module_checksum"]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        COMMIT_FIELD_NUMBER: _ClassVar[int]
        BUILD_DATE_FIELD_NUMBER: _ClassVar[int]
        MODULE_VERSION_FIELD_NUMBER: _ClassVar[int]
        MODULE_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
        version: str
        commit: str
        build_date: str
        module_version: str
        module_checksum: str
        def __init__(self, version: _Optional[str] = ..., commit: _Optional[str] = ..., build_date: _Optional[str] = ..., module_version: _Optional[str] = ..., module_checksum: _Optional[str] = ...) -> None: ...
    class Source(_message.Message):
        __slots__ = ["cerbos", "os", "arch", "num_cpus"]
        CERBOS_FIELD_NUMBER: _ClassVar[int]
        OS_FIELD_NUMBER: _ClassVar[int]
        ARCH_FIELD_NUMBER: _ClassVar[int]
        NUM_CPUS_FIELD_NUMBER: _ClassVar[int]
        cerbos: ServerLaunch.Cerbos
        os: str
        arch: str
        num_cpus: int
        def __init__(self, cerbos: _Optional[_Union[ServerLaunch.Cerbos, _Mapping]] = ..., os: _Optional[str] = ..., arch: _Optional[str] = ..., num_cpus: _Optional[int] = ...) -> None: ...
    class Features(_message.Message):
        __slots__ = ["audit", "schema", "admin_api", "storage"]
        class Audit(_message.Message):
            __slots__ = ["enabled", "backend"]
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            BACKEND_FIELD_NUMBER: _ClassVar[int]
            enabled: bool
            backend: str
            def __init__(self, enabled: bool = ..., backend: _Optional[str] = ...) -> None: ...
        class Schema(_message.Message):
            __slots__ = ["enforcement"]
            ENFORCEMENT_FIELD_NUMBER: _ClassVar[int]
            enforcement: str
            def __init__(self, enforcement: _Optional[str] = ...) -> None: ...
        class AdminApi(_message.Message):
            __slots__ = ["enabled"]
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            enabled: bool
            def __init__(self, enabled: bool = ...) -> None: ...
        class Storage(_message.Message):
            __slots__ = ["driver", "disk", "git", "blob", "bundle"]
            class Disk(_message.Message):
                __slots__ = ["watch"]
                WATCH_FIELD_NUMBER: _ClassVar[int]
                watch: bool
                def __init__(self, watch: bool = ...) -> None: ...
            class Git(_message.Message):
                __slots__ = ["protocol", "auth", "poll_interval"]
                PROTOCOL_FIELD_NUMBER: _ClassVar[int]
                AUTH_FIELD_NUMBER: _ClassVar[int]
                POLL_INTERVAL_FIELD_NUMBER: _ClassVar[int]
                protocol: str
                auth: bool
                poll_interval: _duration_pb2.Duration
                def __init__(self, protocol: _Optional[str] = ..., auth: bool = ..., poll_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
            class Blob(_message.Message):
                __slots__ = ["provider", "poll_interval"]
                PROVIDER_FIELD_NUMBER: _ClassVar[int]
                POLL_INTERVAL_FIELD_NUMBER: _ClassVar[int]
                provider: str
                poll_interval: _duration_pb2.Duration
                def __init__(self, provider: _Optional[str] = ..., poll_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
            class Bundle(_message.Message):
                __slots__ = ["pdp_id", "bundle_source", "client_id"]
                PDP_ID_FIELD_NUMBER: _ClassVar[int]
                BUNDLE_SOURCE_FIELD_NUMBER: _ClassVar[int]
                CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
                pdp_id: str
                bundle_source: str
                client_id: str
                def __init__(self, pdp_id: _Optional[str] = ..., bundle_source: _Optional[str] = ..., client_id: _Optional[str] = ...) -> None: ...
            DRIVER_FIELD_NUMBER: _ClassVar[int]
            DISK_FIELD_NUMBER: _ClassVar[int]
            GIT_FIELD_NUMBER: _ClassVar[int]
            BLOB_FIELD_NUMBER: _ClassVar[int]
            BUNDLE_FIELD_NUMBER: _ClassVar[int]
            driver: str
            disk: ServerLaunch.Features.Storage.Disk
            git: ServerLaunch.Features.Storage.Git
            blob: ServerLaunch.Features.Storage.Blob
            bundle: ServerLaunch.Features.Storage.Bundle
            def __init__(self, driver: _Optional[str] = ..., disk: _Optional[_Union[ServerLaunch.Features.Storage.Disk, _Mapping]] = ..., git: _Optional[_Union[ServerLaunch.Features.Storage.Git, _Mapping]] = ..., blob: _Optional[_Union[ServerLaunch.Features.Storage.Blob, _Mapping]] = ..., bundle: _Optional[_Union[ServerLaunch.Features.Storage.Bundle, _Mapping]] = ...) -> None: ...
        AUDIT_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_FIELD_NUMBER: _ClassVar[int]
        ADMIN_API_FIELD_NUMBER: _ClassVar[int]
        STORAGE_FIELD_NUMBER: _ClassVar[int]
        audit: ServerLaunch.Features.Audit
        schema: ServerLaunch.Features.Schema
        admin_api: ServerLaunch.Features.AdminApi
        storage: ServerLaunch.Features.Storage
        def __init__(self, audit: _Optional[_Union[ServerLaunch.Features.Audit, _Mapping]] = ..., schema: _Optional[_Union[ServerLaunch.Features.Schema, _Mapping]] = ..., admin_api: _Optional[_Union[ServerLaunch.Features.AdminApi, _Mapping]] = ..., storage: _Optional[_Union[ServerLaunch.Features.Storage, _Mapping]] = ...) -> None: ...
    class Stats(_message.Message):
        __slots__ = ["policy", "schema"]
        class Policy(_message.Message):
            __slots__ = ["count", "avg_rule_count", "avg_condition_count"]
            class CountEntry(_message.Message):
                __slots__ = ["key", "value"]
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: int
                def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
            class AvgRuleCountEntry(_message.Message):
                __slots__ = ["key", "value"]
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: float
                def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
            class AvgConditionCountEntry(_message.Message):
                __slots__ = ["key", "value"]
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: float
                def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
            COUNT_FIELD_NUMBER: _ClassVar[int]
            AVG_RULE_COUNT_FIELD_NUMBER: _ClassVar[int]
            AVG_CONDITION_COUNT_FIELD_NUMBER: _ClassVar[int]
            count: _containers.ScalarMap[str, int]
            avg_rule_count: _containers.ScalarMap[str, float]
            avg_condition_count: _containers.ScalarMap[str, float]
            def __init__(self, count: _Optional[_Mapping[str, int]] = ..., avg_rule_count: _Optional[_Mapping[str, float]] = ..., avg_condition_count: _Optional[_Mapping[str, float]] = ...) -> None: ...
        class Schema(_message.Message):
            __slots__ = ["count"]
            COUNT_FIELD_NUMBER: _ClassVar[int]
            count: int
            def __init__(self, count: _Optional[int] = ...) -> None: ...
        POLICY_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_FIELD_NUMBER: _ClassVar[int]
        policy: ServerLaunch.Stats.Policy
        schema: ServerLaunch.Stats.Schema
        def __init__(self, policy: _Optional[_Union[ServerLaunch.Stats.Policy, _Mapping]] = ..., schema: _Optional[_Union[ServerLaunch.Stats.Schema, _Mapping]] = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    version: str
    source: ServerLaunch.Source
    features: ServerLaunch.Features
    stats: ServerLaunch.Stats
    def __init__(self, version: _Optional[str] = ..., source: _Optional[_Union[ServerLaunch.Source, _Mapping]] = ..., features: _Optional[_Union[ServerLaunch.Features, _Mapping]] = ..., stats: _Optional[_Union[ServerLaunch.Stats, _Mapping]] = ...) -> None: ...

class ServerStop(_message.Message):
    __slots__ = ["version", "uptime", "requests_total"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    UPTIME_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_TOTAL_FIELD_NUMBER: _ClassVar[int]
    version: str
    uptime: _duration_pb2.Duration
    requests_total: int
    def __init__(self, version: _Optional[str] = ..., uptime: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., requests_total: _Optional[int] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ["api_activity"]
    class CountStat(_message.Message):
        __slots__ = ["key", "count"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        key: str
        count: int
        def __init__(self, key: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...
    class ApiActivity(_message.Message):
        __slots__ = ["version", "uptime", "method_calls", "user_agents"]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        UPTIME_FIELD_NUMBER: _ClassVar[int]
        METHOD_CALLS_FIELD_NUMBER: _ClassVar[int]
        USER_AGENTS_FIELD_NUMBER: _ClassVar[int]
        version: str
        uptime: _duration_pb2.Duration
        method_calls: _containers.RepeatedCompositeFieldContainer[Event.CountStat]
        user_agents: _containers.RepeatedCompositeFieldContainer[Event.CountStat]
        def __init__(self, version: _Optional[str] = ..., uptime: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., method_calls: _Optional[_Iterable[_Union[Event.CountStat, _Mapping]]] = ..., user_agents: _Optional[_Iterable[_Union[Event.CountStat, _Mapping]]] = ...) -> None: ...
    API_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    api_activity: Event.ApiActivity
    def __init__(self, api_activity: _Optional[_Union[Event.ApiActivity, _Mapping]] = ...) -> None: ...
