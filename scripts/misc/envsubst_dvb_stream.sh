#!/bin/bash
set -eu

function desktop(){
    export IPADDR="${DESKTOP_IP_ADDRESS}"
}

function server(){
    export IPADDR="${SERVER_IP_ADDRESS}"
}


function check_env(){

    local target_array=("${@}")

    for target_var in "${target_array[@]}"; do
        if [[ ! -v ${target_var} ]]; then
            echo "ERROR: '${target_var}' は未定義です。"
            exit 1
        fi

        if [[ -z ${!target_var} ]]; then
            echo "ERROR: '${target_var}' は空文字です。"
            exit 1
        else
            echo "${target_var} は '${!target_var}' として定義されています。"
        fi
    done

    echo "✅ Required Vars Array is passed"

}


function main(){

    check_env "${REQUIRED_VARS_ARRAY[@]}"
    exit 0

    SCRIPT_DIRECTORY="$(dirname "$(readlink -f "$0")" )"
    GIT_TOPLEVEL=$(git -C "${SCRIPT_DIRECTORY}" rev-parse --show-toplevel 2>/dev/null)
    ROOT_DIRECTORY=/root
    FHS_ORIGIN_DIRECTORY=/home

    GENERATE_FILE="dvb_stram.m3u"
    TEMPLATE_FILE="template.${GENERATE_FILE}"

    TEMPLATE_PATH="${GIT_TOPLEVEL}${ROOT_DIRECTORY}${FHS_ORIGIN_DIRECTORY}/${TEMPLATE_FILE}"
    GENERATE_PATH="${HOME}/XDG_USER_DIRS/Desktop/${GENERATE_FILE}"

    echo "${TEMPLATE_PATH}   ===>   ${GENERATE_PATH}"
    # envsubst < "${TEMPLATE_PATH}" | tee "${GENERATE_PATH}" > /dev/null

}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi
