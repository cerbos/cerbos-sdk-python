#!/usr/bin/env bash
#
# Copyright 2023 Zenauth Ltd.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo ">> Generating python classes"
(
    cd $SCRIPT_DIR
    buf generate buf.build/cerbos/cerbos-api
)
echo ">> Finished!"
