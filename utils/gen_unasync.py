import unasync
import glob
import shutil
import tempfile
from pathlib import Path

if __name__ == "__main__":
    rules = [
        unasync.Rule(
            fromdir="/src/cerbos/sdk/_async/",
            todir="/src/cerbos/sdk/_sync/",
            additional_replacements={
                "AsyncCerbosAdminClient": "CerbosAdminClient",
                "AsyncCerbosClient": "CerbosClient",
                "AsyncPrincipalContext": "PrincipalContext",
                "AsyncClient": "Client",
                "AsyncHTTPTransport": "HTTPTransport",
                "AsyncCerbosHubClientBase": "CerbosHubClientBase",
                "AsyncCerbosHubStoreClient": "CerbosHubStoreClient",
                "_AsyncAuthInterceptor": "_AuthInterceptor",
                "_AsyncAuthClient": "_AuthClient",
                "_AsyncClientCallDetails": "ClientCallDetails",
                "_AsyncClientCallDetailsWrapper": "ClientCallDetailsWrapper",
                "aread": "read",
                "aclose": "close",
                "AioRpcError": "RpcError",
            },
        )
    ]

    root = Path(__file__).absolute().parent.parent / "src/cerbos/sdk/_async/**/*.py"
    files = glob.glob(str(root), recursive=True)

    unasync.unasync_files(files, rules)

    # TODO(saml) annoyingly, `unasync` doesn't seem to support replacing object
    # attributes, e.g. `grpc.aio` -> `grpc`, so we do it manually here
    # Consider alternative methods to generate sync code
    sync_root = Path(__file__).absolute().parent.parent / "src/cerbos/sdk/_sync/**/*.py"
    sync_files = glob.glob(str(sync_root), recursive=True)
    for file_path in sync_files:
        temp_file_path = ""
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
            temp_file_name = temp_file.name
            with open(file_path, "r") as original_file:
                for line in original_file:
                    temp_file.write(line.replace("grpc.aio", "grpc"))

        shutil.move(temp_file.name, file_path)
