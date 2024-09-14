#!/usr/bin/bash
set -eux

work_path=$(cd $(dirname $0) && pwd)

echo ${work_path}
# echo ${GITHUB_WORKSPACE}