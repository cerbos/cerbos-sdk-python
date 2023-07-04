#!/usr/bin/env bash
#
# Copyright 2023 Zenauth Ltd.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
PROTO_DIR="${SCRIPT_DIR}/defs"
CERBOS_MODULE=${CERBOS_MODULE:-"buf.build/cerbos/cerbos-api"}

echo ">> Retrieving proto definitions"
rm -rf $PROTO_DIR
(
    cd $SCRIPT_DIR
    buf mod update
    buf export $CERBOS_MODULE -o ${PROTO_DIR}
)

# `dist` is reserved for housing the python wheel for distribution, so we need to check for namespace collisions
if [ -d "${PROTO_DIR}/dist" ]; then
    echo "Error: There cannot be a directory called \`dist\` in ${PROTO_DIR}, as we reserve this directory name for building and distribution. Please talk to the package maintainers. Exiting."
    exit 1
fi

echo ">> Generating python classes"
(
    cd $ROOT_DIR
    find $PROTO_DIR -name '*.proto' | xargs -I{} ./pw pdm run python -m grpc_tools.protoc -I $PROTO_DIR --python_out=pyi_out:. --grpc_python_out=. {}
    # find $PROTO_DIR -name '*.proto' | xargs -I{} ./pw pdm run python -m grpc_tools.protoc -I $PROTO_DIR --python_out=. --grpc_python_out=. {}
)

# For some reason, we need to explicitly create a `__init__.py` file in `google.api` in order for imports within `google.api.expr` to work correctly
if [ -d "google/api" ]; then
    touch google/api/__init__.py
fi

echo ">> Finished!"