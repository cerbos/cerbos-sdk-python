# Copyright 2021-2025 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import zipfile
from functools import wraps
from io import BytesIO
from pathlib import Path
from typing import Iterable, Optional, Union

import circuitbreaker
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
    CannotModifyGitConnectedStoreError,
    ChangeDetails,
    ConditionUnsatisfiedError,
    File,
    ListFilesResponse,
    NoUsableFilesError,
    OperationDiscardedError,
    PermissionDeniedError,
    ReplaceFilesResponse,
    StoreNotFoundError,
    TooManyFailuresError,
    UnknownError,
    ValidationFailureError,
)


class CircuitBreaker(circuitbreaker.CircuitBreaker):
    FAILURE_THRESHOLD = 10
    RECOVERY_TIMEOUT = 60


def handle_store_errors(method):
    @wraps(method)
    async def wrapper(*args, **kwargs):
        try:
            return await method(*args, **kwargs)
        except InvalidCredentialsError as e:
            raise AuthenticationFailedError(e)
        except circuitbreaker.CircuitBreakerError as e:
            raise TooManyFailuresError(e)
        except grpc.RpcError as e:
            status = rpc_status.from_call(e)
            if status is None:
                raise UnknownError(e)

            if status.code == code_pb2.ABORTED:
                raise AbortedError(e)
            elif status.code == code_pb2.ALREADY_EXISTS:
                for detail in status.details:
                    if detail.Is(store_pb2.ErrDetailOperationDiscarded.DESCRIPTOR):
                        info = store_pb2.ErrDetailOperationDiscarded()
                        detail.Unpack(info)
                        raise OperationDiscardedError(e, info)

                raise OperationDiscardedError(e)

            elif status.code == code_pb2.CANCELLED:
                raise AbortedError(e)
            elif status.code == code_pb2.DEADLINE_EXCEEDED:
                raise AbortedError(e)
            elif status.code == code_pb2.FAILED_PRECONDITION:
                for detail in status.details:
                    if detail.Is(
                        store_pb2.ErrDetailCannotModifyGitConnectedStore.DESCRIPTOR
                    ):
                        raise CannotModifyGitConnectedStoreError(e)

                    if detail.Is(store_pb2.ErrDetailConditionUnsatisfied.DESCRIPTOR):
                        info = store_pb2.ErrDetailConditionUnsatisfied()
                        detail.Unpack(info)
                        raise ConditionUnsatisfiedError(e, info)
            elif status.code == code_pb2.INVALID_ARGUMENT:
                for detail in status.details:
                    if detail.Is(store_pb2.ErrDetailNoUsableFiles.DESCRIPTOR):
                        info = store_pb2.ErrDetailNoUsableFiles()
                        detail.Unpack(info)
                        raise NoUsableFilesError(e, info)

                    if detail.Is(store_pb2.ErrDetailValidationFailure.DESCRIPTOR):
                        info = store_pb2.ErrDetailValidationFailure()
                        detail.Unpack(info)
                        raise ValidationFailureError(e, info)
            elif status.code == code_pb2.NOT_FOUND:
                raise StoreNotFoundError(e)
            elif status.code == code_pb2.PERMISSION_DENIED:
                raise PermissionDeniedError(e)
            else:
                raise UnknownError(e)

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
    @circuitbreaker.circuit(cls=CircuitBreaker)
    async def replace_files(
        self,
        store_id: str,
        message: str,
        contents: Union[bytes, Iterable[File]],
        version_must_equal: Optional[int] = None,
        change_details: Optional[ChangeDetails] = None,
    ) -> ReplaceFilesResponse:
        _change_details: Optional[store_pb2.ChangeDetails] = None
        if change_details is None:
            _change_details = store_pb2.ChangeDetails(
                description=message,
                uploader=store_pb2.ChangeDetails.Uploader(name="cerbos-sdk-python"),
            )
        else:
            _change_details = change_details.raw

        _condition: Optional[store_pb2.ReplaceFilesRequest.Condition] = None
        if version_must_equal:
            _condition = store_pb2.ReplaceFilesRequest.Condition(
                store_version_must_equal=version_must_equal
            )

        req = store_pb2.ReplaceFilesRequest(
            store_id=store_id, condition=_condition, change_details=_change_details
        )
        req: store_pb2.ReplaceFilesRequest
        if isinstance(contents, bytes):
            req = store_pb2.ReplaceFilesRequest(
                store_id=store_id,
                condition=_condition,
                change_details=_change_details,
                zipped_contents=contents,
            )
        else:
            files = (store_pb2.File(path=f.path, contents=f.contents) for f in contents)
            req = store_pb2.ReplaceFilesRequest(
                store_id=store_id,
                condition=_condition,
                change_details=_change_details,
                files=store_pb2.ReplaceFilesRequest.Files(files=files),
            )

        resp = await self._store_stub.ReplaceFiles(req)
        return ReplaceFilesResponse(resp)

    @handle_store_errors
    @circuitbreaker.circuit(cls=CircuitBreaker)
    async def replace_files_lenient(
        self,
        store_id: str,
        message: str,
        contents: Union[bytes, Iterable[File]],
        version_must_equal: Optional[int] = None,
        change_details: Optional[ChangeDetails] = None,
    ) -> ReplaceFilesResponse:
        try:
            return await self.replace_files(
                store_id, message, contents, version_must_equal, change_details
            )
        except OperationDiscardedError as e:
            return ReplaceFilesResponse(
                store_pb2.ReplaceFilesResponse(
                    new_store_version=e.current_store_version
                )
            )

    @handle_store_errors
    @circuitbreaker.circuit(cls=CircuitBreaker)
    async def list_files(self, store_id: str) -> ListFilesResponse:
        resp = await self._store_stub.ListFiles(
            store_pb2.ListFilesRequest(store_id=store_id)
        )
        return ListFilesResponse(resp)
