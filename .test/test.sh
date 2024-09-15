#!/usr/bin/bash
set -eu

work_path=$(cd $(dirname $0) && pwd)

echo ${work_path}
realpath $(dirname $0)
echo ${GITHUB_WORKSPACE}
echo ${HOME}