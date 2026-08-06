import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientCredentials(_message.Message):
    __slots__ = ("client_id", "client_secret")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    client_secret: str
    def __init__(self, client_id: _Optional[str] = ..., client_secret: _Optional[str] = ...) -> None: ...

class DeviceToken(_message.Message):
    __slots__ = ("access_token", "refresh_token", "expires_at", "token_type")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    refresh_token: str
    expires_at: _timestamp_pb2.Timestamp
    token_type: str
    def __init__(self, access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., token_type: _Optional[str] = ...) -> None: ...

class SavedCredentials(_message.Message):
    __slots__ = ("api_endpoint", "client_credentials", "device_token")
    API_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    api_endpoint: str
    client_credentials: ClientCredentials
    device_token: DeviceToken
    def __init__(self, api_endpoint: _Optional[str] = ..., client_credentials: _Optional[_Union[ClientCredentials, _Mapping]] = ..., device_token: _Optional[_Union[DeviceToken, _Mapping]] = ...) -> None: ...
