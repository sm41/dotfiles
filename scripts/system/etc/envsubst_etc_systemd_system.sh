#!/bin/bash
set -eu


# lsblk -dno UUID | awk 'NF'
# lsblk -o NAME,SIZE,FSTYPE,UUID,LABEL,PARTUUID,PARTLABEL,MOUNTPOINT

# -d, --nodeps         スレーブデバイスやホルダーを表示しません
# -n, --noheadings     ヘッダを表示しません
# -o, --output <list>  出力する列を指定します


function desktop(){
  export UUID="0123456789"
}

function server(){
  export SERVER_IP_ADDRESS="192.168.1.38"
}

HOSTNAME="${HOSTNAME:-$(hostname)}"
mount_dir="misc"

if  [[ ${HOSTNAME} =~ ^.*desktop$ ]] ; then
  generate_file="mnt-samba-${mount_dir}.mount"
  template_file="template.${generate_file}"
  desktop

elif [[ ${HOSTNAME} =~ ^.*server$ ]] ; then
  generate_file="mnt-local-${mount_dir}.mount"
  template_file="template.${generate_file}"
  server

else
  # echo "Invalid argument"
  exit 1

fi


SCRIPT_PATH="$(readlink -f "$0")"
SCRIPT_DIR="$(dirname "$SCRIPT_PATH")"
GIT_TOPLEVEL=$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel 2>/dev/null)

ROOT_DIR=/root
FHS_DIR=/etc
ORIGIN_DIR=/systemd/system


TEMPLATE_PATH="${GIT_TOPLEVEL}${ROOT_DIR}${FHS_DIR}${ORIGIN_DIR}/${template_file}"
# GENERATE_PATH="${FHS_DIR}${ORIGIN_DIR}/${generate_file}"
GENERATE_PATH="${HOME}/${generate_file}"

# echo ${TEMPLATE_PATH}
# echo ${GENERATE_PATH}


envsubst < "${TEMPLATE_PATH}" > "${GENERATE_PATH}"
