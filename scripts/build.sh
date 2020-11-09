#!/usr/bin/env bash

git submodule update --init && ./scripts/applyPatches.sh || exit 1

if [ "$1" == "--jar" ]; then
     mvn clean package
fi
