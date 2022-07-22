# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import pytest

from cerbos.sdk.client import *
from cerbos.sdk.model import *

pytestmark = pytest.mark.anyio


class TestCerbosClient:
    def test_is_healthy(self, cerbos_client: CerbosClient):
        have = cerbos_client.is_healthy()
        assert have == True

    def test_is_allowed(
        self,
        cerbos_client: CerbosClient,
        principal_john: Principal,
        resource_john_leave_req: Resource,
    ):
        have = cerbos_client.is_allowed(
            "view:public", principal_john, resource_john_leave_req
        )
        assert have == True

    def test_principal_context_is_allowed(
        self, principal_ctx: PrincipalContext, resource_john_leave_req: Resource
    ):
        have = principal_ctx.is_allowed("view:public", resource_john_leave_req)
        assert have == True

    def test_check_resources(
        self,
        cerbos_client: CerbosClient,
        principal_john: Principal,
        resource_list: ResourceList,
    ):
        have = cerbos_client.check_resources(principal_john, resource_list)
        _assert_check_resources(have)

    def test_check_resources_empty_resources(
        self, cerbos_client: CerbosClient, principal_john: Principal
    ):
        have = cerbos_client.check_resources(principal_john, ResourceList())
        _assert_check_resources_empty_resources(have)

    def test_plan_resources(
        self,
        cerbos_client: CerbosClient,
        principal_maggie: Principal,
        resourcedesc_leave_req: ResourceDesc,
    ):
        have = cerbos_client.plan_resources(
            "approve", principal_maggie, resourcedesc_leave_req
        )
        _assert_plan_resources(have)

    def test_plan_resources_validation(
        self,
        cerbos_client: CerbosClient,
        principal_maggie_invalid: Principal,
        resourcedesc_leave_req_invalid: ResourceDesc,
    ):
        have = cerbos_client.plan_resources(
            "approve", principal_maggie_invalid, resourcedesc_leave_req_invalid
        )
        _assert_plan_resources_validation(have)


class TestPrincipalContext:
    def test_is_allowed(
        self, principal_ctx: PrincipalContext, resource_john_leave_req: Resource
    ):
        have = principal_ctx.is_allowed("view:public", resource_john_leave_req)
        assert have == True

    def test_check_resources(
        self, principal_ctx: PrincipalContext, resource_list: ResourceList
    ):
        have = principal_ctx.check_resources(resource_list)
        _assert_check_resources(have)

    def test_plan_resources(
        self, principal_ctx: PrincipalContext, resourcedesc_leave_req: ResourceDesc
    ):
        have = principal_ctx.plan_resources("view:public", resourcedesc_leave_req)
        _assert_plan_resources(have)


class TestAsyncCerbosClient:
    async def test_is_healthy(self, cerbos_async_client: AsyncCerbosClient):
        have = await cerbos_async_client.is_healthy()
        assert have == True

    async def test_is_allowed(
        self,
        cerbos_async_client: AsyncCerbosClient,
        principal_john: Principal,
        resource_john_leave_req: Resource,
    ):
        have = await cerbos_async_client.is_allowed(
            "view:public", principal_john, resource_john_leave_req
        )
        assert have == True

    async def test_principal_context_is_allowed(
        self,
        async_principal_ctx: AsyncPrincipalContext,
        resource_john_leave_req: Resource,
    ):
        have = await async_principal_ctx.is_allowed(
            "view:public", resource_john_leave_req
        )
        assert have == True

    async def test_check_resources(
        self,
        cerbos_async_client: AsyncCerbosClient,
        principal_john: Principal,
        resource_list: ResourceList,
    ):
        have = await cerbos_async_client.check_resources(principal_john, resource_list)
        _assert_check_resources(have)

    async def test_check_resources_empty_resources(
        self, cerbos_async_client: AsyncCerbosClient, principal_john: Principal
    ):
        have = await cerbos_async_client.check_resources(principal_john, ResourceList())
        _assert_check_resources_empty_resources(have)

    async def test_plan_resources(
        self,
        cerbos_async_client: AsyncCerbosClient,
        principal_maggie: Principal,
        resourcedesc_leave_req: ResourceDesc,
    ):
        have = await cerbos_async_client.plan_resources(
            "approve", principal_maggie, resourcedesc_leave_req
        )
        _assert_plan_resources(have)

    async def test_plan_resources_validation(
        self,
        cerbos_async_client: AsyncCerbosClient,
        principal_maggie_invalid: Principal,
        resourcedesc_leave_req_invalid: ResourceDesc,
    ):
        have = await cerbos_async_client.plan_resources(
            "approve", principal_maggie_invalid, resourcedesc_leave_req_invalid
        )
        _assert_plan_resources_validation(have)


