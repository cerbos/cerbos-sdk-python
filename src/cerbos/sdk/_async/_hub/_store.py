# Copyright 2021-2025 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

from functools import wraps
from typing import Optional

import grpc
from google.rpc import code_pb2
from grpc_status import rpc_status

from cerbos.cloud.store.v1 import store_pb2, store_pb2_grpc
from cerbos.sdk._async._hub._auth import InvalidCredentialsError
from cerbos.sdk._async._hub._client import _AsyncCerbosHubClientBase
from cerbos.sdk.hub.model import Credentials
from cerbos.sdk.hub.store_model import (
    AbortedError,
    AuthenticationFailedError,
    ListFilesResponse,
    OperationDiscardedError,
    UnknownError,
)


def handle_store_errors(method):
    @wraps(method)
    async def wrapper(*args, **kwargs):
        try:
            return await method(*args, **kwargs)
        except InvalidCredentialsError as e:
            raise AuthenticationFailedError(e)
        except grpc.RpcError as e:
            status = rpc_status.from_call(e)
            if status is None:
                raise UnknownError(e)

            if status.code == code_pb2.ABORTED:
                raise AbortedError(e)
            elif status.code == code_pb2.ALREADY_EXISTS:
                for detail in status.details:
                    if detail.Is(store_pb2.ErrDetailOperationDiscarded):
                        info = store_pb2.ErrDetailOperationDiscarded()
                        detail.Unpack(info)
                        raise OperationDiscardedError(e, info)

                raise OperationDiscardedError(e)

    return wrapper


class AsyncCerbosHubStoreClient(_AsyncCerbosHubClientBase):
    _store_stub: store_pb2_grpc.CerbosStoreServiceStub

    def __init__(
        self,
        credentials: Optional[Credentials] = None,
        api_endpoint: Optional[str] = None,
        timeout_secs: Optional[float] = None,
    ):
        super(AsyncCerbosHubStoreClient, self).__init__(
            credentials, api_endpoint, timeout_secs
        )
        self._store_stub = store_pb2_grpc.CerbosStoreServiceStub(self._channel)

    @handle_store_errors
    async def list_files(self, store_id: str) -> ListFilesResponse:
        resp = await self._store_stub.ListFiles(
            store_pb2.ListFilesRequest(store_id=store_id)
        )
        return ListFilesResponse(resp)
