# Copyright 2021-2025 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import datetime
from dataclasses import dataclass
from enum import Enum, auto
from typing import Iterable, List, Mapping, Optional, Self

from google.protobuf import json_format, struct_pb2, timestamp_pb2

from cerbos.cloud.store.v1 import store_pb2


class RpcErrorCause(Enum):
    ABORTED = auto()
    AUTHENTICATION_FAILED = auto()
    CANNOT_MODIFY_GIT_CONNECTED_STORE = auto()
    CONDITION_UNSATISFIED = auto()
    INVALID_REQUEST = auto()
    NO_USABLE_FILES = auto()
    OPERATION_DISCARDED = auto()
    PERMISSION_DENIED = auto()
    STORE_NOT_FOUND = auto()
    TOO_MANY_FAILURES = auto()
    UNKNOWN = auto()
    VALIDATION_FAILURE = auto()

    def __str__(self):
        return self.name


class RpcError(Exception):
    cause: RpcErrorCause
    underlying: Exception

    def __init__(self, cause: RpcErrorCause, underlying: Exception):
        msg = "RPC error: {0}".format(cause)
        super(RpcError, self).__init__(msg)
        self.cause = cause
        self.underlying = underlying


class AbortedError(RpcError):
    def __init__(self, underlying: Exception):
        super(AbortedError, self).__init__(RpcErrorCause.ABORTED, underlying)


class AuthenticationFailedError(RpcError):
    def __init__(self, underlying: Exception):
        super(AuthenticationFailedError, self).__init__(
            RpcErrorCause.AUTHENTICATION_FAILED, underlying
        )


class CannotModifyGitConnectedStoreError(RpcError):
    def __init__(self, underlying: Exception):
        super(CannotModifyGitConnectedStoreError, self).__init__(
            RpcErrorCause.CANNOT_MODIFY_GIT_CONNECTED_STORE, underlying
        )


class ConditionUnsatisfiedError(RpcError):
    current_store_version: Optional[int] = None

    def __init__(
        self,
        underlying: Exception,
        details: Optional[store_pb2.ErrDetailConditionUnsatisfied] = None,
    ):
        super(ConditionUnsatisfiedError, self).__init__(
            RpcErrorCause.CONDITION_UNSATISFIED, underlying
        )
        if details:
            self.current_store_version = details.current_store_version


class NoUsableFilesError(RpcError):
    ignored_files: Optional[Iterable[str]]

    def __init__(
        self, underlying: Exception, details: store_pb2.ErrDetailNoUsableFiles
    ):
        super(NoUsableFilesError, self).__init__(
            RpcErrorCause.NO_USABLE_FILES, underlying
        )

        if details.ignored_files:
            self.ignored_files = details.ignored_files


class OperationDiscardedError(RpcError):
    current_store_version: Optional[int] = None

    def __init__(
        self,
        underlying: Exception,
        details: Optional[store_pb2.ErrDetailOperationDiscarded] = None,
    ):
        super(OperationDiscardedError, self).__init__(
            RpcErrorCause.OPERATION_DISCARDED, underlying
        )
        if details:
            self.current_store_version = details.current_store_version


class PermissionDeniedError(RpcError):
    def __init__(self, underlying: Exception):
        super(PermissionDeniedError, self).__init__(
            RpcErrorCause.PERMISSION_DENIED, underlying
        )


class StoreNotFoundError(RpcError):
    def __init__(self, underlying: Exception):
        super(StoreNotFoundError, self).__init__(
            RpcErrorCause.STORE_NOT_FOUND, underlying
        )


class TooManyFailuresError(RpcError):
    def __init__(self, underlying: Exception):
        super(TooManyFailuresError, self).__init__(
            RpcErrorCause.TOO_MANY_FAILURES, underlying
        )


class UnknownError(RpcError):
    def __init__(self, underlying: Exception):
        super(UnknownError, self).__init__(RpcErrorCause.UNKNOWN, underlying)


class ValidationFailureError(RpcError):
    errors: Optional[Iterable[store_pb2.FileError]]

    def __init__(
        self, underlying: Exception, details: store_pb2.ErrDetailValidationFailure
    ):
        super(ValidationFailureError, self).__init__(
            RpcErrorCause.VALIDATION_FAILURE, underlying
        )

        if details.errors:
            self.errors = details.errors


class ChangeDetails:
    raw: store_pb2.ChangeDetails

    def __init__(self, description: str):
        self.raw = store_pb2.ChangeDetails(description=description)

    def with_uploader(
        self, name: str, metadata: Optional[Mapping[str, struct_pb2.Value]] = None
    ) -> Self:
        if metadata:
            self.raw.uploader = store_pb2.ChangeDetails.Uploader(
                name=name, metadata=metadata
            )
        else:
            self.raw.uploader = store_pb2.ChangeDetails.Uploader(name=name)

        return self

    def with_git_source(
        self,
        repo: str,
        hash: str,
        ref: Optional[str] = None,
        message: Optional[str] = None,
        committer: Optional[str] = None,
        commit_date: Optional[datetime.datetime] = None,
        author: Optional[str] = None,
        author_date: Optional[datetime.datetime] = None,
    ) -> Self:
        _commit_date: Optional[timestamp_pb2.Timestamp] = None
        if commit_date:
            _commit_date = timestamp_pb2.Timestamp()
            _commit_date.FromDatetime(commit_date)

        _author_date: Optional[timestamp_pb2.Timestamp] = None
        if author_date:
            _author_date = timestamp_pb2.Timestamp()
            _author_date.FromDatetime(author_date)

        self.raw.git = store_pb2.ChangeDetails.Git(
            repo=repo,
            ref=ref,
            hash=hash,
            message=message,
            committer=committer,
            commit_date=_commit_date,
            author=author,
            author_date=_author_date,
        )

        return self

    def with_internal_source(
        self, source: str, metadata: Optional[Mapping[str, struct_pb2.Value]] = None
    ) -> Self:
        self.raw.internal = store_pb2.ChangeDetails.Internal(
            source=source, metadata=metadata
        )
        return self


@dataclass
class File:
    path: str
    contents: bytes


@dataclass
class ListFilesResponse:
    raw: store_pb2.ListFilesResponse

    def store_version(self) -> int:
        return self.raw.store_version

    def files(self) -> List[str]:
        return [f for f in self.raw.files]

    def __str__(self):
        return json_format.MessageToJson(self.raw)


@dataclass
class ReplaceFilesResponse:
    raw: store_pb2.ReplaceFilesResponse

    def new_store_version(self) -> int:
        return self.raw.new_store_version

    def ignored_files(self) -> Optional[List[str]]:
        if self.raw.ignored_files:
            return [f for f in self.raw.ignored_files]

        return None

    def __str__(self):
        return json_format.MessageToJson(self.raw)
