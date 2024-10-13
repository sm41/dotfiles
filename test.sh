#!/usr/bin/bash
set -eu

work_path=$(cd $(dirname "$0") && pwd)
ddd=$(cd $(dirname "$0") && pwd)


dirname "$0"
basename $0

# ggg=$(basename)
echo ${work_path#${HOME}/*/$(basename $0)}

readlink -f $(dirname "$0")
realpath $(dirname "$0")

# echo ${GITHUB_WORKSPACE}
echo ${HOME}


