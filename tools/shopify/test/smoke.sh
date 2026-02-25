#!/usr/bin/env bash
set -euo pipefail
"$(dirname "$0")/../bin/shopify" --help >/dev/null
"$(dirname "$0")/../bin/shopify" --version >/dev/null
