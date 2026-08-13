#!/bin/bash
set -eu

REQUIRED_VARS_ARRAY=(
    NETWORK_INTERFACE
    DESKTOP_IP_ADDRESS
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

    echo "✅ Required Vars Array is passed"

}

function main(){

    check_env "${REQUIRED_VARS_ARRAY[@]}"

    SCRIPT_DIRECTORY="$(dirname "$(readlink -f "$0")" )"
    GIT_TOPLEVEL=$(git -C "${SCRIPT_DIRECTORY}" rev-parse --show-toplevel 2>/dev/null)
    ROOT_DIRECTORY=/root
    FHS_ORIGIN_DIRECTORY=/etc/NetworkManager/system-connections

    TEMPLATE_FILE="template.network_interface.nmconnection"
    GENERATE_FILE="${NETWORK_INTERFACE}.nmconnection"

    TEMPLATE_PATH="${GIT_TOPLEVEL}${ROOT_DIRECTORY}${FHS_ORIGIN_DIRECTORY}/${TEMPLATE_FILE}"
    GENERATE_PATH="${FHS_ORIGIN_DIRECTORY}/${GENERATE_FILE}"

    echo ${TEMPLATE_PATH}
    echo ${GENERATE_PATH}
    # envsubst < "${TEMPLATE_PATH}" | sudo tee "${GENERATE_PATH}" > /dev/null && \
    # sudo chmod 600 "${GENERATE_PATH}"      && \
    # sudo nmcli connection reload           && \
    # sudo systemctl restart NetworkManager

}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi


# nmcli connection show
# nmcli connection show ${NETWORK_INTERFACE}

