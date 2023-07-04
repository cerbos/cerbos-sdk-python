# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import logging
import os

import pytest

from cerbos.sdk.client import AsyncCerbosClient, CerbosClient
from cerbos.sdk.grpc.client import (
    AsyncCerbosClient as AsyncGrpcCerbosClient,
    CerbosClient as GrpcCerbosClient,
)
from cerbos.sdk.container import CerbosContainer
from cerbos.sdk.model import *


@pytest.fixture(scope="module")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="module", params=[("http"), ("uds")])
def cerbos_client(request, tmp_path_factory):
    container, host = start_container("http", request.param, tmp_path_factory)
    if container:
        with CerbosClient(host, debug=True) as client:
            yield client
        container.stop()


@pytest.mark.anyio
@pytest.fixture(scope="module", params=[("http"), ("uds")])
async def cerbos_async_client(anyio_backend, request, tmp_path_factory):
    container, host = start_container("http", request.param, tmp_path_factory)
    if container:
        async with AsyncCerbosClient(host, debug=True) as client:
            yield client
        container.stop()


@pytest.fixture(scope="module", params=[("http"), ("uds")])
def cerbos_grpc_client(request, tmp_path_factory):
    container, host = start_container("grpc", request.param, tmp_path_factory)
    if container:
        with GrpcCerbosClient(host) as client:
            yield client
        container.stop()


@pytest.mark.anyio
@pytest.fixture(scope="module", params=[("http"), ("uds")])
async def cerbos_async_grpc_client(anyio_backend, request, tmp_path_factory):
    container, host = start_container("grpc", request.param, tmp_path_factory)
    if container:
        async with AsyncGrpcCerbosClient(host) as client:
            yield client
        container.stop()


def start_container(client_type, listener, tmp_path_factory):
    policy_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "store")
    container = CerbosContainer(image="ghcr.io/cerbos/cerbos:dev")
    container.with_volume_mapping(policy_dir, "/policies")
    container.with_env("CERBOS_NO_TELEMETRY", "1")

    if listener == "http":
        container.with_command("server --set=schema.enforcement=reject")
        container.start()
        container.wait_until_ready()

        host = container.http_host() if client_type == "http" else container.grpc_host()
    else:
        sock_dir = tmp_path_factory.mktemp("socket")

        if client_type == "http":
            host = f"unix+http://{sock_dir}/http.sock"
        else:
            host = f"unix:{sock_dir}/grpc.sock"

        container.with_volume_mapping(sock_dir, "/socket", "rw")
        container.with_command(
            f"server --set=server.{client_type}ListenAddr=unix:/socket/{client_type}.sock --set=server.udsFileMode=0o777 --set=schema.enforcement=reject"
        )
        container.start()
        container.wait_until_ready()

    logging.info(f"Cerbos Address: {host}")
    return container, host
