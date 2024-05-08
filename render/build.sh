#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'
cd "${BASH_SOURCE%/*}/.."

poetry install
