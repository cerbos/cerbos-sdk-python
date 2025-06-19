# Copyright 2021-2025 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0
import os
from pathlib import Path
from typing import Any, List, Optional

import pytest

from cerbos.sdk.hub import util
from cerbos.sdk.hub.store import CerbosHubStoreClient
from cerbos.sdk.hub.store_model import (
    ChangeDetails,
    ConditionUnsatisfiedError,
    FileOps,
    FilterPathEqual,
    FilterPathIn,
    InvalidRequestError,
    OperationDiscardedError,
    ValidationFailureError,
)

pytestmark = pytest.mark.anyio


@pytest.fixture(scope="module")
def hub_store_client(anyio_backend):
    with CerbosHubStoreClient() as client:
        yield client


@pytest.fixture(scope="module")
def store_id():
    return os.getenv("CERBOS_HUB_STORE_ID")


@pytest.fixture(scope="module")
def testdata_dir(pytestconfig):
    return Path(pytestconfig.rootdir, "tests", "_hub", "testdata")


@pytest.fixture(scope="module")
def zip_data(testdata_dir):
    return util.zip_directory(Path(testdata_dir, "replace_files", "success"))


@pytest.fixture(scope="class")
def reset_store(hub_store_client, store_id, zip_data):
    hub_store_client.replace_files_lenient(store_id, "Test replace", zip_data)


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
class TestCerbosHubStoreClient:
    class TestReplaceFiles:
        def test_operation_discarded_with_zip(
            self,
            store_id: str,
            testdata_dir: Path,
            hub_store_client: CerbosHubStoreClient,
            reset_store: Any,
        ):
            with pytest.raises(OperationDiscardedError):
                contents = util.zip_directory(
                    Path(testdata_dir, "replace_files", "success")
                )
                hub_store_client.replace_files(store_id, "Test replace", contents)
            assert_store_contents(hub_store_client, store_id)

        def test_operation_discarded_with_files(
            self,
            store_id: str,
            testdata_dir: Path,
            hub_store_client: CerbosHubStoreClient,
            reset_store: Any,
        ):
            with pytest.raises(OperationDiscardedError):
                hub_store_client.replace_files(
                    store_id,
                    "Test replace files",
                    util.iter_files(Path(testdata_dir, "replace_files", "success")),
                )
            assert_store_contents(hub_store_client, store_id)

        def test_invalid_files(
            self,
            store_id: str,
            testdata_dir: Path,
            hub_store_client: CerbosHubStoreClient,
            reset_store: Any,
        ):
            with pytest.raises(ValidationFailureError) as validation_error:
                contents = util.zip_directory(
                    Path(testdata_dir, "replace_files", "invalid")
                )
                hub_store_client.replace_files(store_id, "Test replace", contents)
            assert (
                isinstance(validation_error.value, ValidationFailureError)
                and validation_error.value.errors is not None
            )
            assert_store_contents(hub_store_client, store_id)

        def test_unsuccessful_condition(
            self,
            store_id: str,
            testdata_dir: Path,
            hub_store_client: CerbosHubStoreClient,
            reset_store: Any,
        ):
            with pytest.raises(ConditionUnsatisfiedError) as unsatisfied_error:
                contents = util.zip_directory(
                    Path(testdata_dir, "replace_files", "conditional")
                )
                hub_store_client.replace_files(
                    store_id,
                    "Test replace",
                    contents,
                    version_must_equal=999999999999999,
                )
            assert (
                isinstance(unsatisfied_error.value, ConditionUnsatisfiedError)
                and unsatisfied_error.value.current_store_version is not None
            )
            assert_store_contents(hub_store_client, store_id)

    class TestModifyFiles:
        def test_success(
            self,
            store_id: str,
            testdata_dir: Path,
            hub_store_client: CerbosHubStoreClient,
            reset_store: Any,
        ):
            haveAdd = hub_store_client.modify_files(
                store_id,
                "Test modify",
                FileOps(
                    add=util.iter_files(Path(testdata_dir, "modify_files", "success"))
                ),
                change_details=ChangeDetails("Test modify").with_git_source(
                    "cerbos/foo", "x"
                ),
            )
            assert haveAdd.new_store_version() > 0
            assert_store_contents(hub_store_client, store_id, ["example.yaml"])
            haveFiles = hub_store_client.get_files(store_id, ["example.yaml"])
            haveFileContents = haveFiles.files_as_map()["example.yaml"]
            assert (
                Path(
                    testdata_dir, "modify_files", "success", "example.yaml"
                ).read_bytes()
                == haveFileContents
            )
            haveDelete = hub_store_client.modify_files(
                store_id, "Test delete", FileOps(delete=["example.yaml"])
            )
            assert haveDelete.new_store_version() > haveAdd.new_store_version()
            assert_store_contents(hub_store_client, store_id)

        def test_invalid_request(
            self,
            store_id: str,
            testdata_dir: Path,
            hub_store_client: CerbosHubStoreClient,
            reset_store: Any,
        ):
            with pytest.raises(InvalidRequestError):
                hub_store_client.modify_files(store_id, "Test modify", FileOps())

        def test_invalid_files(
            self,
            store_id: str,
            testdata_dir: Path,
            hub_store_client: CerbosHubStoreClient,
            reset_store: Any,
        ):
            with pytest.raises(ValidationFailureError) as validation_error:
                hub_store_client.modify_files(
                    store_id,
                    "Test modify",
                    FileOps(
                        add=util.iter_files(
                            Path(testdata_dir, "modify_files", "invalid")
                        )
                    ),
                )
            assert (
                isinstance(validation_error.value, ValidationFailureError)
                and validation_error.value.errors is not None
            )

        def test_unsatisfied_condition(
            self,
            store_id: str,
            testdata_dir: Path,
            hub_store_client: CerbosHubStoreClient,
            reset_store: Any,
        ):
            with pytest.raises(ConditionUnsatisfiedError):
                hub_store_client.modify_files(
                    store_id,
                    "Test modify",
                    FileOps(
                        add=util.iter_files(
                            Path(testdata_dir, "modify_files", "conditional")
                        )
                    ),
                    version_must_equal=99999999999,
                )

    class TestGetFiles:
        def test_success(
            self,
            store_id: str,
            hub_store_client: CerbosHubStoreClient,
            reset_store: Any,
        ):
            have = hub_store_client.get_files(
                store_id, ["export_constants/export_constants_01.yaml"]
            )
            haveFiles = have.files_as_map()
            assert len(haveFiles) == 1
            assert "export_constants/export_constants_01.yaml" in haveFiles

        def test_non_existent(
            self,
            store_id: str,
            hub_store_client: CerbosHubStoreClient,
            reset_store: Any,
        ):
            have = hub_store_client.get_files(store_id, ["foobar"])
            assert len(have.files_as_map()) == 0

    class TestListFiles:
        def test_filter_match(
            self,
            store_id: str,
            hub_store_client: CerbosHubStoreClient,
            reset_store: Any,
        ):
            have = hub_store_client.list_files(
                store_id,
                FilterPathIn(
                    [
                        "export_constants/export_constants_01.yaml",
                        "export_variables/export_variables_01.yaml",
                    ]
                ),
            )
            haveFiles = have.files()
            assert haveFiles == [
                "export_constants/export_constants_01.yaml",
                "export_variables/export_variables_01.yaml",
            ]

        def test_no_filter_match(
            self,
            store_id: str,
            hub_store_client: CerbosHubStoreClient,
            reset_store: Any,
        ):
            have = hub_store_client.list_files(store_id, FilterPathEqual("foobar"))
            haveFiles = have.files()
            assert len(haveFiles) == 0


def assert_store_contents(
    hub_store_client: CerbosHubStoreClient,
    store_id: str,
    additional: Optional[List[str]] = None,
):
    have = hub_store_client.list_files(store_id)
    assert len(have.files()) > 0
    want = _WANT_FILES.copy()
    if additional:
        want += additional
    assert sorted(have.files()) == sorted(want)
