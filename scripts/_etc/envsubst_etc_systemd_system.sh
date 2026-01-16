#!/bin/bash
set -eu


# lsblk -dno UUID | awk 'NF'
# lsblk -o NAME,SIZE,FSTYPE,UUID,LABEL,PARTUUID,PARTLABEL,MOUNTPOINT

# -d, --nodeps         スレーブデバイスやホルダーを表示しません
# -n, --noheadings     ヘッダを表示しません
# -o, --output <list>  出力する列を指定します


function desktop(){
  temp_path="${CLIENT_NETWORK_STORAGE_misc#/}"
  template_file="template.mnt-samba-xxx.mount"
}

function server(){
  temp_path="${SERVER_LOCAL_STORAGE_misc#/}"
  template_file="template.mnt-local-xxx.mount"
  export UUID=""
}

if  [[ ${HOSTNAME} =~ ^.*desktop$ ]] ; then
  desktop
elif [[ ${HOSTNAME} =~ ^.*server$ ]] ; then
  server
else
  # echo "Invalid argument"
  exit 1
fi

redefinition_path="${temp_path//\//-}"
generate_file="${redefinition_path}.mount"

SCRIPT_PATH="$(readlink -f "$0")"
SCRIPT_DIR="$(dirname "$SCRIPT_PATH")"

# HOSTNAME="${HOSTNAME:-$(hostname)}"
if ! GIT_TOPLEVEL=$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel 2>/dev/null); then
  echo "Error: script is not inside a git repository" >&2
  exit 1
fi

ROOT_DIR=/root
FHS_ORIGIN_DIR=/etc/systemd/system

TEMPLATE_PATH="${GIT_TOPLEVEL}${ROOT_DIR}${FHS_ORIGIN_DIR}/${template_file}"
GENERATE_PATH="${FHS_ORIGIN_DIR}/${generate_file}"

if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
  echo ${TEMPLATE_PATH}
  echo ${GENERATE_PATH}
  # envsubst < "${TEMPLATE_PATH}" | sudo tee "${GENERATE_PATH}" > /dev/null
fi