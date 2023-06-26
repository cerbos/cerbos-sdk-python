from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Event(_message.Message):
    __slots__ = ["api_activity"]
    class ApiActivity(_message.Message):
        __slots__ = ["method_calls", "uptime", "user_agents", "version"]
        METHOD_CALLS_FIELD_NUMBER: _ClassVar[int]
        UPTIME_FIELD_NUMBER: _ClassVar[int]
        USER_AGENTS_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        method_calls: _containers.RepeatedCompositeFieldContainer[Event.CountStat]
        uptime: _duration_pb2.Duration
        user_agents: _containers.RepeatedCompositeFieldContainer[Event.CountStat]
        version: str
        def __init__(self, version: _Optional[str] = ..., uptime: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., method_calls: _Optional[_Iterable[_Union[Event.CountStat, _Mapping]]] = ..., user_agents: _Optional[_Iterable[_Union[Event.CountStat, _Mapping]]] = ...) -> None: ...
    class CountStat(_message.Message):
        __slots__ = ["count", "key"]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        count: int
        key: str
        def __init__(self, key: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...
    API_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    api_activity: Event.ApiActivity
    def __init__(self, api_activity: _Optional[_Union[Event.ApiActivity, _Mapping]] = ...) -> None: ...

class ServerLaunch(_message.Message):
    __slots__ = ["features", "source", "stats", "version"]
    class Cerbos(_message.Message):
        __slots__ = ["build_date", "commit", "module_checksum", "module_version", "version"]
        BUILD_DATE_FIELD_NUMBER: _ClassVar[int]
        COMMIT_FIELD_NUMBER: _ClassVar[int]
        MODULE_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
        MODULE_VERSION_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        build_date: str
        commit: str
        module_checksum: str
        module_version: str
        version: str
        def __init__(self, version: _Optional[str] = ..., commit: _Optional[str] = ..., build_date: _Optional[str] = ..., module_version: _Optional[str] = ..., module_checksum: _Optional[str] = ...) -> None: ...
    class Features(_message.Message):
        __slots__ = ["admin_api", "audit", "schema", "storage"]
        class AdminApi(_message.Message):
            __slots__ = ["enabled"]
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            enabled: bool
            def __init__(self, enabled: bool = ...) -> None: ...
        class Audit(_message.Message):
            __slots__ = ["backend", "enabled"]
            BACKEND_FIELD_NUMBER: _ClassVar[int]
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            backend: str
            enabled: bool
            def __init__(self, enabled: bool = ..., backend: _Optional[str] = ...) -> None: ...
        class Schema(_message.Message):
            __slots__ = ["enforcement"]
            ENFORCEMENT_FIELD_NUMBER: _ClassVar[int]
            enforcement: str
            def __init__(self, enforcement: _Optional[str] = ...) -> None: ...
        class Storage(_message.Message):
            __slots__ = ["blob", "bundle", "disk", "driver", "git"]
            class Blob(_message.Message):
                __slots__ = ["poll_interval", "provider"]
                POLL_INTERVAL_FIELD_NUMBER: _ClassVar[int]
                PROVIDER_FIELD_NUMBER: _ClassVar[int]
                poll_interval: _duration_pb2.Duration
                provider: str
                def __init__(self, provider: _Optional[str] = ..., poll_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
            class Bundle(_message.Message):
                __slots__ = ["bundle_source", "client_id", "pdp_id"]
                BUNDLE_SOURCE_FIELD_NUMBER: _ClassVar[int]
                CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
                PDP_ID_FIELD_NUMBER: _ClassVar[int]
                bundle_source: str
                client_id: str
                pdp_id: str
                def __init__(self, pdp_id: _Optional[str] = ..., bundle_source: _Optional[str] = ..., client_id: _Optional[str] = ...) -> None: ...
            class Disk(_message.Message):
                __slots__ = ["watch"]
                WATCH_FIELD_NUMBER: _ClassVar[int]
                watch: bool
                def __init__(self, watch: bool = ...) -> None: ...
            class Git(_message.Message):
                __slots__ = ["auth", "poll_interval", "protocol"]
                AUTH_FIELD_NUMBER: _ClassVar[int]
                POLL_INTERVAL_FIELD_NUMBER: _ClassVar[int]
                PROTOCOL_FIELD_NUMBER: _ClassVar[int]
                auth: bool
                poll_interval: _duration_pb2.Duration
                protocol: str
                def __init__(self, protocol: _Optional[str] = ..., auth: bool = ..., poll_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
            BLOB_FIELD_NUMBER: _ClassVar[int]
            BUNDLE_FIELD_NUMBER: _ClassVar[int]
            DISK_FIELD_NUMBER: _ClassVar[int]
            DRIVER_FIELD_NUMBER: _ClassVar[int]
            GIT_FIELD_NUMBER: _ClassVar[int]
            blob: ServerLaunch.Features.Storage.Blob
            bundle: ServerLaunch.Features.Storage.Bundle
            disk: ServerLaunch.Features.Storage.Disk
            driver: str
            git: ServerLaunch.Features.Storage.Git
            def __init__(self, driver: _Optional[str] = ..., disk: _Optional[_Union[ServerLaunch.Features.Storage.Disk, _Mapping]] = ..., git: _Optional[_Union[ServerLaunch.Features.Storage.Git, _Mapping]] = ..., blob: _Optional[_Union[ServerLaunch.Features.Storage.Blob, _Mapping]] = ..., bundle: _Optional[_Union[ServerLaunch.Features.Storage.Bundle, _Mapping]] = ...) -> None: ...
        ADMIN_API_FIELD_NUMBER: _ClassVar[int]
        AUDIT_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_FIELD_NUMBER: _ClassVar[int]
        STORAGE_FIELD_NUMBER: _ClassVar[int]
        admin_api: ServerLaunch.Features.AdminApi
        audit: ServerLaunch.Features.Audit
        schema: ServerLaunch.Features.Schema
        storage: ServerLaunch.Features.Storage
        def __init__(self, audit: _Optional[_Union[ServerLaunch.Features.Audit, _Mapping]] = ..., schema: _Optional[_Union[ServerLaunch.Features.Schema, _Mapping]] = ..., admin_api: _Optional[_Union[ServerLaunch.Features.AdminApi, _Mapping]] = ..., storage: _Optional[_Union[ServerLaunch.Features.Storage, _Mapping]] = ...) -> None: ...
    class Source(_message.Message):
        __slots__ = ["arch", "cerbos", "num_cpus", "os"]
        ARCH_FIELD_NUMBER: _ClassVar[int]
        CERBOS_FIELD_NUMBER: _ClassVar[int]
        NUM_CPUS_FIELD_NUMBER: _ClassVar[int]
        OS_FIELD_NUMBER: _ClassVar[int]
        arch: str
        cerbos: ServerLaunch.Cerbos
        num_cpus: int
        os: str
        def __init__(self, cerbos: _Optional[_Union[ServerLaunch.Cerbos, _Mapping]] = ..., os: _Optional[str] = ..., arch: _Optional[str] = ..., num_cpus: _Optional[int] = ...) -> None: ...
    class Stats(_message.Message):
        __slots__ = ["policy", "schema"]
        class Policy(_message.Message):
            __slots__ = ["avg_condition_count", "avg_rule_count", "count"]
            class AvgConditionCountEntry(_message.Message):
                __slots__ = ["key", "value"]
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: float
                def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
            class AvgRuleCountEntry(_message.Message):
                __slots__ = ["key", "value"]
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: float
                def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
            class CountEntry(_message.Message):
                __slots__ = ["key", "value"]
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: int
                def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
            AVG_CONDITION_COUNT_FIELD_NUMBER: _ClassVar[int]
            AVG_RULE_COUNT_FIELD_NUMBER: _ClassVar[int]
            COUNT_FIELD_NUMBER: _ClassVar[int]
            avg_condition_count: _containers.ScalarMap[str, float]
            avg_rule_count: _containers.ScalarMap[str, float]
            count: _containers.ScalarMap[str, int]
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
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    features: ServerLaunch.Features
    source: ServerLaunch.Source
    stats: ServerLaunch.Stats
    version: str
    def __init__(self, version: _Optional[str] = ..., source: _Optional[_Union[ServerLaunch.Source, _Mapping]] = ..., features: _Optional[_Union[ServerLaunch.Features, _Mapping]] = ..., stats: _Optional[_Union[ServerLaunch.Stats, _Mapping]] = ...) -> None: ...

class ServerStop(_message.Message):
    __slots__ = ["requests_total", "uptime", "version"]
    REQUESTS_TOTAL_FIELD_NUMBER: _ClassVar[int]
    UPTIME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    requests_total: int
    uptime: _duration_pb2.Duration
    version: str
    def __init__(self, version: _Optional[str] = ..., uptime: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., requests_total: _Optional[int] = ...) -> None: ...
