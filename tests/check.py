# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

from cerbos.sdk.client import Client
from cerbos.sdk.model import *
import logging

logging.basicConfig(level=logging.DEBUG)
logging.captureWarnings(True)

c = Client("https://localhost:3592", debug=True, tls_verify=False)
p = Principal(
    "john",
    roles={"employee"},
    policy_version="20210210",
    attr={"department": "marketing", "geography": "GB", "team": "design"},
)
r = Resource(
    "XX125",
    "leave_request",
    attr={
        "id": "XX125",
        "department": "marketing",
        "geography": "GB",
        "team": "design",
        "owner": "john",
    },
)

if __name__ == "__main__":
    print(c.is_allowed("view:public", p, r))
