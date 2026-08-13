#!/bin/bash
set -eu

function main(){
    SCRIPT_DIRECTORY="$(dirname "$(readlink -f "$0")" )"
    GIT_TOPLEVEL=$(git -C "${SCRIPT_DIRECTORY}" rev-parse --show-toplevel 2>/dev/null)
    ROOT_FHS_DIRECTORY=/root/home
    ORIGIN_DIRECTORY=/.mozilla/firefox
    PROFILE_DIRECTORY=/"$(find "${HOME}${ORIGIN_DIRECTORY}" -maxdepth 1 -type d -path "*default-release" -printf '%f\n')"

    STANDARD_DIRECTORY="${GIT_TOPLEVEL}${ROOT_FHS_DIRECTORY}${ORIGIN_DIRECTORY}"

    mkdir -p "${HOME}${ORIGIN_DIRECTORY}${PROFILE_DIRECTORY}/chrome"

    while read FENNEC
    do
        Intermediate="${FENNEC/${GIT_TOPLEVEL}${ROOT_FHS_DIRECTORY}}"
        processed_path="${HOME}${Intermediate/"/default-release"/${PROFILE_DIRECTORY}}"

        # ln -s -f "${FENNEC}"  "${processed_path}"
        echo "${FENNEC}  ===>  ${processed_path}"

    done < <( find "${STANDARD_DIRECTORY}" -type f | sort)

}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi