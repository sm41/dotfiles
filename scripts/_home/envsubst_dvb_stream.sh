#!/bin/bash
set -eu

function desktop(){
    export IPADDR="${DESKTOP_IP_ADDRESS}"
}

function server(){
    export IPADDR="${SERVER_IP_ADDRESS}"
}

function main(){

    HOSTNAME="${HOSTNAME:-$(hostname)}"

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

    if ! GIT_TOPLEVEL=$(git -C "${SCRIPT_DIR}" rev-parse --show-toplevel 2>/dev/null); then
        echo "Error: script is not inside a git repository" >&2
        exit 1
    fi

    ROOT_DIR=/root
    FHS_ORIGIN_DIR=/home

    generate_file="dvb_stram.m3u"
    template_file="template.${generate_file}"

    TEMPLATE_PATH="${GIT_TOPLEVEL}${ROOT_DIR}${FHS_ORIGIN_DIR}/${template_file}"
    GENERATE_PATH="${HOME}/XDG_USER_DIRS/Desktop/${generate_file}"

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

    envsubst < "${TEMPLATE_PATH}" | tee "${GENERATE_PATH}" > /dev/null

}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi
