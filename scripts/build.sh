#!/usr/bin/env bash

git submodule update --init && ./scripts/applyPatches.sh && pushd Waterfall-Proxy && mvn clean package && popd
