# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import json
from unittest.mock import Mock, patch

import anyio
import pytest
from tenacity import RetryError

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

    def test_check_resources_with_output(
        self,
        cerbos_client: CerbosClient,
        principal_john: Principal,
        resource_list: ResourceList,
    ):
        have = cerbos_client.check_resources(principal_john, resource_list)
        _assert_check_resources_with_output(have)

    @patch("httpx.Client.post")
    def test_request_retries_on_failure(
        self,
        post_mock,
        principal_john: Principal,
        resource_list: ResourceList,
    ):
        status_code = 200

        post_mock.side_effect = [
            IOError(),
            httpx.Response(
                status_code=status_code,
                text=json.dumps(
                    {
                        "request_id": "123",
                        "code": status_code,
                        "message": "success",
                    }
                ),
            ),
        ]

        client = CerbosClient("http://localhost:3592", request_retries=1, debug=True)

        resp = client.check_resources(principal_john, resource_list)

        assert resp.status_code == status_code
        assert post_mock.call_count == 2

    @patch("httpx.Client.post")
    def test_request_retries_not_if_zero(
        self,
        post_mock,
        principal_john: Principal,
        resource_list: ResourceList,
    ):
        status_code = 400

        post_mock.side_effect = [
            IOError(),
            httpx.Response(
                status_code=status_code,
                text=json.dumps(
                    {
                        "request_id": "123",
                        "code": status_code,
                        "message": "success",
                    }
                ),
            ),
        ]

        client = CerbosClient("http://localhost:3592", request_retries=0, debug=True)

        with pytest.raises(IOError):
            resp = client.check_resources(principal_john, resource_list)

            assert resp.failed()
            assert resp.status_code == status_code
            assert post_mock.call_count == 1

    @patch("httpx.Client.post")
    def test_request_retries_not_on_success(
        self,
        post_mock,
        principal_john: Principal,
        resource_list: ResourceList,
    ):
        status_code = 200

        post_mock.return_value = httpx.Response(
            status_code=status_code,
            text=json.dumps(
                {
                    "request_id": "123",
                    "code": status_code,
                    "message": "success",
                }
            ),
        )

        client = CerbosClient("http://localhost:3592", request_retries=1, debug=True)

        resp = client.check_resources(principal_john, resource_list)

        assert resp.status_code == status_code
        assert post_mock.call_count == 1

    @patch("socket.create_connection")
    def test_connection_retries(
        self,
        socket_mock,
        principal_john: Principal,
        resource_list: ResourceList,
    ):
        n_retries = 3
        n_requests = n_retries + 1

        socket_mock.side_effect = [ConnectionRefusedError()] * n_requests

        client = CerbosClient(
            "http://localhost:3592", connection_retries=n_retries, debug=True
        )

        with pytest.raises(httpx.ConnectError):
            client.check_resources(principal_john, resource_list)

        assert socket_mock.call_count == n_requests


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

    def test_check_resources_with_output(
        self,
        cerbos_client: CerbosClient,
        principal_donald: Principal,
        resource_list: ResourceList,
    ):
        principal_ctx_override = cerbos_client.with_principal(principal_donald)
        have = principal_ctx_override.check_resources(resource_list)
        _assert_check_resources_principal_override_with_output(have)

    def test_plan_resources(
        self, principal_ctx: PrincipalContext, resourcedesc_leave_req: ResourceDesc
    ):
        have = principal_ctx.plan_resources("view:*", resourcedesc_leave_req)
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

    async def test_check_resources_with_output(
        self,
        cerbos_async_client: AsyncCerbosClient,
        principal_john: Principal,
        resource_list: ResourceList,
    ):
        have = await cerbos_async_client.check_resources(principal_john, resource_list)
        _assert_check_resources_with_output(have)

    @patch("httpx.AsyncClient.post")
    async def test_request_retries_on_failure(
        self,
        post_mock,
        principal_john: Principal,
        resource_list: ResourceList,
    ):
        status_code = 200
        post_mock.side_effect = [
            IOError(),
            httpx.Response(
                status_code=status_code,
                text=json.dumps(
                    {
                        "request_id": "123",
                        "code": status_code,
                        "message": "success",
                    }
                ),
            ),
        ]

        client = AsyncCerbosClient(
            "http://localhost:3592", request_retries=1, debug=True
        )

        # TODO SamL 2023-01-03: My local machine is raising this error during this test, but the GH test runners are not. Needs to be investigated.
        # with pytest.raises(IOError):
        resp = await client.check_resources(principal_john, resource_list)

        assert resp.status_code == status_code
        assert post_mock.call_count == 2

    @patch("httpx.AsyncClient.post")
    async def test_request_retries_not_if_zero(
        self,
        post_mock,
        principal_john: Principal,
        resource_list: ResourceList,
    ):
        status_code = 400

        post_mock.side_effect = [
            IOError(),
            httpx.Response(
                status_code=status_code,
                text=json.dumps(
                    {
                        "request_id": "123",
                        "code": status_code,
                        "message": "success",
                    }
                ),
            ),
        ]

        client = AsyncCerbosClient(
            "http://localhost:3592", request_retries=0, debug=True
        )

        with pytest.raises(IOError):
            resp = await client.check_resources(principal_john, resource_list)

            assert resp.failed()
            assert resp.status_code == status_code
            assert post_mock.call_count == 1

    @patch("httpx.AsyncClient.post")
    async def test_request_retries_not_on_success(
        self,
        post_mock,
        principal_john: Principal,
        resource_list: ResourceList,
    ):
        status_code = 200

        post_mock.return_value = httpx.Response(
            status_code=status_code,
            text=json.dumps(
                {
                    "request_id": "123",
                    "code": status_code,
                    "message": "success",
                }
            ),
        )

        client = AsyncCerbosClient(
            "http://localhost:3592", request_retries=1, debug=True
        )

        resp = await client.check_resources(principal_john, resource_list)

        assert resp.status_code == status_code
        assert post_mock.call_count == 1

    @patch("anyio._backends._asyncio.connect_tcp")
    async def test_connection_retries(
        self,
        tcp_mock,
        principal_john: Principal,
        resource_list: ResourceList,
    ):
        n_retries = 3
        n_requests = n_retries + 1

        tcp_mock.side_effect = [ConnectionRefusedError()] * n_requests

        client = AsyncCerbosClient(
            "http://127.0.0.1:3592", connection_retries=n_retries, debug=True
        )

        with pytest.raises(httpx.ConnectError):
            await client.check_resources(principal_john, resource_list)

        assert tcp_mock.call_count == n_requests


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

    async def test_check_resources_with_output(
        self,
        cerbos_async_client: AsyncCerbosClient,
        principal_donald: Principal,
        resource_list: ResourceList,
    ):
        async_principal_ctx_override = cerbos_async_client.with_principal(
            principal_donald
        )
        have = await async_principal_ctx_override.check_resources(resource_list)
        _assert_check_resources_principal_override_with_output(have)

    async def test_plan_resources(
        self,
        async_principal_ctx: AsyncPrincipalContext,
        resourcedesc_leave_req: ResourceDesc,
    ):
        have = await async_principal_ctx.plan_resources(
            "view:*", resourcedesc_leave_req
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


def _assert_check_resources_with_output(have: CheckResourcesResponse):
    xx125 = have.get_resource(
        "XX125", predicate=lambda r: r.policy_version == "20210210"
    )
    assert xx125 is not None
    assert len(xx125.outputs) == 1
    outputs = xx125.outputs[0].to_dict()
    assert outputs == {
        "src": "resource.leave_request.v20210210#public-view",
        "val": {
            "formatted_string": "id:john",
            "keys": "XX125",
            "pID": "john",
            "some_bool": True,
            "some_list": ["foo", "bar"],
            "something_nested": {
                "nested_bool": False,
                "nested_formatted_string": "id:john",
                "nested_list": ["nest_foo", 1.01],
                "nested_str": "foo",
            },
        },
    }


def _assert_check_resources_principal_override_with_output(
    have: CheckResourcesResponse,
):
    xx125 = have.get_resource(
        "XX125", predicate=lambda r: r.policy_version == "20210210"
    )
    assert xx125 is not None
    assert len(xx125.outputs) == 1
    d = next(filter(lambda x: isinstance(x.val, dict), xx125.outputs))
    assert d.to_dict() == {
        "src": "resource.leave_request.v20210210#public-view",
        "val": {
            "formatted_string": "id:donald_duck",
            "keys": "XX125",
            "pID": "donald_duck",
            "some_bool": True,
            "some_list": ["foo", "bar"],
            "something_nested": {
                "nested_bool": False,
                "nested_formatted_string": "id:donald_duck",
                "nested_list": ["nest_foo", 1.01],
                "nested_str": "foo",
            },
        },
    }


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
def principal_donald():
    return Principal(
        "donald_duck",
        roles={"employee"},
        policy_version="20210210",
        attr={"department": "engineering", "geography": "GB", "team": "QA"},
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
