#!/bin/bash
set -eu

DOTFILES_DIR=/dotfiles/root
ORIGIN_DIR=/etc/samba
TARGET_FILE=99_smb.conf

# hard link config.yaml to netplan
sudo cp --interactive \
  ${HOME}${DOTFILES_DIR}${ORIGIN_DIR}/sample.${TARGET_FILE} \
  ${ORIGIN_DIR}/${TARGET_FILE}