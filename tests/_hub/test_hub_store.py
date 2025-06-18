# Copyright 2021-2025 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import os

import pytest

from cerbos.sdk.hub.store import AsyncCerbosHubStoreClient, CerbosHubStoreClient

pytestmark = pytest.mark.anyio


@pytest.fixture(scope="module")
async def async_hub_store_client(anyio_backend):
    async with AsyncCerbosHubStoreClient() as client:
        yield client


@pytest.fixture(scope="module")
def hub_store_client():
    with CerbosHubStoreClient() as client:
        yield client


@pytest.fixture(scope="module")
def store_id():
    return os.getenv("CERBOS_HUB_STORE_ID")


@pytest.mark.skipif(
    os.getenv("CERBOS_HUB_CLIENT_ID") == ""
    or os.getenv("CERBOS_HUB_CLIENT_SECRET") == ""
    or os.getenv("CERBOS_HUB_STORE_ID") == "",
    reason="Cerbos Hub credentials not defined",
)
class TestAsyncCerbosHubStoreClient:
    async def test_list_files(
        self, store_id: str, async_hub_store_client: AsyncCerbosHubStoreClient
    ):
        have = await async_hub_store_client.list_files(store_id)
        assert len(have.files()) > 0


@pytest.mark.skipif(
    os.getenv("CERBOS_HUB_CLIENT_ID") == ""
    or os.getenv("CERBOS_HUB_CLIENT_SECRET") == ""
    or os.getenv("CERBOS_HUB_STORE_ID") == "",
    reason="Cerbos Hub credentials not defined",
)
class TestCerbosHubStoreClient:
    def test_list_files(self, store_id: str, hub_store_client: CerbosHubStoreClient):
        have = hub_store_client.list_files(store_id)
        assert len(have.files()) > 0
