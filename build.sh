#!/usr/bin/env bash

git submodule update --init && ./applyPatches.sh && pushd Waterfall-Proxy && mvn clean package && popd

