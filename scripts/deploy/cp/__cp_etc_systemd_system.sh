#!/bin/bash
set -eu

DOTFILES_DIR=/dotfiles/root
ORIGIN_DIR=/etc/systemd/system
TARGET_FILE=mnt-path.mount

# hard link config.yaml to systemd unit
sudo cp --interactive \
  ${HOME}${DOTFILES_DIR}${ORIGIN_DIR}/sample.${TARGET_FILE} \
  ${ORIGIN_DIR}/${TARGET_FILE}