#!/usr/bin/env bash
#
# Copyright 2024 Zenauth Ltd.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR=$(cd "${SCRIPT_DIR}/../src" && pwd)
PRESERVE_FILE="${SCRIPT_DIR}/.preserve"

fd --search-path="${SOURCE_DIR}" --exclude=cerbos --type=directory --max-depth=1 --exec rm -rf {}
fd --search-path="${SOURCE_DIR}/cerbos" --ignore-file="$PRESERVE_FILE" --type=directory --max-depth=1 --exec rm -rf {}
(
    cd "${SCRIPT_DIR}"
    buf generate --include-imports
)
