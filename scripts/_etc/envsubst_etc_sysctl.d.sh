#!/bin/bash
set -eu

# https://netplan.readthedocs.io/en/latest/

# ip link |grep "state UP"
# ip -br link show | awk '$2 == "UP" { print $1 }'
# ip addr

# /etc/netplan/xxx_config.yaml
# sudo netplan apply

if  [[ ${HOSTNAME} =~ ^.*desktop$ ]]  ||  [[ ${HOSTNAME} =~ ^.*server$ ]] ; then
  :
else
  # echo "Invalid argument"
  exit 1
fi

SCRIPT_PATH="$(readlink -f "$0")"
SCRIPT_DIR="$(dirname "$SCRIPT_PATH")"

# HOSTNAME="${HOSTNAME:-$(hostname)}"
if ! GIT_TOPLEVEL=$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel 2>/dev/null); then
  echo "Error: script is not inside a git repository" >&2
  exit 1
fi

ROOT_DIR=/root
FHS_ORIGIN_DIR=/etc/sysctl.d

generate_file="77_ipv6-privacy.conf"
template_file="template.${generate_file}"

TEMPLATE_PATH="${GIT_TOPLEVEL}${ROOT_DIR}${FHS_ORIGIN_DIR}/${template_file}"
GENERATE_PATH="${FHS_ORIGIN_DIR}/${generate_file}"

if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
  echo ${TEMPLATE_PATH}
  echo ${GENERATE_PATH}
  # envsubst < "${TEMPLATE_PATH}" | sudo tee "${GENERATE_PATH}" > /dev/null
fi