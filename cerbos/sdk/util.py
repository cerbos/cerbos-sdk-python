# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

from requests.adapters import HTTPAdapter


class TimeoutAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout_secs = kwargs["timeout_secs"]
        del kwargs["timeout_secs"]

        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        kwargs["timeout"] = self.timeout_secs
        return super().send(request, **kwargs)
