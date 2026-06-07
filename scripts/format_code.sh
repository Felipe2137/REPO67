#!/bin/bash
set -e

source .venv/bin/activate

if [ "$1" == "check" ]; then
    black --check single_app.py tests/
else
    black single_app.py tests/
fi