# Copyright 2021-2025 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0
from typing import Any, Callable, List, NamedTuple, Optional, Union

import grpc

from cerbos.sdk._sync._hub._auth import _AuthClient

# grpc.aio classes are annoyingly different from the non-async version so we need a second, slightly-different non-async implementation.


class _ClientCallDetails(NamedTuple):
    method: str
    timeout: Optional[float]
    metadata: Optional[List]
    credentials: Optional[grpc.CallCredentials]
    wait_for_ready: Optional[bool]
    compression: Optional[grpc.Compression]


# Dummy placeholder so that the non-async interceptor type-checks.


class _ClientCallDetailsWrapper(_ClientCallDetails, grpc.ClientCallDetails):
    pass


# Dummy placeholder so that the non-async interceptor type-checks.


class _AuthInterceptor(
    grpc.UnaryUnaryClientInterceptor,
    grpc.UnaryStreamClientInterceptor,
    grpc.StreamUnaryClientInterceptor,
    grpc.StreamStreamClientInterceptor,
):
    _auth_client: _AuthClient

    def __init__(self, auth_client: _AuthClient):
        self._auth_client = auth_client

    def _intercept(
        self,
        continuation: Callable[..., Any],
        client_call_details: grpc.ClientCallDetails,
        request: Any,
    ):
        token = self._auth_client.authenticate()
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

    def intercept_unary_unary(self, continuation, client_call_details, request):
        return self._intercept(continuation, client_call_details, request)

    def intercept_unary_stream(self, continuation, client_call_details, request):
        return self._intercept(continuation, client_call_details, request)

    def intercept_stream_unary(
        self, continuation, client_call_details, request_iterator
    ):
        return self._intercept(continuation, client_call_details, request_iterator)

    def intercept_stream_stream(
        self, continuation, client_call_details, request_iterator
    ):
        return self._intercept(continuation, client_call_details, request_iterator)
