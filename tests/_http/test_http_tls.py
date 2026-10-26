# Copyright 2026 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import asyncio
import shutil
import ssl
import subprocess
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest

from cerbos.sdk.client import AsyncCerbosClient, CerbosClient


@pytest.fixture(scope="module")
def tls_server(tmp_path_factory):
    openssl = shutil.which("openssl")
    if openssl is None:
        pytest.skip("openssl is required to generate a temporary test certificate")
    directory = tmp_path_factory.mktemp("tls")
    certificate = directory / "certificate.pem"
    key = directory / "key.pem"
    subprocess.run(
        [
            openssl,
            "req",
            "-x509",
            "-newkey",
            "rsa:2048",
            "-nodes",
            "-keyout",
            str(key),
            "-out",
            str(certificate),
            "-days",
            "1",
            "-subj",
            "/CN=localhost",
            "-addext",
            "subjectAltName=DNS:localhost",
        ],
        check=True,
        capture_output=True,
    )

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200 if self.path == "/_cerbos/health" else 404)
            self.end_headers()

        def log_message(self, *args):
            pass

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certificate, key)
    server.socket = context.wrap_socket(server.socket, server_side=True)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"https://localhost:{server.server_port}", certificate
    finally:
        server.shutdown()
        server.server_close()
        thread.join()


@pytest.mark.parametrize("connection_retries", [0, 1])
@pytest.mark.parametrize(
    "verification", ["default", "disabled", "certificate", "context"]
)
@pytest.mark.parametrize("asynchronous", [False, True], ids=["sync", "async"])
def test_connection_retries_preserve_tls_verification(
    tls_server, connection_retries, verification, asynchronous
):
    host, certificate = tls_server
    if verification == "default":
        verify = True
    elif verification == "disabled":
        verify = False
    elif verification == "certificate":
        verify = str(certificate)
    else:
        verify = ssl.create_default_context(cafile=str(certificate))
    options = {"tls_verify": verify, "connection_retries": connection_retries}
    if asynchronous:

        async def check_health():
            async with AsyncCerbosClient(host, **options) as client:
                return await client.is_healthy()

        healthy = asyncio.run(check_health())
    else:
        with CerbosClient(host, **options) as client:
            healthy = client.is_healthy()
    # The default trust store must still reject this self-signed certificate.
    assert healthy is (verification != "default")
