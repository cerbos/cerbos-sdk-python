# Copyright 2021-2025 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import zipfile
from io import BytesIO
from pathlib import Path
from typing import Coroutine, Iterable

from cerbos.sdk.hub.store_model import File


def zip_directory(directory: Path) -> bytes:
    mem = BytesIO()
    with zipfile.ZipFile(mem, mode="w") as memzip:
        for root, dirs, files in directory.walk(top_down=True):
            for f in files:
                if not f.startswith("."):
                    file_name = root / f
                    memzip.write(file_name, file_name.relative_to(directory))

            dirs[:] = [d for d in dirs if not d.startswith(".")]

    return mem.getvalue()


def iter_files(directory: Path) -> Iterable[File]:
    for root, dirs, files in directory.walk(top_down=True):
        for f in files:
            if not f.startswith("."):
                full_file_name = root / f
                store_file_name = full_file_name.relative_to(directory)
                yield File(
                    path=store_file_name.__str__(), contents=full_file_name.read_bytes()
                )

        dirs[:] = [d for d in dirs if not d.startswith(".")]
