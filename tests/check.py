# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import logging

from cerbos.sdk.client import CerbosClient
from cerbos.sdk.model import *

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.captureWarnings(True)

    with CerbosClient(
        "https://localhost:3592",
        playground_instance="XXY",
        debug=True,
        tls_verify=False,
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
        print(c.is_allowed("view:public", p, r))

        rd = ResourceDesc("leave_request", policy_version="20210210")
        plan = c.plan_resources("view", p, rd)
        print(plan.filter.to_json())
