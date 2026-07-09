#!/usr/bin/bash
set -eu


function main(){
    SCRIPT_PATH="$(readlink -f "$0")"
    SCRIPT_DIR="$(dirname "${SCRIPT_PATH}")"

    GIT_TOPLEVEL=$(git -C "${SCRIPT_DIR}" rev-parse --show-toplevel 2>/dev/null)

    ROOT_FHS_DIR=/root/home
    TEMP_PATH="${GIT_TOPLEVEL}${ROOT_FHS_DIR}"

    USER_PROFILE=".profile"

    # echo "${TEMP_PATH}/sample${USER_PROFILE}"
    cp -f -b --suffix=_`date +%Y%m%d_%H%M`  "${TEMP_PATH}/sample${USER_PROFILE}"  "${HOME}/${USER_PROFILE}"

    source "${HOME}/.profile"

}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi
