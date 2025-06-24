# Copyright 2021-2025 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import zipfile
from io import BytesIO
from pathlib import Path
from typing import Iterable

from cerbos.sdk.hub.store_model import File


def zip_directory(directory: Path) -> bytes:
    mem = BytesIO()
    with zipfile.ZipFile(mem, mode="w") as memzip:
        for f in _list_files(directory):
            memzip.write(f, f.relative_to(directory))

    return mem.getvalue()


def iter_files(directory: Path) -> Iterable[File]:
    for f in _list_files(directory):
        store_file_name = f.relative_to(directory)
        contents = f.read_bytes()
        if len(contents) > 0:
            yield File(path=store_file_name.__str__(), contents=contents)


def _list_files(directory: Path) -> Iterable[Path]:
    for root, dirs, files in directory.walk(top_down=True):
        for f in files:
            if (not f.startswith(".")) and (f.endswith((".yaml", ".yml", ".json"))):
                yield root / f

        dirs[:] = [d for d in dirs if not d.startswith(".")]
