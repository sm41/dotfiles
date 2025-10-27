#!/bin/bash
set -eu

# https://netplan.readthedocs.io/en/latest/

# ip link |grep "state UP"
# ip -br link show | awk '$2 == "UP" { print $1 }'
# ip addr

# /etc/netplan/xxx_config.yaml
# sudo netplan apply

function desktop(){
  export IPADDR="${DESKTOP_IP_ADDRESS}/24"
}

function server(){
  export IPADDR="${SERVER_IP_ADDRESS}/24"
}

if  [[ ${HOSTNAME} =~ ^.*desktop$ ]] ; then
  desktop
elif [[ ${HOSTNAME} =~ ^.*server$ ]] ; then
  server
else
  # echo "Invalid argument"
  exit 1
fi

SCRIPT_PATH="$(readlink -f "$0")"
SCRIPT_DIR="$(dirname "$SCRIPT_PATH")"

# HOSTNAME="${HOSTNAME:-$(hostname)}"
GIT_TOPLEVEL=$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel 2>/dev/null)

ROOT_DIR=/root
FHS_ORIGIN_DIR=/etc/netplan

generate_file="99_config.yaml"
template_file="template.${generate_file}"

TEMPLATE_PATH="${GIT_TOPLEVEL}${ROOT_DIR}${FHS_ORIGIN_DIR}/${template_file}"
GENERATE_PATH="${FHS_ORIGIN_DIR}/${generate_file}"

if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
  echo ${TEMPLATE_PATH}
  echo ${GENERATE_PATH}
  # envsubst < "${TEMPLATE_PATH}" | sudo tee "${GENERATE_PATH}" > /dev/null
fi