# !/bin/bash
set -eu

# input samba user
echo    "[ 📢  create {samba user} ]"
read -p "・Input \"samba user\"  ==>  "  SAMBA_USER

# create user
# sudo adduser  --system  --no-create-home  --disabled-login   "${SAMBA_USER}"
echo  "sudo adduser  --system  --no-create-home  --disabled-login   "${SAMBA_USER}"  "

# Register user and set password in Samba
# sudo pdbedit -a -u "${SAMBA_USER}"
echo  "sudo pdbedit -a -u "${SAMBA_USER}"  "
