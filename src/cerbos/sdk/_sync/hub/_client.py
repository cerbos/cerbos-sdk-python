# Copyright 2021-2025 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import json
import os
from typing import Any, Dict, Optional, Union

import grpc

from cerbos.sdk.hub.model import Credentials


class SyncHubClientBase:
    _channel: grpc.Channel

    def __init__(
        self,
        credentials: Optional[Credentials] = None,
        api_endpoint: Optional[str] = None,
        timeout_secs: Union[float, None] = None,
    ):
        target = os.environ["CERBOS_HUB_API_ENDPOINT"]
        if api_endpoint:
            target = api_endpoint

        client_id = os.environ["CERBOS_HUB_CLIENT_ID"]
        client_secret = os.environ["CERBOS_HUB_CLIENT_SECRET"]
        if credentials:
            if credentials.client_id != "":
                client_id = credentials.client_id

            if credentials.client_secret != "":
                client_secret = credentials.client_secret

        if timeout_secs and not isinstance(timeout_secs, (int, float)):
            raise TypeError("timeout_secs must be a number type")

        method_config: Dict[str, Any] = {
            "methodConfig": [
                {
                    "name": [{}],
                    "timeout": "5s",
                    "maxRequestMessageBytes": 1048576,
                    "retryPolicy": {
                        "maxAttempts": 3,
                        "initialBackoff": "0.2s",
                        "maxBackoff": "5s",
                        "backoffMultiplier": 2,
                        "retryableStatusCodes": ["UNAVAILABLE"],
                    },
                },
                {
                    "name": [
                        {
                            "service": "cerbos.cloud.store.v1.CerbosStoreService",
                            "method": "ReplaceFiles",
                        },
                        {
                            "service": "cerbos.cloud.store.v1.CerbosStoreService",
                            "method": "ModifyFiles",
                        },
                    ],
                    "timeout": "10s",
                    "maxRequestMessageBytes": 20971520,
                },
            ],
            "retryThrottling": {"maxTokens": 10, "tokenRatio": 0.5},
        }

        options = [
            ("grpc.service_config_disable_resolution", False),
            ("grpc.service_config", json.dumps(method_config)),
        ]

        self._channel = grpc.secure_channel(
            target,
            credentials=grpc.ssl_channel_credentials(),
            options=options,
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        self._channel.close()
