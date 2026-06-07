#!/bin/bash
set -e

source .venv/bin/activate

BLACK_TARGET="."
BLACK_EXCLUDE="--exclude '/\.venv/'"

if [ "$1" == "check" ]; then
    black $BLACK_EXCLUDE --check $BLACK_TARGET
else
    black $BLACK_EXCLUDE $BLACK_TARGET
fi