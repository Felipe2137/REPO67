#!/bin/bash
set -e

source .venv/bin/activate

pylint single_app.py tests