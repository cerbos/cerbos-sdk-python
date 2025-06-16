from buf.validate import validate_pb2 as _validate_pb2
from cerbos.cloud.pdp.v1 import pdp_pb2 as _pdp_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Source(_message.Message):
    __slots__ = ["deployment_id", "playground_id"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYGROUND_ID_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    playground_id: str
    def __init__(self, deployment_id: _Optional[str] = ..., playground_id: _Optional[str] = ...) -> None: ...

class BundleInfo(_message.Message):
    __slots__ = ["source", "input_hash", "output_hash", "encryption_key", "segments"]
    class Segment(_message.Message):
        __slots__ = ["segment_id", "checksum", "download_urls"]
        SEGMENT_ID_FIELD_NUMBER: _ClassVar[int]
        CHECKSUM_FIELD_NUMBER: _ClassVar[int]
        DOWNLOAD_URLS_FIELD_NUMBER: _ClassVar[int]
        segment_id: int
        checksum: bytes
        download_urls: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, segment_id: _Optional[int] = ..., checksum: _Optional[bytes] = ..., download_urls: _Optional[_Iterable[str]] = ...) -> None: ...
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    INPUT_HASH_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_HASH_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    source: Source
    input_hash: bytes
    output_hash: bytes
    encryption_key: bytes
    segments: _containers.RepeatedCompositeFieldContainer[BundleInfo.Segment]
    def __init__(self, source: _Optional[_Union[Source, _Mapping]] = ..., input_hash: _Optional[bytes] = ..., output_hash: _Optional[bytes] = ..., encryption_key: _Optional[bytes] = ..., segments: _Optional[_Iterable[_Union[BundleInfo.Segment, _Mapping]]] = ...) -> None: ...

class Meta(_message.Message):
    __slots__ = ["bundle_id", "source"]
    BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    bundle_id: str
    source: str
    def __init__(self, bundle_id: _Optional[str] = ..., source: _Optional[str] = ...) -> None: ...

class Manifest(_message.Message):
    __slots__ = ["api_version", "policy_index", "schemas", "meta"]
    class PolicyIndexEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    POLICY_INDEX_FIELD_NUMBER: _ClassVar[int]
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    api_version: str
    policy_index: _containers.ScalarMap[str, str]
    schemas: _containers.RepeatedScalarFieldContainer[str]
    meta: Meta
    def __init__(self, api_version: _Optional[str] = ..., policy_index: _Optional[_Mapping[str, str]] = ..., schemas: _Optional[_Iterable[str]] = ..., meta: _Optional[_Union[Meta, _Mapping]] = ...) -> None: ...

class GetBundleRequest(_message.Message):
    __slots__ = ["pdp_id", "source"]
    PDP_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    pdp_id: _pdp_pb2.Identifier
    source: Source
    def __init__(self, pdp_id: _Optional[_Union[_pdp_pb2.Identifier, _Mapping]] = ..., source: _Optional[_Union[Source, _Mapping]] = ...) -> None: ...

class GetBundleResponse(_message.Message):
    __slots__ = ["bundle_info"]
    BUNDLE_INFO_FIELD_NUMBER: _ClassVar[int]
    bundle_info: BundleInfo
    def __init__(self, bundle_info: _Optional[_Union[BundleInfo, _Mapping]] = ...) -> None: ...

class WatchBundleRequest(_message.Message):
    __slots__ = ["pdp_id", "start", "heartbeat"]
    class Start(_message.Message):
        __slots__ = ["source"]
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        source: Source
        def __init__(self, source: _Optional[_Union[Source, _Mapping]] = ...) -> None: ...
    class Heartbeat(_message.Message):
        __slots__ = ["timestamp", "active_bundle_id"]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
        timestamp: _timestamp_pb2.Timestamp
        active_bundle_id: str
        def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., active_bundle_id: _Optional[str] = ...) -> None: ...
    PDP_ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    pdp_id: _pdp_pb2.Identifier
    start: WatchBundleRequest.Start
    heartbeat: WatchBundleRequest.Heartbeat
    def __init__(self, pdp_id: _Optional[_Union[_pdp_pb2.Identifier, _Mapping]] = ..., start: _Optional[_Union[WatchBundleRequest.Start, _Mapping]] = ..., heartbeat: _Optional[_Union[WatchBundleRequest.Heartbeat, _Mapping]] = ...) -> None: ...

class WatchBundleResponse(_message.Message):
    __slots__ = ["bundle_update", "reconnect", "bundle_removed"]
    class Reconnect(_message.Message):
        __slots__ = ["backoff", "reason"]
        BACKOFF_FIELD_NUMBER: _ClassVar[int]
        REASON_FIELD_NUMBER: _ClassVar[int]
        backoff: _duration_pb2.Duration
        reason: str
        def __init__(self, backoff: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., reason: _Optional[str] = ...) -> None: ...
    class BundleRemoved(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    BUNDLE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    RECONNECT_FIELD_NUMBER: _ClassVar[int]
    BUNDLE_REMOVED_FIELD_NUMBER: _ClassVar[int]
    bundle_update: BundleInfo
    reconnect: WatchBundleResponse.Reconnect
    bundle_removed: WatchBundleResponse.BundleRemoved
    def __init__(self, bundle_update: _Optional[_Union[BundleInfo, _Mapping]] = ..., reconnect: _Optional[_Union[WatchBundleResponse.Reconnect, _Mapping]] = ..., bundle_removed: _Optional[_Union[WatchBundleResponse.BundleRemoved, _Mapping]] = ...) -> None: ...
