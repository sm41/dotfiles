#!/bin/bash
set -eu

# https://netplan.readthedocs.io/en/latest/

# ip link |grep "state UP"
# ip -br link show | awk '$2 == "UP" { print $1 }'
# ip addr

# /etc/netplan/xxx_config.yaml
# sudo netplan apply

SCRIPT_PATH="$(readlink -f "$0")"
SCRIPT_DIR="$(dirname "$SCRIPT_PATH")"

HOSTNAME="${HOSTNAME:-$(hostname)}"
GIT_TOPLEVEL=$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel 2>/dev/null)

ROOT_DIR=/root
FHS_DIR=/etc
ORIGIN_DIR=/netplan
generate_file="99_config.yaml"
template_file="template.${generate_file}"

TEMPLATE_PATH="${GIT_TOPLEVEL}${ROOT_DIR}${FHS_DIR}${ORIGIN_DIR}/${template_file}"
# GENERATE_PATH="${FHS_DIR}${ORIGIN_DIR}/${generate_file}"
GENERATE_PATH="${HOME}/${generate_file}"


function desktop(){
  export IPADDR="${DESKTOP_IP_ADDRESS}/24"
}

function server(){
  export IPADDR="${SERVER_IP_ADDRESS}/24"
}

# echo ${TEMPLATE_PATH}
# echo ${GENERATE_PATH}

if  [[ ${HOSTNAME} =~ ^.*desktop$ ]] ; then
  desktop

elif [[ ${HOSTNAME} =~ ^.*server$ ]] ; then
  server

else
  # echo "Invalid argument"
  exit 1

fi

envsubst < "${TEMPLATE_PATH}" > "${GENERATE_PATH}"
