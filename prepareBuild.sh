#!/usr/bin/env bash

git submodule update --recursive --init

pushd Waterfall

./applyPatches.sh

popd

./applyPatches.sh

