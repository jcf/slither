#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'
cd "${BASH_SOURCE%/*}/.."

# `app.main:app` refers to the `app` var within the `app/main.py` file.
exec uvicorn app.main:app --host 0.0.0.0 --port $PORT
