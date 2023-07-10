# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import logging
import os

import pytest

from cerbos.sdk.client import AsyncCerbosClient, CerbosClient
from cerbos.sdk.container import CerbosContainer
from cerbos.sdk.grpc.client import AdminCredentials, AsyncCerbosAdminClient
from cerbos.sdk.grpc.client import AsyncCerbosClient as AsyncGrpcCerbosClient
from cerbos.sdk.grpc.client import CerbosAdminClient
from cerbos.sdk.grpc.client import CerbosClient as GrpcCerbosClient
from cerbos.sdk.model import *


@pytest.fixture(scope="module")
def anyio_backend():
    return "asyncio"


_params = [("http"), ("uds")]


@pytest.fixture(
    scope="module",
    params=_params,
    ids=[f"transport=http,listener={p}" for p in _params],
)
def cerbos_client(request, tmp_path_factory):
    container, host = start_container("http", request.param, tmp_path_factory)
    if container:
        with CerbosClient(host, debug=True) as client:
            yield client
        container.stop()


@pytest.mark.anyio
@pytest.fixture(
    scope="module",
    params=_params,
    ids=[f"transport=http,listener={p}" for p in _params],
)
async def cerbos_async_client(anyio_backend, request, tmp_path_factory):
    container, host = start_container("http", request.param, tmp_path_factory)
    if container:
        async with AsyncCerbosClient(host, debug=True) as client:
            yield client
        container.stop()


@pytest.fixture(
    scope="module",
    params=_params,
    ids=[f"transport=grpc,listener={p}" for p in _params],
)
def cerbos_grpc_client(request, tmp_path_factory):
    container, host = start_container("grpc", request.param, tmp_path_factory)
    if container:
        with GrpcCerbosClient(host) as client:
            yield client
        container.stop()


@pytest.mark.anyio
@pytest.fixture(
    scope="module",
    params=_params,
    ids=[f"transport=grpc,listener={p}" for p in _params],
)
async def cerbos_async_grpc_client(anyio_backend, request, tmp_path_factory):
    container, host = start_container("grpc", request.param, tmp_path_factory)
    if container:
        async with AsyncGrpcCerbosClient(host) as client:
            yield client
        container.stop()


@pytest.fixture(
    scope="module",
    params=_params,
    ids=[f"transport=grpc,listener={p}" for p in _params],
)
def cerbos_admin_client(request, tmp_path_factory):
    container, host = start_container(
        "grpc", request.param, tmp_path_factory, with_admin=True
    )
    if container:
        with CerbosAdminClient(host, AdminCredentials(password="randomHash")) as client:
            yield client
        container.stop()


@pytest.mark.anyio
@pytest.fixture(
    scope="module",
    params=_params,
    ids=[f"transport=grpc,listener={p}" for p in _params],
)
async def cerbos_async_admin_client(anyio_backend, request, tmp_path_factory):
    container, host = start_container(
        "grpc", request.param, tmp_path_factory, with_admin=True
    )
    if container:
        async with AsyncCerbosAdminClient(
            host, AdminCredentials(password="randomHash")
        ) as client:
            yield client
        container.stop()


def start_container(client_type, listener, tmp_path_factory, with_admin=False):
    store_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "store")
    container = CerbosContainer(image="ghcr.io/cerbos/cerbos:dev")
    container.with_volume_mapping(store_dir, "/store")
    container.with_env("CERBOS_NO_TELEMETRY", "1")

    with_mutable_store = ""
    if with_admin:
        with_mutable_store = (
            " --set=storage.driver=sqlite3 --set=storage.sqlite3.dsn=:memory:"
        )

    if listener == "http":
        container.with_command(
            "server --config=./store/conf.yaml --set=schema.enforcement=reject"
            + with_mutable_store
        )
        container.start()
        container.wait_until_ready()

        host = container.http_host() if client_type == "http" else container.grpc_host()
    else:
        # (07-23 saml) macOS+docker does not play nice when it comes to sharing UDS across the host and container. I've not figured out how to work around
        # this yet so I tend to comment out `uds` in the fixture params above and rely on CI to test the full suite.
        sock_dir = tmp_path_factory.mktemp("socket")

        container.with_volume_mapping(sock_dir, "/socket", "rw")
        container.with_command(
            f"server --config=./store/conf.yaml --set=server.{client_type}ListenAddr=unix:/socket/cerbos.{client_type} --set=server.udsFileMode=0o777 --set=schema.enforcement=reject"
            + with_mutable_store
        )
        container.start()
        container.wait_until_ready()

        host = f"unix:{sock_dir}/cerbos.{client_type}"

    logging.info(f"Cerbos Address: {host}")
    return container, host
