#!/usr/bin/env bash
#
# Copyright 2024 Zenauth Ltd.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LIBS_DIR="${SCRIPT_DIR}/libs"

(
    echo ">> Downloading distributions"
    cd $SCRIPT_DIR
    ./pw pdm run pip download --no-deps \
        -d ${LIBS_DIR} \
        --extra-index-url https://buf.build/gen/python \
        cerbos-cerbos-api-protocolbuffers-pyi \
        cerbos-cerbos-api-grpc-python \
        cerbos-cerbos-api-protocolbuffers-python

    echo ">> Wheels downloaded!"

    echo ">> Installing wheels"
    ./pw pdm add ${LIBS_DIR}/*

    echo ">> Proto vendoring complete!"
)
