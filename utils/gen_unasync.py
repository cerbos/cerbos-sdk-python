import unasync
import glob
from pathlib import Path

if __name__ == '__main__':
    rules = [
        unasync.Rule(
            fromdir="/cerbos/sdk/_async/",
            todir="/cerbos/sdk/_sync/",
            additional_replacements={
                "AsyncCerbosClient": "CerbosClient",
                "AsyncPrincipalContext": "PrincipalContext",
                "AsyncClient": "Client",
                "AsyncHTTPTransport": "HTTPTransport",
                "aread": "read",
                "aclose": "close",
            },
        )
    ]

    root = Path(__file__).absolute().parent.parent / "cerbos/sdk/_async/**/*.py"
    files = glob.glob(str(root), recursive=True)

    unasync.unasync_files(files, rules)
