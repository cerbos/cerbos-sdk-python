# Copyright 2021-2025 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import os
from pathlib import Path
from typing import Any

import pytest

from cerbos.sdk.hub import util
from cerbos.sdk.hub.store import AsyncCerbosHubStoreClient, CerbosHubStoreClient
from cerbos.sdk.hub.store_model import (
    ConditionUnsatisfiedError,
    OperationDiscardedError,
    ValidationFailureError,
)

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


@pytest.fixture(scope="module")
def testdata_dir(pytestconfig):
    return Path(pytestconfig.rootdir, "tests", "_hub", "testdata")


@pytest.fixture(scope="class")
async def async_reset_store(async_hub_store_client, store_id, testdata_dir):
    contents = util.zip_directory(Path(testdata_dir, "replace_files", "success"))
    await async_hub_store_client.replace_files_lenient(
        store_id, "Test replace", contents
    )


@pytest.fixture(scope="class")
def reset_store(hub_store_client, store_id, testdata_dir):
    contents = util.zip_directory(Path(testdata_dir, "replace_files", "success"))
    hub_store_client.replace_files_lenient(store_id, "Test replace", contents)


_WANT_FILES = [
    "_schemas/principal.json",
    "_schemas/resources/leave_request.json",
    "_schemas/resources/purchase_order.json",
    "_schemas/resources/salary_record.json",
    "derived_roles/common_roles.yaml",
    "derived_roles/derived_roles_01.yaml",
    "derived_roles/derived_roles_02.yaml",
    "derived_roles/derived_roles_03.yaml",
    "derived_roles/derived_roles_04.yaml",
    "derived_roles/derived_roles_05.yaml",
    "export_constants/export_constants_01.yaml",
    "export_variables/export_variables_01.yaml",
    "principal_policies/policy_01.yaml",
    "principal_policies/policy_02.yaml",
    "principal_policies/policy_02_acme.hr.yaml",
    "principal_policies/policy_02_acme.sales.yaml",
    "principal_policies/policy_02_acme.yaml",
    "principal_policies/policy_03.yaml",
    "principal_policies/policy_04.yaml",
    "principal_policies/policy_05.yaml",
    "principal_policies/policy_06.yaml",
    "resource_policies/disabled_policy_01.yaml",
    "resource_policies/policy_01.yaml",
    "resource_policies/policy_02.yaml",
    "resource_policies/policy_03.yaml",
    "resource_policies/policy_04.yaml",
    "resource_policies/policy_04_test.yaml",
    "resource_policies/policy_05.yaml",
    "resource_policies/policy_05_acme.hr.uk.brighton.kemptown.yaml",
    "resource_policies/policy_05_acme.hr.uk.brighton.yaml",
    "resource_policies/policy_05_acme.hr.uk.london.yaml",
    "resource_policies/policy_05_acme.hr.uk.yaml",
    "resource_policies/policy_05_acme.hr.yaml",
    "resource_policies/policy_05_acme.yaml",
    "resource_policies/policy_06.yaml",
    "resource_policies/policy_07.yaml",
    "resource_policies/policy_07_acme.yaml",
    "resource_policies/policy_08.yaml",
    "resource_policies/policy_09.yaml",
    "resource_policies/policy_10.yaml",
    "resource_policies/policy_11.yaml",
    "resource_policies/policy_12.yaml",
    "resource_policies/policy_13.yaml",
    "resource_policies/policy_14.yaml",
    "resource_policies/policy_15.yaml",
    "resource_policies/policy_16.yaml",
    "resource_policies/policy_17.acme.sales.yaml",
    "resource_policies/policy_17.acme.yaml",
    "resource_policies/policy_17.yaml",
    "resource_policies/policy_18.yaml",
    "role_policies/policy_01_acme.hr.uk.brighton.yaml",
    "role_policies/policy_02_acme.hr.uk.brighton.yaml",
    "role_policies/policy_03_acme.hr.uk.yaml",
    "role_policies/policy_04_acme.hr.uk.yaml",
    "role_policies/policy_05_acme.hr.uk.london.yaml",
    "role_policies/policy_06_acme.hr.uk.brighton.kemptown.yaml",
    "tests/policy_04_test.yaml",
    "tests/policy_05_test.yaml",
]


@pytest.mark.skipif(
    os.getenv("CERBOS_HUB_CLIENT_ID") == ""
    or os.getenv("CERBOS_HUB_CLIENT_SECRET") == ""
    or os.getenv("CERBOS_HUB_STORE_ID") == "",
    reason="Cerbos Hub credentials not defined",
)
class TestAsyncCerbosHubStoreClient:
    class TestReplaceFiles:
        async def test_operation_discarded_with_zip(
            self,
            store_id: str,
            testdata_dir: Path,
            async_hub_store_client: AsyncCerbosHubStoreClient,
            async_reset_store: Any,
        ):
            with pytest.raises(OperationDiscardedError):
                contents = util.zip_directory(
                    Path(testdata_dir, "replace_files", "success")
                )
                await async_hub_store_client.replace_files(
                    store_id, "Test replace", contents
                )
            await async_assert_store_contents_unchanged(
                async_hub_store_client, store_id
            )

        async def test_operation_discarded_with_files(
            self,
            store_id: str,
            testdata_dir: Path,
            async_hub_store_client: AsyncCerbosHubStoreClient,
            async_reset_store: Any,
        ):
            with pytest.raises(OperationDiscardedError):
                await async_hub_store_client.replace_files(
                    store_id,
                    "Test replace files",
                    util.iter_files(Path(testdata_dir, "replace_files", "success")),
                )
            await async_assert_store_contents_unchanged(
                async_hub_store_client, store_id
            )

        async def test_invalid_files(
            self,
            store_id: str,
            testdata_dir: Path,
            async_hub_store_client: AsyncCerbosHubStoreClient,
            async_reset_store: Any,
        ):
            with pytest.raises(ValidationFailureError) as validation_error:
                contents = util.zip_directory(
                    Path(testdata_dir, "replace_files", "invalid")
                )
                await async_hub_store_client.replace_files(
                    store_id, "Test replace", contents
                )
            assert (
                isinstance(validation_error.value, ValidationFailureError)
                and validation_error.value.errors is not None
            )
            await async_assert_store_contents_unchanged(
                async_hub_store_client, store_id
            )

        async def test_unsuccessful_condition(
            self,
            store_id: str,
            testdata_dir: Path,
            async_hub_store_client: AsyncCerbosHubStoreClient,
            async_reset_store: Any,
        ):
            with pytest.raises(ConditionUnsatisfiedError) as unsatisfied_error:
                contents = util.zip_directory(
                    Path(testdata_dir, "replace_files", "conditional")
                )
                await async_hub_store_client.replace_files(
                    store_id,
                    "Test replace",
                    contents,
                    version_must_equal=999999999999999,
                )
            assert (
                isinstance(unsatisfied_error.value, ConditionUnsatisfiedError)
                and unsatisfied_error.value.current_store_version is not None
            )
            await async_assert_store_contents_unchanged(
                async_hub_store_client, store_id
            )

    class TestListFiles:
        async def test_list_files(
            self,
            store_id: str,
            async_hub_store_client: AsyncCerbosHubStoreClient,
            async_reset_store: Any,
        ):
            have = await async_hub_store_client.list_files(store_id)
            assert len(have.files()) > 0


async def async_assert_store_contents_unchanged(
    async_hub_store_client: AsyncCerbosHubStoreClient, store_id: str
):
    have = await async_hub_store_client.list_files(store_id)
    assert len(have.files()) > 0
    assert sorted(have.files()) == sorted(_WANT_FILES)


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
