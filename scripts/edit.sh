#!/usr/bin/env bash

pushd Travertine-Proxy
git rebase --interactive upstream/upstream
popd
