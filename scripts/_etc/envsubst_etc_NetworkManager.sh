#!/bin/bash
set -eu


function desktop(){
    export IPADDR="${DESKTOP_IP_ADDRESS}"
}

function server(){
    export IPADDR="${SERVER_IP_ADDRESS}"
}

function main(){
    if  [[ ${HOSTNAME} =~ ^.*desktop$ ]] ; then
        desktop
    elif [[ ${HOSTNAME} =~ ^.*server$ ]] ; then
        server
    else
        # echo "Invalid argument"
        exit 1
    fi

    SCRIPT_PATH="$(readlink -f "$0")"
    SCRIPT_DIR="$(dirname "${SCRIPT_PATH}")"

    # HOSTNAME="${HOSTNAME:-$(hostname)}"
    if ! GIT_TOPLEVEL=$(git -C "${SCRIPT_DIR}" rev-parse --show-toplevel 2>/dev/null); then
        echo "Error: script is not inside a git repository" >&2
        exit 1
    fi

    ROOT_DIR=/root
    FHS_ORIGIN_DIR=/etc/NetworkManager/system-connections

    generate_file="${NETWORK_INTERFACE}.nmconnection"
    template_file="template.network_interface.nmconnection"

    TEMPLATE_PATH="${GIT_TOPLEVEL}${ROOT_DIR}${FHS_ORIGIN_DIR}/${template_file}"
    GENERATE_PATH="${FHS_ORIGIN_DIR}/${generate_file}"

    if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
        # echo ${TEMPLATE_PATH}
        # echo ${GENERATE_PATH}
        envsubst < "${TEMPLATE_PATH}" | sudo tee "${GENERATE_PATH}" > /dev/null && \
        sudo chmod 600 "${GENERATE_PATH}"      && \
        sudo nmcli connection reload           && \
        sudo systemctl restart NetworkManager
    fi
}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi



# sudo chmod 600 /etc/NetworkManager/system-connections/*.nmconnection
# sudo nmcli connection reload
# sudo systemctl restart NetworkManager


# nmcli connection show
# nmcli connection show ${NETWORK_INTERFACE}

