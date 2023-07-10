# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import base64
import json
import os

import pytest

from cerbos.policy.v1 import policy_pb2
from cerbos.schema.v1 import schema_pb2
from cerbos.sdk.grpc.client import (
    AdminCredentials,
    AsyncCerbosAdminClient,
    CerbosAdminClient,
)

pytestmark = pytest.mark.anyio


schema_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "../store/policies/_schemas/principal.json",
)
with open(schema_path, "rb") as f:
    d = json.load(f)
    schema_contents = json.dumps(d, separators=(",", ":")).encode()


class TestCerbosAdminClient:
    def test_admin_credentials_metadata(self, cerbos_admin_client: CerbosAdminClient):
        admin_credentials = AdminCredentials(username="user", password="password")
        metadata = admin_credentials.metadata()
        encoded_credentials = base64.b64encode("user:password".encode("utf-8")).decode(
            "utf-8"
        )
        expected_metadata = (("authorization", f"Basic {encoded_credentials}"),)
        assert metadata == expected_metadata

    def test_add_or_update_policy(self, cerbos_admin_client: CerbosAdminClient):
        cerbos_admin_client.add_or_update_policy(
            [
                policy_pb2.Policy(
                    api_version="api.cerbos.dev/v1",
                    principal_policy=policy_pb2.PrincipalPolicy(
                        principal="terry", version="default"
                    ),
                )
            ]
        )

    def test_list_policies(self, cerbos_admin_client: CerbosAdminClient):
        resp = cerbos_admin_client.list_policies()
        assert resp.policy_ids == ["principal.terry.vdefault"]

    def test_get_policy(self, cerbos_admin_client: CerbosAdminClient):
        resp = cerbos_admin_client.get_policy(["principal.terry.vdefault"])
        assert len(resp.policies) == 1
        p = resp.policies[0]
        assert p.principal_policy.principal == "terry"
        assert p.principal_policy.version == "default"

    def test_disable_policy(self, cerbos_admin_client: CerbosAdminClient):
        resp = cerbos_admin_client.disable_policy(["principal.terry.vdefault"])
        assert resp.disabled_policies == 1

    def test_enable_policy(self, cerbos_admin_client: CerbosAdminClient):
        resp = cerbos_admin_client.enable_policy(["principal.terry.vdefault"])
        assert resp.enabled_policies == 1

    def test_add_or_update_schema(self, cerbos_admin_client: CerbosAdminClient):
        cerbos_admin_client.add_or_update_schema(
            [
                schema_pb2.Schema(
                    id="principal.json",
                    definition=schema_contents,
                )
            ]
        )

    def test_list_schemas(self, cerbos_admin_client: CerbosAdminClient):
        resp = cerbos_admin_client.list_schemas()
        assert len(resp.schema_ids) == 1
        assert resp.schema_ids[0] == "principal.json"

    def test_get_schema(self, cerbos_admin_client: CerbosAdminClient):
        resp = cerbos_admin_client.get_schema(["principal.json"])
        assert len(resp.schemas) == 1
        s = resp.schemas[0]
        assert s.id == "principal.json"
        assert s.definition == schema_contents

    def test_delete_schema(self, cerbos_admin_client: CerbosAdminClient):
        resp = cerbos_admin_client.delete_schema(["principal.json"])
        assert resp.deleted_schemas == 1

    def test_reload_store(self, cerbos_admin_client: CerbosAdminClient):
        cerbos_admin_client.reload_store()


class TestAsyncCerbosAdminClient:
    async def test_add_or_update_policy(
        self, cerbos_async_admin_client: AsyncCerbosAdminClient
    ):
        await cerbos_async_admin_client.add_or_update_policy(
            [
                policy_pb2.Policy(
                    api_version="api.cerbos.dev/v1",
                    principal_policy=policy_pb2.PrincipalPolicy(
                        principal="terry", version="default"
                    ),
                )
            ]
        )

    async def test_list_policies(
        self, cerbos_async_admin_client: AsyncCerbosAdminClient
    ):
        resp = await cerbos_async_admin_client.list_policies()
        assert resp.policy_ids == ["principal.terry.vdefault"]

    async def test_get_policy(self, cerbos_async_admin_client: AsyncCerbosAdminClient):
        resp = await cerbos_async_admin_client.get_policy(["principal.terry.vdefault"])
        assert len(resp.policies) == 1
        p = resp.policies[0]
        assert p.principal_policy.principal == "terry"
        assert p.principal_policy.version == "default"

    async def test_disable_policy(
        self, cerbos_async_admin_client: AsyncCerbosAdminClient
    ):
        resp = await cerbos_async_admin_client.disable_policy(
            ["principal.terry.vdefault"]
        )
        assert resp.disabled_policies == 1

    async def test_enable_policy(
        self, cerbos_async_admin_client: AsyncCerbosAdminClient
    ):
        resp = await cerbos_async_admin_client.enable_policy(
            ["principal.terry.vdefault"]
        )
        assert resp.enabled_policies == 1

    async def test_add_or_update_schema(
        self, cerbos_async_admin_client: AsyncCerbosAdminClient
    ):
        await cerbos_async_admin_client.add_or_update_schema(
            [
                schema_pb2.Schema(
                    id="principal.json",
                    definition=schema_contents,
                )
            ]
        )

    async def test_list_schemas(
        self, cerbos_async_admin_client: AsyncCerbosAdminClient
    ):
        resp = await cerbos_async_admin_client.list_schemas()
        assert len(resp.schema_ids) == 1
        assert resp.schema_ids[0] == "principal.json"

    async def test_get_schema(self, cerbos_async_admin_client: AsyncCerbosAdminClient):
        resp = await cerbos_async_admin_client.get_schema(["principal.json"])
        assert len(resp.schemas) == 1
        s = resp.schemas[0]
        assert s.id == "principal.json"
        assert s.definition == schema_contents

    async def test_delete_schema(
        self, cerbos_async_admin_client: AsyncCerbosAdminClient
    ):
        resp = await cerbos_async_admin_client.delete_schema(["principal.json"])
        assert resp.deleted_schemas == 1

    async def test_reload_store(
        self, cerbos_async_admin_client: AsyncCerbosAdminClient
    ):
        await cerbos_async_admin_client.reload_store()
