#!/bin/bash
set -e

source .venv/bin/activate

black --check single_app.py tests/