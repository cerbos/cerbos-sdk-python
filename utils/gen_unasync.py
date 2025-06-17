# Adapted from https://github.com/python-trio/unasync/blob/3d7a3695099f8e5772631025c0b32909527437fb/src/unasync/__init__.py
# MIT Licence: https://github.com/python-trio/unasync/blob/3d7a3695099f8e5772631025c0b32909527437fb/LICENSE.MIT

import ast
import glob
import shutil
import tempfile
from pathlib import Path
import collections
import os
import tokenize as std_tokenize

import tokenize_rt
from setuptools.command import build_py as orig


_ASYNC_TO_SYNC = {
    "__aenter__": "__enter__",
    "__aexit__": "__exit__",
    "__aiter__": "__iter__",
    "__anext__": "__next__",
    "asynccontextmanager": "contextmanager",
    "AsyncIterable": "Iterable",
    "AsyncIterator": "Iterator",
    "AsyncGenerator": "Generator",
    # TODO StopIteration is still accepted in Python 2, but the right change
    # is 'raise StopAsyncIteration' -> 'return' since we want to use unasynced
    # code in Python 3.7+
    "StopAsyncIteration": "StopIteration",
}


class Rule:
    """A single set of rules for 'unasync'ing file(s)"""

    def __init__(self, fromdir, todir, additional_replacements=None):
        self.fromdir = fromdir.replace("/", os.sep)
        self.todir = todir.replace("/", os.sep)

        # Add any additional user-defined token replacements to our list.
        self.token_replacements = _ASYNC_TO_SYNC.copy()
        for key, val in (additional_replacements or {}).items():
            self.token_replacements[key] = val

    def _match(self, filepath):
        """Determines if a Rule matches a given filepath and if so
        returns a higher comparable value if the match is more specific.
        """
        file_segments = [x for x in filepath.split(os.sep) if x]
        from_segments = [x for x in self.fromdir.split(os.sep) if x]
        len_from_segments = len(from_segments)

        if len_from_segments > len(file_segments):
            return False

        for i in range(len(file_segments) - len_from_segments + 1):
            if file_segments[i : i + len_from_segments] == from_segments:
                return len_from_segments, i

        return False

    def _unasync_file(self, filepath):
        with open(filepath, "rb") as f:
            encoding, _ = std_tokenize.detect_encoding(f.readline)

        with open(filepath, encoding=encoding) as f:
            contents = f.read()
            tokens = self._preprocess(filepath, contents)
            tokens = self._unasync_tokens(tokens)
            result = tokenize_rt.tokens_to_src(tokens)
            outfilepath = filepath.replace(self.fromdir, self.todir)
            os.makedirs(os.path.dirname(outfilepath), exist_ok=True)
            with open(outfilepath, "wb") as f:
                f.write(result.encode(encoding))

    def _preprocess(self, filename, contents):
        tokens = tokenize_rt.src_to_tokens(contents)
        ignored_lines = set()
        for token in tokens:
            if token.name == "COMMENT" and "unasync:ignore" in token.src:
                ignored_lines.add(token.line)

        if len(ignored_lines) > 0:
            to_delete = set()
            tree = ast.parse(contents, filename=filename)
            for node in ast.walk(tree):
                if hasattr(node, "lineno") and getattr(node, "lineno") in ignored_lines:
                    for lineno in range(
                        getattr(node, "lineno"), getattr(node, "end_lineno") + 1
                    ):
                        to_delete.add(lineno)

            for i, token in tokenize_rt.reversed_enumerate(tokens):
                if token.line in to_delete:
                    tokens.pop(i)

        return tokens

    def _unasync_tokens(self, tokens):
        skip_next = False
        for token in tokens:
            if skip_next:
                skip_next = False
                continue

            if token.src in ["async", "await"]:
                # When removing async or await, we want to skip the following whitespace
                # so that `print(await stuff)` becomes `print(stuff)` and not `print( stuff)`
                skip_next = True
            else:
                if token.name == "NAME":
                    token = token._replace(src=self._unasync_name(token.src))
                elif token.name == "STRING":
                    left_quote, name, right_quote = (
                        token.src[0],
                        token.src[1:-1],
                        token.src[-1],
                    )
                    token = token._replace(
                        src=left_quote + self._unasync_name(name) + right_quote
                    )

                yield token

    def _unasync_name(self, name):
        if name in self.token_replacements:
            return self.token_replacements[name]
        # Convert classes prefixed with 'Async' into 'Sync'
        elif len(name) > 5 and name.startswith("Async") and name[5].isupper():
            return name[5:]
        elif len(name) > 6 and name.startswith("_Async") and name[6].isupper():
            return "_" + name[6:]
        return name


def unasync_files(fpath_list, rules):
    for f in fpath_list:
        found_rule = None
        found_weight = None

        for rule in rules:
            weight = rule._match(f)
            if weight and (found_weight is None or weight > found_weight):
                found_rule = rule
                found_weight = weight

        if found_rule:
            found_rule._unasync_file(f)


Token = collections.namedtuple("Token", ["type", "string", "start", "end", "line"])


_DEFAULT_RULE = Rule(fromdir="/_async/", todir="/_sync/")


class _build_py(orig.build_py):
    """
    Subclass build_py from setuptools to modify its behavior.

    Convert files in _async dir from being asynchronous to synchronous
    and saves them in _sync dir.
    """

    UNASYNC_RULES = (_DEFAULT_RULE,)

    def run(self):
        rules = self.UNASYNC_RULES

        self._updated_files = []

        # Base class code
        if self.py_modules:
            self.build_modules()
        if self.packages:
            self.build_packages()
            self.build_package_data()

        # Our modification!
        unasync_files(self._updated_files, rules)

        # Remaining base class code
        self.byte_compile(self.get_outputs(include_bytecode=False))

    def build_module(self, module, module_file, package):
        outfile, copied = super().build_module(module, module_file, package)
        if copied:
            self._updated_files.append(outfile)
        return outfile, copied


def cmdclass_build_py(rules=(_DEFAULT_RULE,)):
    """Creates a 'build_py' class for use within 'cmdclass={"build_py": ...}'"""

    class _custom_build_py(_build_py):
        UNASYNC_RULES = rules

    return _custom_build_py


if __name__ == "__main__":
    rules = [
        Rule(
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

    unasync_files(files, rules)

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
