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
ORIGIN_DIR=/sysctl.d
generate_file="77_ipv6-privacy.conf"
template_file="template.${generate_file}"


TEMPLATE_PATH="${GIT_TOPLEVEL}${ROOT_DIR}${FHS_DIR}${ORIGIN_DIR}/${template_file}"
# GENERATE_PATH="${FHS_DIR}${ORIGIN_DIR}/${generate_file}"
GENERATE_PATH="${HOME}/${generate_file}"

# echo ${TEMPLATE_PATH}
# echo ${GENERATE_PATH}

if  [[ ${HOSTNAME} =~ ^.*desktop$ ]]  ||  [[ ${HOSTNAME} =~ ^.*server$ ]] ; then
  export NETWORK_INTERFACE="$(ip -br link show | awk '$2 == "UP" { print $1 }')"

else
  # echo "Invalid argument"
  exit 1

fi

envsubst < "${TEMPLATE_PATH}" > "${GENERATE_PATH}"
