import datetime

from buf.validate import validate_pb2 as _validate_pb2
from cerbos.cloud.auth.v1 import auth_pb2 as _auth_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IssueAccessTokenRequest(_message.Message):
    __slots__ = ("client_id", "client_secret")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    client_secret: str
    def __init__(self, client_id: _Optional[str] = ..., client_secret: _Optional[str] = ...) -> None: ...

class IssueAccessTokenResponse(_message.Message):
    __slots__ = ("access_token", "expires_in")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    expires_in: _duration_pb2.Duration
    def __init__(self, access_token: _Optional[str] = ..., expires_in: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class RegisterDeviceRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RegisterDeviceResponse(_message.Message):
    __slots__ = ("verification_url", "device_token")
    VERIFICATION_URL_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    verification_url: str
    device_token: _auth_pb2.DeviceToken
    def __init__(self, verification_url: _Optional[str] = ..., device_token: _Optional[_Union[_auth_pb2.DeviceToken, _Mapping]] = ...) -> None: ...

class RefreshDeviceTokenRequest(_message.Message):
    __slots__ = ("device_token",)
    DEVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    device_token: _auth_pb2.DeviceToken
    def __init__(self, device_token: _Optional[_Union[_auth_pb2.DeviceToken, _Mapping]] = ...) -> None: ...

class RefreshDeviceTokenResponse(_message.Message):
    __slots__ = ("device_token",)
    DEVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    device_token: _auth_pb2.DeviceToken
    def __init__(self, device_token: _Optional[_Union[_auth_pb2.DeviceToken, _Mapping]] = ...) -> None: ...
