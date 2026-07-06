#!/bin/bash
set -eu

required_vars=(
    NETWORK_INTERFACE
    IPADDR
    hogefuga
)

function main(){

    export IPADDR="${DESKTOP_IP_ADDRESS}"

    for var in "${required_vars[@]}"; do
        if [[ ! -v $var ]]; then
            echo "ERROR: '$var' が未定義です。"
            exit 1
        fi

        if [[ -z ${!var} ]]; then
            echo "ERROR: '$var' は空文字です。"
            exit 1
        fi
    done

    HOSTNAME="${HOSTNAME:-$(hostname)}"

    SCRIPT_PATH="$(readlink -f "$0")"
    SCRIPT_DIR="$(dirname "${SCRIPT_PATH}")"

    if ! GIT_TOPLEVEL=$(git -C "${SCRIPT_DIR}" rev-parse --show-toplevel 2>/dev/null); then
        echo "Error: script is not inside a git repository" >&2
        exit 1
    fi

    ROOT_DIR=/root
    FHS_ORIGIN_DIR=/etc/NetworkManager/system-connections

    template_file="template.network_interface.nmconnection"
    generate_file="${NETWORK_INTERFACE}.nmconnection"

    TEMPLATE_PATH="${GIT_TOPLEVEL}${ROOT_DIR}${FHS_ORIGIN_DIR}/${template_file}"
    GENERATE_PATH="${FHS_ORIGIN_DIR}/${generate_file}"

    if [[ -f ${GENERATE_PATH} ]]; then
        echo     "📢 [ \"${GENERATE_PATH}\" file is already exists  ]"
        echo     "📢 [ Do you want to overwrite it? ]"
        read -p  "👉️ [ y(yes) ] or [ n(no) ]  ==>  "   flagment

        if   [[ ${flagment} == "n" ]]; then
            echo "Do Nothing"
            exit 1
        elif [[ ${flagment} != "y" ]]; then
            echo "Invailed Input Key"
            exit 1
        fi
    fi

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

