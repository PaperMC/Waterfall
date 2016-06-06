#!/usr/bin/env bash

./applyPatches.sh && pushd Travertine-Proxy && mvn clean package && popd

