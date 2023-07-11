# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

from typing import List

import grpc
import pytest
from google.protobuf import struct_pb2
from google.protobuf.json_format import MessageToDict

from cerbos.engine.v1 import engine_pb2
from cerbos.request.v1 import request_pb2
from cerbos.response.v1 import response_pb2
from cerbos.sdk.grpc.client import (
    AsyncCerbosClient,
    AsyncPrincipalContext,
    CerbosClient,
    PrincipalContext,
)
from cerbos.sdk.grpc.utils import get_resource, is_allowed

pytestmark = pytest.mark.anyio


class TestCerbosClient:
    def test_is_allowed(
        self,
        cerbos_grpc_client: CerbosClient,
        principal_john: engine_pb2.Principal,
        resource_john_leave_req: engine_pb2.Resource,
    ):
        have = cerbos_grpc_client.is_allowed(
            "view:public", principal_john, resource_john_leave_req
        )
        assert have

    def test_principal_context_is_allowed(
        self,
        principal_ctx: PrincipalContext,
        resource_john_leave_req: engine_pb2.Resource,
    ):
        have = principal_ctx.is_allowed("view:public", resource_john_leave_req)
        assert have

    def test_check_resources(
        self,
        cerbos_grpc_client: CerbosClient,
        principal_john: engine_pb2.Principal,
        resource_list: List[request_pb2.CheckResourcesRequest.ResourceEntry],
    ):
        have = cerbos_grpc_client.check_resources(principal_john, resource_list)
        _assert_check_resources(have)

    def test_check_resources_empty_resources(
        self, cerbos_grpc_client: CerbosClient, principal_john: engine_pb2.Principal
    ):
        with pytest.raises(
            grpc.RpcError,
            match="invalid CheckResourcesRequest.Resources: value must contain at least 1 item\\(s\\)",
        ) as e:
            cerbos_grpc_client.check_resources(principal_john, [])
        err = e.value
        assert err.code().value[0] == 3

    def test_plan_resources(
        self,
        cerbos_grpc_client: CerbosClient,
        principal_maggie: engine_pb2.Principal,
        resourcedesc_leave_req: engine_pb2.PlanResourcesInput.Resource,
    ):
        have = cerbos_grpc_client.plan_resources(
            "approve", principal_maggie, resourcedesc_leave_req
        )
        _assert_plan_resources(have)

    def test_plan_resources_validation(
        self,
        cerbos_grpc_client: CerbosClient,
        principal_maggie_invalid: engine_pb2.Principal,
        resourcedesc_leave_req_invalid: engine_pb2.PlanResourcesInput.Resource,
    ):
        have = cerbos_grpc_client.plan_resources(
            "approve", principal_maggie_invalid, resourcedesc_leave_req_invalid
        )
        _assert_plan_resources_validation(have)

    def test_check_resources_with_output(
        self,
        cerbos_grpc_client: CerbosClient,
        principal_john: engine_pb2.Principal,
        resource_list: List[request_pb2.CheckResourcesRequest.ResourceEntry],
    ):
        have = cerbos_grpc_client.check_resources(principal_john, resource_list)
        _assert_check_resources_with_output(have)


class TestPrincipalContext:
    def test_is_allowed(
        self,
        principal_ctx: PrincipalContext,
        resource_john_leave_req: engine_pb2.Resource,
    ):
        have = principal_ctx.is_allowed("view:public", resource_john_leave_req)
        assert have

    def test_check_resources(
        self,
        principal_ctx: PrincipalContext,
        resource_list: List[request_pb2.CheckResourcesRequest.ResourceEntry],
    ):
        have = principal_ctx.check_resources(resource_list)
        _assert_check_resources(have)

    def test_check_resources_with_output(
        self,
        cerbos_grpc_client: CerbosClient,
        principal_donald: engine_pb2.Principal,
        resource_list: List[request_pb2.CheckResourcesRequest.ResourceEntry],
    ):
        principal_ctx_override = cerbos_grpc_client.with_principal(principal_donald)
        have = principal_ctx_override.check_resources(resource_list)
        _assert_check_resources_principal_override_with_output(have)

    def test_plan_resources(
        self,
        principal_ctx: PrincipalContext,
        resourcedesc_leave_req: engine_pb2.PlanResourcesInput.Resource,
    ):
        have = principal_ctx.plan_resources("view:*", resourcedesc_leave_req)
        _assert_plan_resources(have)


