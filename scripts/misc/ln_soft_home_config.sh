#!/bin/bash
set -eu

function main(){
    SCRIPT_DIR="$(dirname "$(readlink -f "$0")" )"
    GIT_TOPLEVEL=$(git -C "${SCRIPT_DIR}" rev-parse --show-toplevel 2>/dev/null)
    ROOT_FHS_DIR=/root/home
    XDG_DIR=/.config

    while read DOT_CONFIG
    do
        CONFIG_DIR="${HOME}${DOT_CONFIG/${GIT_TOPLEVEL}${ROOT_FHS_DIR}}"
        mkdir -p "${CONFIG_DIR%/*}"
        # ln -s -f "${DOT_CONFIG}"  "${CONFIG_DIR}"
        echo "${DOT_CONFIG}  ===>   ${CONFIG_DIR}"

    done < <( find "${GIT_TOPLEVEL}${ROOT_FHS_DIR}${XDG_DIR}" -not \( -path "${GIT_TOPLEVEL}${ROOT_FHS_DIR}${XDG_DIR}/systemd/user*" \) -type f | sort )
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi