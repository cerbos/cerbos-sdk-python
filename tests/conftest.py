# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import logging
import os

import pytest

from cerbos.sdk.client import CerbosClient
from cerbos.sdk.container import CerbosContainer


@pytest.fixture(scope="module", params=["http", "uds"])
def cerbos_client(request, tmp_path_factory):
    policy_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "store")

    container = CerbosContainer(image="ghcr.io/cerbos/cerbos:dev")
    container.with_volume_mapping(policy_dir, "/policies")
    container.with_env("CERBOS_NO_TELEMETRY", "1")

    client = None

    if request.param == "http":
        container.with_command("server --set=schema.enforcement=reject")
        container.start()
        container.wait_until_ready()

        host = container.http_host()
        logging.info(f"Cerbos Address: {host}")
        client = CerbosClient(host, debug=True)
    elif request.param == "uds":
        sock_dir = tmp_path_factory.mktemp("socket")
        container.with_volume_mapping(sock_dir, "/socket", "rw")
        container.with_command(
            "server --set=server.httpListenAddr=unix:///socket/http.sock --set=server.udsFileMode=0o777 --set=schema.enforcement=reject"
        )

        container.start()
        container.wait_until_ready()

        client = CerbosClient(f"unix+http://{sock_dir}/http.sock", debug=True)

    yield client

    client.close()
    container.stop()