class TestAsyncCerbosClient:
    async def test_is_allowed(
        self,
        cerbos_async_grpc_client: AsyncCerbosClient,
        principal_john: engine_pb2.Principal,
        resource_john_leave_req: engine_pb2.Resource,
    ):
        have = await cerbos_async_grpc_client.is_allowed(
            "view:public", principal_john, resource_john_leave_req
        )
        assert have

    async def test_principal_context_is_allowed(
        self,
        async_principal_ctx: AsyncPrincipalContext,
        resource_john_leave_req: engine_pb2.Resource,
    ):
        have = await async_principal_ctx.is_allowed(
            "view:public", resource_john_leave_req
        )
        assert have

    async def test_check_resources(
        self,
        cerbos_async_grpc_client: AsyncCerbosClient,
        principal_john: engine_pb2.Principal,
        resource_list: List[request_pb2.CheckResourcesRequest.ResourceEntry],
    ):
        have = await cerbos_async_grpc_client.check_resources(
            principal_john, resource_list
        )
        _assert_check_resources(have)

    async def test_check_resources_empty_resources(
        self,
        cerbos_async_grpc_client: AsyncCerbosClient,
        principal_john: engine_pb2.Principal,
    ):
        with pytest.raises(
            grpc.aio.AioRpcError,
            match="invalid CheckResourcesRequest.Resources: value must contain at least 1 item\\(s\\)",
        ) as e:
            await cerbos_async_grpc_client.check_resources(principal_john, [])
        err = e.value
        assert err.code().value[0] == 3

    async def test_plan_resources(
        self,
        cerbos_async_grpc_client: AsyncCerbosClient,
        principal_maggie: engine_pb2.Principal,
        resourcedesc_leave_req: engine_pb2.PlanResourcesInput.Resource,
    ):
        have = await cerbos_async_grpc_client.plan_resources(
            "approve", principal_maggie, resourcedesc_leave_req
        )
        _assert_plan_resources(have)

    async def test_plan_resources_validation(
        self,
        cerbos_async_grpc_client: AsyncCerbosClient,
        principal_maggie_invalid: engine_pb2.Principal,
        resourcedesc_leave_req_invalid: engine_pb2.PlanResourcesInput.Resource,
    ):
        have = await cerbos_async_grpc_client.plan_resources(
            "approve", principal_maggie_invalid, resourcedesc_leave_req_invalid
        )
        _assert_plan_resources_validation(have)

    async def test_check_resources_with_output(
        self,
        cerbos_async_grpc_client: AsyncCerbosClient,
        principal_john: engine_pb2.Principal,
        resource_list: List[request_pb2.CheckResourcesRequest.ResourceEntry],
    ):
        have = await cerbos_async_grpc_client.check_resources(
            principal_john, resource_list
        )
        _assert_check_resources_with_output(have)


class TestAsyncAsyncPrincipalContext:
    async def test_is_allowed(
        self,
        async_principal_ctx: AsyncPrincipalContext,
        resource_john_leave_req: engine_pb2.Resource,
    ):
        have = await async_principal_ctx.is_allowed(
            "view:public", resource_john_leave_req
        )
        assert have

    async def test_check_resources(
        self,
        async_principal_ctx: AsyncPrincipalContext,
        resource_list: List[request_pb2.CheckResourcesRequest.ResourceEntry],
    ):
        have = await async_principal_ctx.check_resources(resource_list)
        _assert_check_resources(have)

    async def test_check_resources_with_output(
        self,
        cerbos_async_grpc_client: AsyncCerbosClient,
        principal_donald: engine_pb2.Principal,
        resource_list: List[request_pb2.CheckResourcesRequest.ResourceEntry],
    ):
        async_principal_ctx_override = cerbos_async_grpc_client.with_principal(
            principal_donald
        )
        have = await async_principal_ctx_override.check_resources(resource_list)
        _assert_check_resources_principal_override_with_output(have)

    async def test_plan_resources(
        self,
        async_principal_ctx: AsyncPrincipalContext,
        resourcedesc_leave_req: engine_pb2.PlanResourcesInput.Resource,
    ):
        have = await async_principal_ctx.plan_resources(
            "view:*", resourcedesc_leave_req
        )
        _assert_plan_resources(have)


def _assert_check_resources(have: response_pb2.CheckResourcesResponse):
    xx125 = get_resource(
        have, "XX125", predicate=lambda r: r.policy_version == "20210210"
    )
    assert xx125 is not None
    assert is_allowed(xx125, "view:public")
    assert not is_allowed(xx125, "approve")

    xx225 = get_resource(have, "XX225")
    assert xx225 is not None
    assert not is_allowed(xx225, "view:public")
    assert not is_allowed(xx225, "approve")

    zz225 = get_resource(have, "ZZ225")
    assert zz225 is None


def _assert_plan_resources(have: response_pb2.PlanResourcesResponse):
    assert have.resource_kind == "leave_request"
    assert have.policy_version == "20210210"
    assert have.filter.kind == engine_pb2.PlanResourcesFilter.KIND_CONDITIONAL
    assert have.filter.condition is not None
    assert len(have.validation_errors) == 0


