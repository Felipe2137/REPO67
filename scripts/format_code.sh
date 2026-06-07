#!/bin/bash
set -e

source .venv/bin/activate

if [ "$1" == "check" ]; then
    black --check .
else
    black .
fi
