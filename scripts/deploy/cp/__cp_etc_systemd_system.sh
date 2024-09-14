#!/bin/bash
set -eu

DOTFILES_DIR=/dotfiles/root
ORIGIN_DIR=/etc/systemd/system
TARGET_FILE=mnt-640G.mount

# hard link config.yaml to sysctl.d
sudo cp --interactive \
  ${HOME}${DOTFILES_DIR}${ORIGIN_DIR}/${TARGET_FILE} \
  ${ORIGIN_DIR}/${TARGET_FILE}