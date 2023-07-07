# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

from cerbos.effect.v1.effect_pb2 import EFFECT_ALLOW
from cerbos.response.v1.response_pb2 import CheckResourcesResponse


def get_resource(
    resp: CheckResourcesResponse,
    resource_id: str,
    predicate=lambda _: True,
) -> CheckResourcesResponse.ResultEntry | None:
    return next(
        filter(
            lambda r: (r.resource.id == resource_id and predicate(r.resource)),
            resp.results,
        ),
        None,
    )


def is_allowed(entry: CheckResourcesResponse.ResultEntry, action: str) -> bool:
    if action in entry.actions:
        return entry.actions[action] == EFFECT_ALLOW
    return False
