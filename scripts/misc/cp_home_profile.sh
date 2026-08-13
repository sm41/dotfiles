#!/usr/bin/bash
set -eu

function main(){
    SCRIPT_DIRECTORY="$(dirname "$(readlink -f "$0")" )"
    GIT_TOPLEVEL=$(git -C "${SCRIPT_DIRECTORY}" rev-parse --show-toplevel 2>/dev/null)
    ROOT_FHS_DIRECTORY=/root/home
    USER_PROFILE=".profile"

    echo ${SCRIPT_DIRECTORY}
    exit 1

    TEMP_PATH="${GIT_TOPLEVEL}${ROOT_FHS_DIRECTORY}"

    # echo "${TEMP_PATH}/sample${USER_PROFILE}"
    cp -f -b --suffix=_`date +%Y%m%d_%H%M`  "${TEMP_PATH}/sample${USER_PROFILE}"  "${HOME}/${USER_PROFILE}"
    source "${HOME}/.profile"

}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi
