#!/usr/bin/env bash
#
# Copyright 2024 Zenauth Ltd.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR=$(cd "${SCRIPT_DIR}/../src" && pwd)
TEMP_DEFS_DIR="${SCRIPT_DIR}/defs"
CURRENT_PROTOS_LOG="${SCRIPT_DIR}/.current_proto_dirs"

# Additional paths might have to be added here later on: https://github.com/cerbos/cerbos-sdk-python/pull/46
PATHS=(
    "google/api/expr"
    "cerbos"
    "buf"
)

if [ -f "$CURRENT_PROTOS_LOG" ]; then
    echo ">> Removing current proto generated code..."

    while IFS= read -r dir; do
        full_path="${SOURCE_DIR}/${dir}"

        if [ -d "$full_path" ]; then
            echo "Deleting $full_path"
            rm -rf "$full_path"
        fi
    done <"$CURRENT_PROTOS_LOG"

    echo ">> Proto-generated code removal completed!"
fi

(
    echo ">> Importing proto definitions..."

    cd "$SCRIPT_DIR"
    rm -rf "$TEMP_DEFS_DIR"
    mkdir -p "$TEMP_DEFS_DIR"

    # `buf export` includes dependencies by default
    buf export buf.build/cerbos/cerbos-api --output="$TEMP_DEFS_DIR"
    buf export buf.build/cerbos/cloud-api --output="$TEMP_DEFS_DIR"

    echo ">> Import complete!"

    echo ">> Tracking generated files..."

    rm "$CURRENT_PROTOS_LOG"
    echo "# DO NOT EDIT. This is generated automatically and used to track proto-generated code" >>"$CURRENT_PROTOS_LOG"
    while IFS= read -r -d '' file; do
        dirname "${file#"$TEMP_DEFS_DIR"/}" >>"$CURRENT_PROTOS_LOG"
    done < <(find "$TEMP_DEFS_DIR" -type f -print0)

    echo ">> Tracking complete! File list stored in $CURRENT_PROTOS_LOG"

    echo ">> Generating python classes..."

    buf_generate_cmd="buf generate"
    for path in "${PATHS[@]}"; do
        buf_generate_cmd+=" --path $TEMP_DEFS_DIR/$path"
    done
    $buf_generate_cmd "$TEMP_DEFS_DIR"

    rm -rf "$TEMP_DEFS_DIR"

    echo ">> Generation complete! All done! Bye bye"
)