class TestAsyncAsyncPrincipalContext:
    async def test_is_allowed(
        self,
        async_principal_ctx: AsyncPrincipalContext,
        resource_john_leave_req: Resource,
    ):
        have = await async_principal_ctx.is_allowed(
            "view:public", resource_john_leave_req
        )
        assert have == True

    async def test_check_resources(
        self, async_principal_ctx: AsyncPrincipalContext, resource_list: ResourceList
    ):
        have = await async_principal_ctx.check_resources(resource_list)
        _assert_check_resources(have)

    async def test_plan_resources(
        self,
        async_principal_ctx: AsyncPrincipalContext,
        resourcedesc_leave_req: ResourceDesc,
    ):
        have = await async_principal_ctx.plan_resources(
            "view:public", resourcedesc_leave_req
        )
        _assert_plan_resources(have)


def _assert_check_resources(have: CheckResourcesResponse):
    assert have.failed() == False

    xx125 = have.get_resource(
        "XX125", predicate=lambda r: r.policy_version == "20210210"
    )
    assert xx125 is not None
    assert xx125.is_allowed("view:public") == True
    assert xx125.is_allowed("approve") == False

    xx225 = have.get_resource("XX225")
    assert xx225 is not None
    assert xx225.is_allowed("view:public") == False
    assert xx225.is_allowed("approve") == False

    zz225 = have.get_resource("ZZ225")
    assert zz225 is None


def _assert_check_resources_empty_resources(have: CheckResourcesResponse):
    assert have.failed() == True
    assert have.status_msg.code == 3

    with pytest.raises(CerbosRequestException):
        have.raise_if_failed()


def _assert_plan_resources(have: PlanResourcesResponse):
    assert have.failed() == False
    assert have.resource_kind == "leave_request"
    assert have.policy_version == "20210210"
    assert have.filter.kind == PlanResourcesFilterKind.CONDITIONAL
    assert have.filter.condition is not None
    assert have.validation_errors is None


def _assert_plan_resources_validation(have: PlanResourcesResponse):
    assert have.failed() == False
    assert have.resource_kind == "leave_request"
    assert have.policy_version == "20210210"
    assert have.filter.kind == PlanResourcesFilterKind.ALWAYS_DENIED
    assert have.filter.condition is None
    assert len(have.validation_errors) == 2


@pytest.fixture
def principal_ctx(cerbos_client, principal_john):
    return cerbos_client.with_principal(principal_john)


@pytest.fixture
def async_principal_ctx(cerbos_async_client, principal_john):
    return cerbos_async_client.with_principal(principal_john)


@pytest.fixture
def resource_john_leave_req():
    return Resource(
        "XX125",
        "leave_request",
        policy_version="20210210",
        attr={
            "id": "XX125",
            "department": "marketing",
            "geography": "GB",
            "team": "design",
            "owner": "john",
        },
    )


@pytest.fixture
def resource_alice_leave_req():
    return Resource(
        "XX225",
        "leave_request",
        policy_version="20210210",
        attr={
            "id": "XX225",
            "department": "marketing",
            "geography": "GB",
            "team": "design",
            "owner": "alice",
            "status": "PENDING_APPROVAL",
        },
    )


@pytest.fixture
def resource_list(resource_john_leave_req, resource_alice_leave_req):
    return ResourceList(
        [
            ResourceAction(
                resource=resource_john_leave_req,
                actions={"view:public", "approve"},
            ),
            ResourceAction(
                resource=resource_alice_leave_req,
                actions={"view:private", "approve"},
            ),
        ]
    )


@pytest.fixture
def resourcedesc_leave_req():
    return ResourceDesc("leave_request", policy_version="20210210")


@pytest.fixture
def resourcedesc_leave_req_invalid():
    return ResourceDesc(
        "leave_request",
        policy_version="20210210",
        attr={"department": "accounting"},
    )


@pytest.fixture
def principal_john():
    return Principal(
        "john",
        roles={"employee"},
        policy_version="20210210",
        attr={"department": "marketing", "geography": "GB", "team": "design"},
    )


@pytest.fixture
def principal_maggie():
    return Principal(
        "maggie",
        roles={"manager"},
        policy_version="20210210",
        attr={
            "department": "marketing",
            "geography": "GB",
            "managed_geographies": "GB",
            "team": "design",
        },
    )


@pytest.fixture
def principal_maggie_invalid():
    return Principal(
        "maggie",
        roles={"manager"},
        policy_version="20210210",
        attr={
            "reader": False,
            "department": "accounting",
            "geography": "GB",
            "managed_geographies": "GB",
            "team": "design",
        },
    )
