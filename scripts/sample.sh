#!/bin/bash
set -eu


echo "hoge"
WORKSPACE="${GITHUB_WORKSPACE:-$(pwd)}"


bash "${WORKSPACE}/scripts/system/cp/cp_home_profile.sh"