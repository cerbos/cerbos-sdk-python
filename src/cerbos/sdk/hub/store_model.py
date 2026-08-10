# Copyright 2021-2025 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import datetime
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from enum import Enum, auto
from typing import Self

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
        msg = f"RPC error: {cause}"
        super().__init__(msg)
        self.cause = cause
        self.underlying = underlying


class AbortedError(RpcError):
    def __init__(self, underlying: Exception):
        super().__init__(RpcErrorCause.ABORTED, underlying)


class AuthenticationFailedError(RpcError):
    def __init__(self, underlying: Exception):
        super().__init__(RpcErrorCause.AUTHENTICATION_FAILED, underlying)


class CannotModifyGitConnectedStoreError(RpcError):
    def __init__(self, underlying: Exception):
        super().__init__(RpcErrorCause.CANNOT_MODIFY_GIT_CONNECTED_STORE, underlying)


class ConditionUnsatisfiedError(RpcError):
    current_store_version: int | None = None

    def __init__(
        self,
        underlying: Exception,
        details: store_pb2.ErrDetailConditionUnsatisfied | None = None,
    ):
        super().__init__(RpcErrorCause.CONDITION_UNSATISFIED, underlying)
        if details:
            self.current_store_version = details.current_store_version


class InvalidRequestError(RpcError):
    def __init__(self, underlying: Exception):
        super().__init__(RpcErrorCause.INVALID_REQUEST, underlying)


class NoUsableFilesError(RpcError):
    ignored_files: Iterable[str] | None

    def __init__(
        self, underlying: Exception, details: store_pb2.ErrDetailNoUsableFiles
    ):
        super().__init__(RpcErrorCause.NO_USABLE_FILES, underlying)

        if details.ignored_files:
            self.ignored_files = details.ignored_files


class OperationDiscardedError(RpcError):
    current_store_version: int | None = None
    ignored_files: Iterable[str] | None = None

    def __init__(
        self,
        underlying: Exception,
        details: store_pb2.ErrDetailOperationDiscarded | None = None,
    ):
        super().__init__(RpcErrorCause.OPERATION_DISCARDED, underlying)
        if details:
            self.current_store_version = details.current_store_version
            self.ignored_files = details.ignored_files


class PermissionDeniedError(RpcError):
    def __init__(self, underlying: Exception):
        super().__init__(RpcErrorCause.PERMISSION_DENIED, underlying)


class StoreNotFoundError(RpcError):
    def __init__(self, underlying: Exception):
        super().__init__(RpcErrorCause.STORE_NOT_FOUND, underlying)


class TooManyFailuresError(RpcError):
    def __init__(self, underlying: Exception):
        super().__init__(RpcErrorCause.TOO_MANY_FAILURES, underlying)


class UnknownError(RpcError):
    def __init__(self, underlying: Exception):
        super().__init__(RpcErrorCause.UNKNOWN, underlying)


class ValidationFailureError(RpcError):
    errors: Iterable[store_pb2.FileError] | None

    def __init__(
        self, underlying: Exception, details: store_pb2.ErrDetailValidationFailure
    ):
        super().__init__(RpcErrorCause.VALIDATION_FAILURE, underlying)

        if details.errors:
            self.errors = details.errors


class ChangeDetails:
    """
    Provide detailed metadata about the change being commited to the store.
    """

    raw: store_pb2.ChangeDetails

    def __init__(self, description: str):
        self.raw = store_pb2.ChangeDetails(description=description)

    def with_uploader(
        self, name: str, metadata: Mapping[str, struct_pb2.Value] | None = None
    ) -> Self:
        """
        Set the name and any custom metadata about the uploader.
        """
        if metadata:
            self.raw.MergeFrom(
                store_pb2.ChangeDetails(
                    uploader=store_pb2.ChangeDetails.Uploader(
                        name=name, metadata=metadata
                    )
                )
            )
        else:
            self.raw.MergeFrom(
                store_pb2.ChangeDetails(
                    uploader=store_pb2.ChangeDetails.Uploader(name=name)
                )
            )

        return self

    def with_git_source(
        self,
        repo: str,
        hash: str,
        ref: str | None = None,
        message: str | None = None,
        committer: str | None = None,
        commit_date: datetime.datetime | None = None,
        author: str | None = None,
        author_date: datetime.datetime | None = None,
    ) -> Self:
        """
        Attach information about the underlying git commit.
        Mutually exclusive with internal source.
        """
        _commit_date: timestamp_pb2.Timestamp | None = None
        if commit_date:
            _commit_date = timestamp_pb2.Timestamp()
            _commit_date.FromDatetime(commit_date)

        _author_date: timestamp_pb2.Timestamp | None = None
        if author_date:
            _author_date = timestamp_pb2.Timestamp()
            _author_date.FromDatetime(author_date)

        self.raw.MergeFrom(
            store_pb2.ChangeDetails(
                git=store_pb2.ChangeDetails.Git(
                    repo=repo,
                    ref=ref,
                    hash=hash,
                    message=message,
                    committer=committer,
                    commit_date=_commit_date,
                    author=author,
                    author_date=_author_date,
                )
            )
        )

        return self

    def with_internal_source(
        self, source: str, metadata: Mapping[str, struct_pb2.Value] | None = None
    ) -> Self:
        """
        Attach information about the internal data source for this change.
        Mutually exclusive with git source.
        """
        self.raw.MergeFrom(
            store_pb2.ChangeDetails(
                internal=store_pb2.ChangeDetails.Internal(
                    source=source, metadata=metadata
                )
            )
        )
        return self


@dataclass
class File:
    path: str
    contents: bytes


@dataclass
class FileOps:
    add: Iterable[File] | None = None
    delete: Iterable[str] | None = None


@dataclass
class FilterPathEqual:
    path: str


@dataclass
class FilterPathContains:
    fragment: str


@dataclass
class FilterPathIn:
    paths: Iterable[str]


@dataclass
class ListFilesResponse:
    raw: store_pb2.ListFilesResponse

    def store_version(self) -> int:
        return self.raw.store_version

    def files(self) -> list[str]:
        return [f for f in self.raw.files]

    def __str__(self):
        return json_format.MessageToJson(self.raw)


@dataclass
class ReplaceFilesResponse:
    raw: store_pb2.ReplaceFilesResponse

    def new_store_version(self) -> int:
        return self.raw.new_store_version

    def ignored_files(self) -> list[str] | None:
        if self.raw.ignored_files:
            return [f for f in self.raw.ignored_files]

        return None

    def __str__(self):
        return json_format.MessageToJson(self.raw)


@dataclass
class ModifyFilesResponse:
    raw: store_pb2.ModifyFilesResponse

    def new_store_version(self) -> int:
        return self.raw.new_store_version

    def __str__(self):
        return json_format.MessageToJson(self.raw)


@dataclass
class GetFilesResponse:
    raw: store_pb2.GetFilesResponse

    def store_version(self) -> int:
        return self.raw.store_version

    def files(self) -> Iterable[File]:
        return (File(path=f.path, contents=f.contents) for f in self.raw.files)

    def files_as_map(self) -> Mapping[str, bytes]:
        return {f.path: f.contents for f in self.raw.files}

    def __str__(self):
        return json_format.MessageToJson(self.raw)
