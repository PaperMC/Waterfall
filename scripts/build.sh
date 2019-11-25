#!/usr/bin/env bash

set -e
git submodule update --init && ./scripts/applyPatches.sh

if [ "$1" == "--jar" ]; then
     mvn clean package
fi
