#!/bin/bash
set -eu


# lsblk -dno UUID | awk 'NF'
# lsblk -o NAME,SIZE,FSTYPE,UUID,LABEL,PARTUUID,PARTLABEL,MOUNTPOINT

# -d, --nodeps         スレーブデバイスやホルダーを表示しません
# -n, --noheadings     ヘッダを表示しません
# -o, --output <list>  出力する列を指定します


function desktop(){
  temp_path="${CLIENT_NETWORK_STORAGE_misc#/}"
  redefinition_path="${temp_path//\//-}"

  generate_file="${redefinition_path}.mount"
  template_file="template.mnt-samba-xxx.mount"
}

function server(){
  temp_path="${SERVER_LOCAL_STORAGE_misc#/}"
  redefinition_path="${temp_path//\//-}"

  generate_file="${redefinition_path}.mount"
  template_file="template.mnt-local-xxx.mount"

  export UUID=""

}


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
SCRIPT_DIR="$(dirname "$SCRIPT_PATH")"
GIT_TOPLEVEL=$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel 2>/dev/null)

ROOT_DIR=/root
FHS_DIR=/etc
ORIGIN_DIR=/systemd/system


TEMPLATE_PATH="${GIT_TOPLEVEL}${ROOT_DIR}${FHS_DIR}${ORIGIN_DIR}/${template_file}"
# GENERATE_PATH="${FHS_DIR}${ORIGIN_DIR}/${generate_file}"
GENERATE_PATH="${HOME}/${generate_file}"

echo ${TEMPLATE_PATH}
echo ${GENERATE_PATH}


# envsubst < "${TEMPLATE_PATH}" > "${GENERATE_PATH}"
