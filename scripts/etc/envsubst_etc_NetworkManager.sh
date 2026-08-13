#!/bin/bash
set -eu

REQUIRED_VARS_ARRAY=(
    NETWORK_INTERFACE
    IPADDR
)


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

    echo "Required Vars Array is passed"

}


function main(){

    check_env "${REQUIRED_VARS_ARRAY[@]}"
    exit 0

    SCRIPT_DIR="$(dirname "$(readlink -f "$0")" )"
    GIT_TOPLEVEL=$(git -C "${SCRIPT_DIR}" rev-parse --show-toplevel 2>/dev/null)
    ROOT_DIR=/root
    FHS_ORIGIN_DIR=/etc/NetworkManager/system-connections

    TEMPLATE_FILE="template.network_interface.nmconnection"
    GENERATE_FILE="${NETWORK_INTERFACE}.nmconnection"

    TEMPLATE_PATH="${GIT_TOPLEVEL}${ROOT_DIR}${FHS_ORIGIN_DIR}/${TEMPLATE_FILE}"
    GENERATE_PATH="${FHS_ORIGIN_DIR}/${GENERATE_FILE}"

    # echo ${TEMPLATE_PATH}
    # echo ${GENERATE_PATH}
    envsubst < "${TEMPLATE_PATH}" | sudo tee "${GENERATE_PATH}" > /dev/null && \
    sudo chmod 600 "${GENERATE_PATH}"      && \
    sudo nmcli connection reload           && \
    sudo systemctl restart NetworkManager

}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi


# nmcli connection show
# nmcli connection show ${NETWORK_INTERFACE}

