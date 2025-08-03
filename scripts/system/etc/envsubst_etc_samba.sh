#!/bin/bash
set -eu


# https://wiki.archlinux.jp/index.php/Samba


# lsblk -dno UUID | awk 'NF'
# lsblk -o NAME,SIZE,FSTYPE,UUID,LABEL,PARTUUID,PARTLABEL,MOUNTPOINT

# -d, --nodeps         スレーブデバイスやホルダーを表示しません
# -n, --noheadings     ヘッダを表示しません
# -o, --output <list>  出力する列を指定します


function desktop(){
  export SAMBA_MOUNT_PATH="${CLIENT_NETWORK_STORAGE_misc}"
}

function server(){
  export SAMBA_MOUNT_PATH="${SERVER_LOCAL_STORAGE_misc}"
}

HOSTNAME="${HOSTNAME:-$(hostname)}"
config_file="smb.conf"
credentials_file="credentials"

temp_conf_file="template.${config_file}"
temp_cred_file="template.${credentials_file}"

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
ORIGIN_DIR=/samba

# sudo mkdir -p "${FHS_DIR}${ORIGIN_DIR}"

TEMPLATE_CONF_PATH="${GIT_TOPLEVEL}${ROOT_DIR}${FHS_DIR}${ORIGIN_DIR}/${temp_conf_file}"
TEMPLATE_CRED_PATH="${GIT_TOPLEVEL}${ROOT_DIR}${FHS_DIR}${ORIGIN_DIR}/${temp_cred_file}"

# GENERATE_CONF_PATH="${HOME}/${config_file}"
# GENERATE_CRED_PATH="${HOME}/${credentials_file}"
GENERATE_CONF_PATH="${FHS_DIR}${ORIGIN_DIR}/${config_file}"
GENERATE_CRED_PATH="${FHS_DIR}${ORIGIN_DIR}/${credentials_file}"

echo ${TEMPLATE_CONF_PATH}
echo ${TEMPLATE_CRED_PATH}

echo ${GENERATE_CONF_PATH}
echo ${GENERATE_CRED_PATH}


# envsubst < "${TEMPLATE_CONF_PATH}" > "${GENERATE_CONF_PATH}"
# envsubst < "${TEMPLATE_CRED_PATH}" > "${GENERATE_CRED_PATH}"
