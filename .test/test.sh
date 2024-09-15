#!/usr/bin/bash
set -eu

work_path=$(cd $(dirname $0) && pwd)

echo ${work_path}
echo ${GITHUB_WORKSPACE}
realpath $(dirname $0)