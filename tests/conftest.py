# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import logging
import os

import pytest

from cerbos.sdk.client import CerbosClient
from cerbos.sdk.container import CerbosContainer


@pytest.fixture(scope="module")
def cerbos_client():
    policy_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "store")

    container = CerbosContainer(image="ghcr.io/cerbos/cerbos:dev")
    container.with_volume_mapping(policy_dir, "/policies")
    container.with_env("CERBOS_NO_TELEMETRY", "1")
    container.start()

    container.wait_until_ready()

    host = container.http_host()
    logging.info(f"Cerbos Address: {host}")
    client = CerbosClient(host, debug=True)

    yield client

    client.close()
    container.stop()
