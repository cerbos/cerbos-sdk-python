# Copyright 2021-2025 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0
import threading
import os
from datetime import datetime, timedelta
from typing import Optional
import grpc
from google.rpc import code_pb2
from grpc_status import rpc_status
from cerbos.cloud.apikey.v1 import apikey_pb2, apikey_pb2_grpc
from cerbos.sdk.hub.model import Credentials

class InvalidCredentialsError(Exception):
    pass

class _AuthClient:
    _EARLY_EXPIRY: timedelta = timedelta(minutes=5)
    _client: apikey_pb2_grpc.ApiKeyServiceStub
    _client_id: str
    _client_secret: str
    _timeout_secs: float
    _expiry: datetime
    _lock: threading.Lock
    _token: Optional[str] = None
    _invalid_credentials: bool = False

    def __init__(self, channel: grpc.Channel, timeout_secs: float, credentials: Optional[Credentials]=None):
        self._client_id = os.environ['CERBOS_HUB_CLIENT_ID']
        self._client_secret = os.environ['CERBOS_HUB_CLIENT_SECRET']
        if credentials:
            if credentials.client_id != '':
                self._client_id = credentials.client_id
            if credentials.client_secret != '':
                self._client_secret = credentials.client_secret
        self._client = apikey_pb2_grpc.ApiKeyServiceStub(channel)
        self._timeout_secs = timeout_secs
        self._lock = threading.Lock()

    def authenticate(self) -> str:
        with self._lock:
            if self._invalid_credentials:
                raise InvalidCredentialsError('Invalid credentials')
            if self._token and self._expiry > datetime.now():
                return self._token
            req = apikey_pb2.IssueAccessTokenRequest(client_id=self._client_id, client_secret=self._client_secret)
            try:
                resp: apikey_pb2.IssueAccessTokenResponse = self._client.IssueAccessToken(req, timeout=self._timeout_secs)
                self._token = resp.access_token
                expires_in = resp.expires_in.ToTimedelta()
                if expires_in > self._EARLY_EXPIRY:
                    expires_in = expires_in - self._EARLY_EXPIRY
                self._expiry = datetime.now() + expires_in
                return self._token
            except grpc.RpcError as rpc_error:
                status = rpc_status.from_call(rpc_error)
                if status and status.code == code_pb2.UNAUTHENTICATED:
                    self._invalid_credentials = True
                    raise InvalidCredentialsError('Invalid credentials')
                raise rpc_error