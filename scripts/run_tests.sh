#!/bin/bash
set -e

source .venv/bin/activate

PYTHONPATH=. pytest -v