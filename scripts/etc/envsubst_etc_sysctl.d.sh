#!/bin/bash
set -eu

# https://netplan.readthedocs.io/en/latest/

# ip link |grep "state UP"
# ip -br link show | awk '$2 == "UP" { print $1 }'
# ip addr

# /etc/netplan/xxx_config.yaml
# sudo netplan apply

required_vars=(
    NETWORK_INTERFACE
)

function main(){

    for var in "${required_vars[@]}"; do
        if [[ ! -v $var ]]; then
            echo "ERROR: '$var' が未定義です。"
            exit 1
        fi

        if [[ -z ${!var} ]]; then
            echo "ERROR: '$var' は空文字です。"
            exit 1
        fi
        echo ${!var}
    done

    echo "env var is passed"
    exit 0


    HOSTNAME="${HOSTNAME:-$(hostname)}"

    SCRIPT_PATH="$(readlink -f "$0")"
    SCRIPT_DIR="$(dirname "${SCRIPT_PATH}")"
    GIT_TOPLEVEL=$(git -C "${SCRIPT_DIR}" rev-parse --show-toplevel 2>/dev/null)
    ROOT_DIR=/root
    FHS_ORIGIN_DIR=/etc/sysctl.d

    generate_file="77_ipv6-privacy.conf"
    template_file="template.${generate_file}"

    TEMPLATE_PATH="${GIT_TOPLEVEL}${ROOT_DIR}${FHS_ORIGIN_DIR}/${template_file}"
    GENERATE_PATH="${FHS_ORIGIN_DIR}/${generate_file}"

    # echo ${TEMPLATE_PATH}
    # echo ${GENERATE_PATH}
    envsubst < "${TEMPLATE_PATH}" | sudo tee "${GENERATE_PATH}" > /dev/null

}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi