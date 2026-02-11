# Copyright 2021-2025 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0
from functools import wraps
from typing import Iterable, List, Optional, Union

import circuitbreaker
import grpc
from google.protobuf import json_format
from google.rpc import code_pb2
from grpc_status import rpc_status

from cerbos.cloud.store.v1 import store_pb2, store_pb2_grpc
from cerbos.sdk._sync._hub._auth import InvalidCredentialsError
from cerbos.sdk._sync._hub._client import _CerbosHubClientBase
from cerbos.sdk.hub.model import Credentials
from cerbos.sdk.hub.store_model import (
    AbortedError,
    AuthenticationFailedError,
    CannotModifyGitConnectedStoreError,
    ChangeDetails,
    ConditionUnsatisfiedError,
    File,
    FileOps,
    FilterPathContains,
    FilterPathEqual,
    FilterPathIn,
    GetFilesResponse,
    InvalidRequestError,
    ListFilesResponse,
    ModifyFilesResponse,
    NoUsableFilesError,
    OperationDiscardedError,
    PermissionDeniedError,
    ReplaceFilesResponse,
    StoreNotFoundError,
    TooManyFailuresError,
    UnknownError,
    ValidationFailureError,
)

_MAX_FILE_SIZE = 5 * 1024 * 1024
_MAX_UPLOAD_SIZE = 50 * 1024 * 1024
_MAX_ZIP_SIZE = 15 * 1024 * 1024
_MIN_ZIP_SIZE = 22


def _exclude_errors(thrown_type, thrown_value):
    if isinstance(thrown_value, grpc.RpcError):
        status = rpc_status.from_call(thrown_value)
        if status is None:
            return False
        return status.code in {
            code_pb2.ABORTED,
            code_pb2.CANCELLED,
            code_pb2.DEADLINE_EXCEEDED,
        }
    return False


class CircuitBreaker(circuitbreaker.CircuitBreaker):
    FAILURE_THRESHOLD = 10
    RECOVERY_TIMEOUT = 60
    EXPECTED_EXCEPTION = _exclude_errors


_CIRCUIT_BREAKER = CircuitBreaker().decorate


def handle_store_errors(method):

    @wraps(method)
    def wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
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


class CerbosHubStoreClient(_CerbosHubClientBase):
    """
    Client for working with Cerbos Hub stores.
    Requires a set of credentials which can be generated using the Cerbos Hub interface.
    Provide the credentials using the environment variables CERBOS_HUB_CLIENT_ID and CERBOS_HUB_CLIENT_SECRET.

    For well-known errors, the methods of this class raise errors that are subclasses of cerbos.sdk.hub.store_model.RpcError.
    Some of the error subclasses contain additional details about the error such as validation failures and ignored files.
    - AbortedError: call cancelled or timed out
    - AuthenticationFailedError: invalid credentials
    - CannotModifyGitConnectedStoreError: attempting to modify a store connected to Git
    - ConditionUnsatisfiedError: the condition attached to the call wasn't satisfied
    - InvalidRequestError: the arguments passed to the call are invalid
    - NoUsableFilesError: none of the provided files can be stored
    - OperationDiscardedError: the operation does not modify store state
    - PermissionDeniedError: permission denied for the action
    - TooManyFailuresError: the client has had too many failed requests and should cool down
    - UnknownError: catch-all for errors that are not specifically handled
    - ValidationFailureError: the request was rejected due to validation failures
    """

    _store_stub: store_pb2_grpc.CerbosStoreServiceStub

    def __init__(
        self,
        credentials: Optional[Credentials] = None,
        api_endpoint: Optional[str] = None,
        timeout_secs: Optional[float] = None,
    ):
        super(CerbosHubStoreClient, self).__init__(
            credentials, api_endpoint, timeout_secs
        )
        self._store_stub = store_pb2_grpc.CerbosStoreServiceStub(self._channel)

    @handle_store_errors
    @_CIRCUIT_BREAKER
    def replace_files(
        self,
        store_id: str,
        message: str,
        contents: Union[bytes, Iterable[File]],
        version_must_equal: Optional[int] = None,
        change_details: Optional[ChangeDetails] = None,
    ) -> ReplaceFilesResponse:
        """
        Overwrite the store such that it only contains the files included in this request.
        Raises OperationDiscardedError if the store is already at the desired state.
        """
        if not (store_id and store_id.strip()):
            raise InvalidRequestError(ValueError("store_id is required"))
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
            if not _MIN_ZIP_SIZE <= len(contents) <= _MAX_ZIP_SIZE:
                raise InvalidRequestError(ValueError("invalid zip contents"))
            req = store_pb2.ReplaceFilesRequest(
                store_id=store_id,
                condition=_condition,
                change_details=_change_details,
                zipped_contents=contents,
            )
        else:
            files = []
            total_size = 0
            for f in contents:
                file_size = len(f.contents)
                if file_size > _MAX_FILE_SIZE:
                    raise InvalidRequestError(ValueError(f"file {f.path} is too large"))
                total_size += file_size
                if total_size > _MAX_UPLOAD_SIZE:
                    raise InvalidRequestError(
                        ValueError("total size of files exceeds upload limit")
                    )
                files.append(store_pb2.File(path=f.path, contents=f.contents))
            if len(files) == 0:
                raise InvalidRequestError(ValueError("file list is empty"))
            req = store_pb2.ReplaceFilesRequest(
                store_id=store_id,
                condition=_condition,
                change_details=_change_details,
                files=store_pb2.ReplaceFilesRequest.Files(files=files),
            )
        resp = self._store_stub.ReplaceFiles(req)
        return ReplaceFilesResponse(resp)

    @handle_store_errors
    @_CIRCUIT_BREAKER
    def replace_files_lenient(
        self,
        store_id: str,
        message: str,
        contents: Union[bytes, Iterable[File]],
        version_must_equal: Optional[int] = None,
        change_details: Optional[ChangeDetails] = None,
    ) -> ReplaceFilesResponse:
        """
        Overwrite the store such that it only contains the files included in this request.
        Does not raise OperationDiscardedError if the store is already at the desired state.
        """
        try:
            return self.replace_files(
                store_id, message, contents, version_must_equal, change_details
            )
        except OperationDiscardedError as e:
            return ReplaceFilesResponse(
                store_pb2.ReplaceFilesResponse(
                    new_store_version=e.current_store_version
                )
            )

    @handle_store_errors
    @_CIRCUIT_BREAKER
    def modify_files(
        self,
        store_id: str,
        message: str,
        file_ops: FileOps,
        version_must_equal: Optional[int] = None,
        change_details: Optional[ChangeDetails] = None,
    ) -> ModifyFilesResponse:
        """
        Add or delete files.
        Raises OperationDiscardedError if the operation does not change store state.
        """
        if not (store_id and store_id.strip()):
            raise InvalidRequestError(ValueError("store_id is required"))
        _change_details: Optional[store_pb2.ChangeDetails] = None
        if change_details is None:
            _change_details = store_pb2.ChangeDetails(
                description=message,
                uploader=store_pb2.ChangeDetails.Uploader(name="cerbos-sdk-python"),
            )
        else:
            _change_details = change_details.raw
        _condition: Optional[store_pb2.ModifyFilesRequest.Condition] = None
        if version_must_equal:
            _condition = store_pb2.ModifyFilesRequest.Condition(
                store_version_must_equal=version_must_equal
            )
        ops: List[store_pb2.FileOp] = []
        if file_ops.add:
            total_size = 0
            for f in file_ops.add:
                file_size = len(f.contents)
                if file_size > _MAX_FILE_SIZE:
                    raise InvalidRequestError(ValueError(f"file {f.path} is too large"))
                total_size += file_size
                if total_size > _MAX_UPLOAD_SIZE:
                    raise InvalidRequestError(
                        ValueError("total size of files exceeds upload limit")
                    )
                ops.append(
                    store_pb2.FileOp(
                        add_or_update=store_pb2.File(path=f.path, contents=f.contents)
                    )
                )
        if file_ops.delete:
            for f in file_ops.delete:
                ops.append(store_pb2.FileOp(delete=f))
        if len(ops) == 0:
            raise InvalidRequestError(ValueError("file operations list is empty"))
        req = store_pb2.ModifyFilesRequest(
            store_id=store_id,
            condition=_condition,
            operations=ops,
            change_details=_change_details,
        )
        resp = self._store_stub.ModifyFiles(req)
        return ModifyFilesResponse(resp)

    @handle_store_errors
    @_CIRCUIT_BREAKER
    def modify_files_lenient(
        self,
        store_id: str,
        message: str,
        file_ops: FileOps,
        version_must_equal: Optional[int] = None,
        change_details: Optional[ChangeDetails] = None,
    ) -> ModifyFilesResponse:
        """
        Add or delete files.
        Does not raise OperationDiscardedError if the operation does not change store state.
        """
        try:
            return self.modify_files(
                store_id, message, file_ops, version_must_equal, change_details
            )
        except OperationDiscardedError as e:
            return ModifyFilesResponse(
                store_pb2.ModifyFilesResponse(new_store_version=e.current_store_version)
            )

    @handle_store_errors
    @_CIRCUIT_BREAKER
    def get_files(self, store_id: str, file_paths: Iterable[str]) -> GetFilesResponse:
        """
        Retrieve the contents of the given files.
        """
        if not (store_id and store_id.strip()):
            raise InvalidRequestError(ValueError("store_id is required"))
        req = store_pb2.GetFilesRequest(store_id=store_id, files=file_paths)
        resp = self._store_stub.GetFiles(req)
        return GetFilesResponse(resp)

    @handle_store_errors
    @circuitbreaker.circuit(cls=CircuitBreaker)
    def list_files(
        self,
        store_id: str,
        filter: Optional[
            Union[FilterPathEqual, FilterPathContains, FilterPathIn]
        ] = None,
    ) -> ListFilesResponse:
        """
        List the files available on the remote store.
        The listing can be filtered by providing an optional `filter` argument which can be one of the following types.
          - FilterPathEqual: Match a path exactly
          - FilterPathLike: Match a path partially
          - FilterPathIn: Match any or all of the paths in the given list
        """
        path_filter: Optional[store_pb2.FileFilter] = None
        if filter:
            if isinstance(filter, FilterPathEqual):
                path_filter = store_pb2.FileFilter(
                    path=store_pb2.StringMatch(equals=filter.path)
                )
            elif isinstance(filter, FilterPathContains):
                path_filter = store_pb2.FileFilter(
                    path=store_pb2.StringMatch(contains=filter.fragment)
                )
            elif isinstance(filter, FilterPathIn):
                # "in" is a Python keyword  :(
                path_filter = json_format.ParseDict(
                    {"path": {"in": {"values": [p for p in filter.paths]}}},
                    store_pb2.FileFilter(),
                )
        resp = self._store_stub.ListFiles(
            store_pb2.ListFilesRequest(store_id=store_id, filter=path_filter)
        )
        return ListFilesResponse(resp)
