#!/usr/bin/bash
set -eu

work_path=$(cd $(dirname "$0") && pwd)

echo ${work_path}
readlink -f $(dirname "$0")
realpath $(dirname "$0")
# echo ${GITHUB_WORKSPACE}
echo ${HOME}


