# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import logging
import os

import pytest

from cerbos.sdk.client import AsyncCerbosClient, CerbosClient
from cerbos.sdk.container import CerbosContainer
from cerbos.sdk.model import *


@pytest.fixture(scope="module")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="module", params=["http", "uds"])
def cerbos_client(request, tmp_path_factory):
    (container, host) = start_container(request.param, tmp_path_factory)
    client = CerbosClient(host, debug=True)
    yield client

    client.close()
    container.stop()


@pytest.mark.anyio
@pytest.fixture(scope="module", params=["http", "uds"])
async def cerbos_async_client(anyio_backend, request, tmp_path_factory):
    (container, host) = start_container(request.param, tmp_path_factory)
    client = AsyncCerbosClient(host, debug=True)
    yield client

    await client.close()
    container.stop()


def start_container(listener, tmp_path_factory):
    policy_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "store")

    container = CerbosContainer(image="ghcr.io/cerbos/cerbos:dev")
    container.with_volume_mapping(policy_dir, "/policies")
    container.with_env("CERBOS_NO_TELEMETRY", "1")

    if listener == "http":
        container.with_command("server --set=schema.enforcement=reject")
        container.start()
        container.wait_until_ready()

        host = container.http_host()
        logging.info(f"Cerbos Address: {host}")
        return (container, host)
    elif listener == "uds":
        sock_dir = tmp_path_factory.mktemp("socket")
        container.with_volume_mapping(sock_dir, "/socket", "rw")
        container.with_command(
            "server --set=server.httpListenAddr=unix:///socket/http.sock --set=server.udsFileMode=0o777 --set=schema.enforcement=reject"
        )

        container.start()
        container.wait_until_ready()

        host = f"unix+http://{sock_dir}/http.sock"
        return (container, host)
