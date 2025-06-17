# Copyright 2021-2025 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

from enum import Enum, auto
from typing import List, Optional

from google.protobuf import json_format

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


class UnknownError(RpcError):
    def __init__(self, underlying: Exception):
        super(UnknownError, self).__init__(RpcErrorCause.UNKNOWN, underlying)


class ListFilesResponse:
    raw: store_pb2.ListFilesResponse

    def __init__(self, raw: store_pb2.ListFilesResponse):
        self.raw = raw

    def store_version(self) -> int:
        return self.raw.store_version

    def files(self) -> List[str]:
        return [f for f in self.raw.files]

    def __str__(self):
        return json_format.MessageToJson(self.raw)
