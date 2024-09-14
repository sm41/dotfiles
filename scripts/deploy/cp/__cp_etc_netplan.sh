#!/bin/bash
set -eu

DOTFILES_DIR=/dotfiles/root
ORIGIN_DIR=/etc/netplan
TARGET_FILE=99_config.yaml

# hard link config.yaml to netplan
sudo cp --interactive \
  ${HOME}${DOTFILES_DIR}${ORIGIN_DIR}/${TARGET_FILE} \
  ${ORIGIN_DIR}/${TARGET_FILE}