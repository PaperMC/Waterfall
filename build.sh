#!/usr/bin/env bash

./prepareBuild.sh && pushd Travertine-Proxy && mvn clean package && popd

