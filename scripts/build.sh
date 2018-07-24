#!/usr/bin/env bash

git submodule update --init && ./scripts/applyPatches.sh

if [ "$1" == "--jar" ]; then
     mvn clean package
fi
