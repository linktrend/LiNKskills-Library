#!/usr/bin/env bash
set -euo pipefail
"$(dirname "$0")/../bin/doc-engine" --help >/dev/null
"$(dirname "$0")/../bin/doc-engine" --version >/dev/null
