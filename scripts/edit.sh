#!/usr/bin/env bash

pushd FlameCord-Proxy
git rebase --interactive upstream/upstream
popd
