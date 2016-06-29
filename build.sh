#!/usr/bin/env bash

git submodule update --recursive --init && ./applyPatches.sh && pushd Travertine-Proxy && mvn clean package && popd
