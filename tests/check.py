# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import logging

import anyio

from cerbos.sdk.client import AsyncCerbosClient
from cerbos.sdk.model import *


async def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.captureWarnings(True)

    async with AsyncCerbosClient(
        "https://localhost:3592",
        playground_instance="XXY",
        debug=True,
        tls_verify=False,
        raise_on_error=True,
    ) as c:
        p = Principal(
            "john",
            roles={"employee"},
            policy_version="20210210",
            attr={"department": "marketing", "geography": "GB", "team": "design"},
        )
        r = Resource(
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

        allowed = await c.is_allowed("view:public", p, r)
        print(allowed)

        rd = ResourceDesc("leave_request", policy_version="20210210")
        plan = await c.plan_resources("view", p, rd)
        print(plan.filter.to_json())


if __name__ == "__main__":
    anyio.run(main)
