#!/bin/bash
# set -eu


# echo ${pwd}
WORKSPACE="${GITHUB_WORKSPACE:-$(pwd)}"


bash "${WORKSPACE}/scripts/system/cp/cp_home_profile.sh"