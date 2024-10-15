#!/usr/bin/bash
set -eu

work_path=$(cd $(dirname "$0") && pwd)
ddd=$(cd $(dirname "$0") && pwd)

echo $0
echo ${BASH_SOURCE:-$0}
echo ------
realpath $0
realpath ${BASH_SOURCE}
realpath ${BASH_SOURCE:-$0}
echo ------
readlink -f $(dirname "$0")
realpath $(dirname "$0")
echo ------

# echo ${GITHUB_WORKSPACE}
# echo ${HOME}


