# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for_logs


class CerbosContainer(DockerContainer):
    HTTP_PORT = 3592
    GRPC_PORT = 3593

    def __init__(self, image: str = "ghcr.io/cerbos/cerbos:latest"):
        super(CerbosContainer, self).__init__(image)
        self.with_exposed_ports(self.HTTP_PORT, self.GRPC_PORT)

    def http_host(self, protocol: str = "http") -> str:
        return f"{protocol}://{self.get_container_host_ip()}:{self.get_exposed_port(self.HTTP_PORT)}"

    def grpc_host(self) -> str:
        return f"{self.get_container_host_ip()}:{self.get_exposed_port(self.GRPC_PORT)}"

    def wait_until_ready(self, timeout_secs: float = 30):
        wait_for_logs(self, r"Starting HTTP server at", timeout=timeout_secs)
