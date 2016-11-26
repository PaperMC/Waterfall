#!/usr/bin/env bash

pushd Waterfall-Proxy
git rebase --interactive upstream/upstream
popd
