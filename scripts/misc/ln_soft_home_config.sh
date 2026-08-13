#!/bin/bash
set -eu

function main(){
    SCRIPT_DIRECTORY="$(dirname "$(readlink -f "$0")" )"
    GIT_TOPLEVEL=$(git -C "${SCRIPT_DIRECTORY}" rev-parse --show-toplevel 2>/dev/null)
    ROOT_FHS_DIRECTORY=/root/home
    XDG_DIRECTORY=/.config

    STANDARD_DIRECTORY="${GIT_TOPLEVEL}${ROOT_FHS_DIRECTORY}${XDG_DIRECTORY}"

    while read DOT_CONFIG
    do
        CONFIG_DIRECTORY="${HOME}${DOT_CONFIG/${GIT_TOPLEVEL}${ROOT_FHS_DIRECTORY}}"
        mkdir -p "${CONFIG_DIRECTORY%/*}"
        # ln -s -f "${DOT_CONFIG}"  "${CONFIG_DIRECTORY}"
        echo "${DOT_CONFIG}  ===>   ${CONFIG_DIRECTORY}"

    done < <( find "${STANDARD_DIRECTORY}" -not \( -path "${STANDARD_DIRECTORY}/systemd/user*" \) -type f | sort )
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi