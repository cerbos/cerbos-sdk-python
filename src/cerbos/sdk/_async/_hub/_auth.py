# Copyright 2021-2025 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import asyncio
import os
from datetime import datetime, timedelta
from typing import Any, Callable, List, NamedTuple, Optional, Union

import grpc
from google.rpc import code_pb2
from grpc_status import rpc_status

from cerbos.cloud.apikey.v1 import apikey_pb2, apikey_pb2_grpc
from cerbos.sdk.hub.model import Credentials


class InvalidCredentialsError(Exception):
    pass


class _AsyncAuthClient:
    _EARLY_EXPIRY: timedelta = timedelta(minutes=5)
    _client: apikey_pb2_grpc.ApiKeyServiceStub
    _client_id: str
    _client_secret: str
    _timeout_secs: float
    _expiry: datetime
    _lock: asyncio.Lock
    _token: Optional[str] = None
    _invalid_credentials: bool = False

    def __init__(
        self,
        channel: grpc.aio.Channel,
        timeout_secs: float,
        credentials: Optional[Credentials] = None,
    ):
        self._client_id = os.environ["CERBOS_HUB_CLIENT_ID"]
        self._client_secret = os.environ["CERBOS_HUB_CLIENT_SECRET"]
        if credentials:
            if credentials.client_id != "":
                self._client_id = credentials.client_id

            if credentials.client_secret != "":
                self._client_secret = credentials.client_secret

        self._client = apikey_pb2_grpc.ApiKeyServiceStub(channel)
        self._timeout_secs = timeout_secs
        self._lock = asyncio.Lock()

    async def authenticate(self) -> str:
        async with self._lock:
            if self._invalid_credentials:
                raise InvalidCredentialsError("Invalid credentials")

            if self._token and self._expiry > datetime.now():
                return self._token

            req = apikey_pb2.IssueAccessTokenRequest(
                client_id=self._client_id, client_secret=self._client_secret
            )
            try:
                resp: apikey_pb2.IssueAccessTokenResponse = (
                    await self._client.IssueAccessToken(req, timeout=self._timeout_secs)
                )
                self._token = resp.access_token
                expires_in = resp.expires_in.ToTimedelta()
                if expires_in > self._EARLY_EXPIRY:
                    expires_in = expires_in - self._EARLY_EXPIRY

                self._expiry = datetime.now() + expires_in
                return self._token
            except grpc.aio.AioRpcError as rpc_error:
                status = rpc_status.from_call(rpc_error)
                if status and status.code == code_pb2.UNAUTHENTICATED:
                    self._invalid_credentials = True
                    raise InvalidCredentialsError("Invalid credentials")

                raise rpc_error


class _AsyncClientCallDetails(NamedTuple):
    method: str
    timeout: Optional[float]
    metadata: Optional[grpc.aio.Metadata]
    credentials: Optional[grpc.CallCredentials]
    wait_for_ready: Optional[bool]


class _AsyncClientCallDetailsWrapper(
    _AsyncClientCallDetails, grpc.aio.ClientCallDetails
):
    pass