def _assert_plan_resources_validation(have: response_pb2.PlanResourcesResponse):
    assert have.resource_kind == "leave_request"
    assert have.policy_version == "20210210"
    assert have.filter.kind == engine_pb2.PlanResourcesFilter.KIND_ALWAYS_DENIED
    assert len(have.filter.condition.SerializeToString()) == 0
    assert len(have.validation_errors) == 2


def _assert_check_resources_with_output(have: response_pb2.CheckResourcesResponse):
    xx125 = get_resource(
        have, "XX125", predicate=lambda r: r.policy_version == "20210210"
    )
    assert xx125 is not None
    assert len(xx125.outputs) == 1
    outputs = MessageToDict(xx125.outputs[0])
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
    have: response_pb2.CheckResourcesResponse,
):
    xx125 = get_resource(
        have, "XX125", predicate=lambda r: r.policy_version == "20210210"
    )
    assert xx125 is not None
    assert len(xx125.outputs) == 1
    d = next(filter(lambda x: x.val.HasField("struct_value"), xx125.outputs))
    assert MessageToDict(d) == {
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
def principal_ctx(cerbos_grpc_client, principal_john):
    return cerbos_grpc_client.with_principal(principal_john)


@pytest.fixture
def async_principal_ctx(cerbos_async_grpc_client, principal_john):
    return cerbos_async_grpc_client.with_principal(principal_john)


@pytest.fixture
def resource_john_leave_req():
    return engine_pb2.Resource(
        id="XX125",
        kind="leave_request",
        policy_version="20210210",
        attr={
            "id": struct_pb2.Value(string_value="XX125"),
            "department": struct_pb2.Value(string_value="marketing"),
            "geography": struct_pb2.Value(string_value="GB"),
            "team": struct_pb2.Value(string_value="design"),
            "owner": struct_pb2.Value(string_value="john"),
        },
    )


@pytest.fixture
def resource_alice_leave_req():
    return engine_pb2.Resource(
        id="XX225",
        kind="leave_request",
        policy_version="20210210",
        attr={
            "id": struct_pb2.Value(string_value="XX225"),
            "department": struct_pb2.Value(string_value="marketing"),
            "geography": struct_pb2.Value(string_value="GB"),
            "team": struct_pb2.Value(string_value="design"),
            "owner": struct_pb2.Value(string_value="alice"),
            "status": struct_pb2.Value(string_value="PENDING_APPROVAL"),
        },
    )


@pytest.fixture
def resource_list(resource_john_leave_req, resource_alice_leave_req):
    return [
        request_pb2.CheckResourcesRequest.ResourceEntry(
            resource=resource_john_leave_req,
            actions={"view:public", "approve"},
        ),
        request_pb2.CheckResourcesRequest.ResourceEntry(
            resource=resource_alice_leave_req,
            actions={"view:private", "approve"},
        ),
    ]


@pytest.fixture
def resourcedesc_leave_req():
    return engine_pb2.PlanResourcesInput.Resource(
        kind="leave_request",
        policy_version="20210210",
    )


@pytest.fixture
def resourcedesc_leave_req_invalid():
    return engine_pb2.PlanResourcesInput.Resource(
        kind="leave_request",
        policy_version="20210210",
        attr={"department": struct_pb2.Value(string_value="accounting")},
    )


@pytest.fixture
def principal_john():
    return engine_pb2.Principal(
        id="john",
        roles=["employee"],
        policy_version="20210210",
        attr={
            "department": struct_pb2.Value(string_value="marketing"),
            "geography": struct_pb2.Value(string_value="GB"),
            "team": struct_pb2.Value(string_value="design"),
        },
    )


@pytest.fixture
def principal_maggie():
    return engine_pb2.Principal(
        id="maggie",
        roles={"manager"},
        policy_version="20210210",
        attr={
            "department": struct_pb2.Value(string_value="marketing"),
            "geography": struct_pb2.Value(string_value="GB"),
            "managed_geographies": struct_pb2.Value(string_value="GB"),
            "team": struct_pb2.Value(string_value="design"),
        },
    )


@pytest.fixture
def principal_donald():
    return engine_pb2.Principal(
        id="donald_duck",
        roles={"employee"},
        policy_version="20210210",
        attr={
            "department": struct_pb2.Value(string_value="engineering"),
            "geography": struct_pb2.Value(string_value="GB"),
            "team": struct_pb2.Value(string_value="QA"),
        },
    )


@pytest.fixture
def principal_maggie_invalid():
    return engine_pb2.Principal(
        id="maggie",
        roles={"manager"},
        policy_version="20210210",
        attr={
            "reader": struct_pb2.Value(bool_value=False),
            "department": struct_pb2.Value(string_value="accounting"),
            "geography": struct_pb2.Value(string_value="GB"),
            "managed_geographies": struct_pb2.Value(string_value="GB"),
            "team": struct_pb2.Value(string_value="design"),
        },
    )
