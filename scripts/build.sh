#!/usr/bin/env bash

git submodule update --recursive --init && ./scripts/applyPatches.sh && pushd Travertine-Proxy && mvn clean package && popd