class _AsyncAuthInterceptor(
    grpc.aio.UnaryUnaryClientInterceptor,
    grpc.aio.UnaryStreamClientInterceptor,
    grpc.aio.StreamUnaryClientInterceptor,
    grpc.aio.StreamStreamClientInterceptor,
):
    _auth_client: _AsyncAuthClient

    def __init__(
        self,
        auth_client: _AsyncAuthClient,
    ):
        self._auth_client = auth_client

    async def _intercept(
        self,
        continuation: Callable[..., Any],
        client_call_details: grpc.aio.ClientCallDetails,
        request: Any,
    ):
        token = await self._auth_client.authenticate()
        metadata = client_call_details.metadata or grpc.aio.Metadata()
        metadata.add("x-cerbos-auth", token)
        new_client_call_details = _AsyncClientCallDetailsWrapper(
            client_call_details.method,
            client_call_details.timeout,
            metadata,
            client_call_details.credentials,
            client_call_details.wait_for_ready,
        )
        return await continuation(new_client_call_details, request)

    async def intercept_unary_unary(
        self,
        continuation: Callable[
            [grpc.aio.ClientCallDetails, grpc.aio._typing.RequestType],
            grpc.aio.UnaryUnaryCall,
        ],
        client_call_details: grpc.aio.ClientCallDetails,
        request: grpc.aio._typing.RequestType,
    ) -> Union[grpc.aio.UnaryUnaryCall, object]:
        return await self._intercept(continuation, client_call_details, request)

    async def intercept_unary_stream(
        self,
        continuation: Callable[
            [grpc.aio.ClientCallDetails, grpc.aio._typing.RequestType],
            grpc.aio.UnaryStreamCall,
        ],
        client_call_details: grpc.aio.ClientCallDetails,
        request: grpc.aio._typing.RequestType,
    ) -> Union[grpc.aio._typing.ResponseIterableType, grpc.aio.UnaryStreamCall]:
        return await self._intercept(continuation, client_call_details, request)

    async def intercept_stream_unary(
        self,
        continuation: Callable[
            [grpc.aio.ClientCallDetails, grpc.aio._typing.RequestType],
            grpc.aio.StreamUnaryCall,
        ],
        client_call_details: grpc.aio.ClientCallDetails,
        request_iterator: grpc.aio._typing.RequestIterableType,
    ) -> grpc.aio._call.StreamUnaryCall:
        return await self._intercept(
            continuation, client_call_details, request_iterator
        )

    async def intercept_stream_stream(
        self,
        continuation: Callable[
            [grpc.aio.ClientCallDetails, grpc.aio._typing.RequestType],
            grpc.aio.StreamStreamCall,
        ],
        client_call_details: grpc.aio.ClientCallDetails,
        request_iterator: grpc.aio._typing.RequestIterableType,
    ) -> Union[grpc.aio._typing.ResponseIterableType, grpc.aio.StreamStreamCall]:
        return await self._intercept(
            continuation, client_call_details, request_iterator
        )


# grpc.aio classes are different from the sync version so we need a second definition here.


class _AuthClient:
    pass


class _ClientCallDetails(NamedTuple):
    method: str
    timeout: Optional[float]
    metadata: Optional[List]
    credentials: Optional[grpc.CallCredentials]
    wait_for_ready: Optional[bool]
    compression: Optional[grpc.Compression]


class _ClientCallDetailsWrapper(_ClientCallDetails, grpc.ClientCallDetails):
    pass


class _AuthInterceptor(
    grpc.UnaryUnaryClientInterceptor,
    grpc.UnaryStreamClientInterceptor,
    grpc.StreamUnaryClientInterceptor,
    grpc.StreamStreamClientInterceptor,
):
    _auth_client: _AuthClient

    def __init__(
        self,
        auth_client: _AuthClient,
    ):
        self._auth_client = auth_client

    async def _intercept(
        self,
        continuation: Callable[..., Any],
        client_call_details: grpc.ClientCallDetails,
        request: Any,
    ):
        token = await self._auth_client.authenticate()
        metadata = client_call_details.metadata or []
        metadata.append(("x-cerbos-auth", token))
        new_client_call_details = _ClientCallDetailsWrapper(
            client_call_details.method,
            client_call_details.timeout,
            metadata,
            client_call_details.credentials,
            client_call_details.wait_for_ready,
            client_call_details.compression,
        )
        return continuation(new_client_call_details, request)

    def intercept_unary_unary(
        self,
        continuation,
        client_call_details,
        request,
    ):
        return self._intercept(continuation, client_call_details, request)

    def intercept_unary_stream(
        self,
        continuation,
        client_call_details,
        request,
    ):
        return self._intercept(continuation, client_call_details, request)

    def intercept_stream_unary(
        self,
        continuation,
        client_call_details,
        request_iterator,
    ):
        return self._intercept(continuation, client_call_details, request_iterator)

    def intercept_stream_stream(
        self,
        continuation,
        client_call_details,
        request_iterator,
    ):
        return self._intercept(continuation, client_call_details, request_iterator)
