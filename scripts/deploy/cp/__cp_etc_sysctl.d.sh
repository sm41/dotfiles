#!/bin/bash
set -eu

DOTFILES_DIR=/dotfiles/root
ORIGIN_DIR=/etc/sysctl.d
TARGET_FILE=77-ipv6-privacy.conf

# hard link config.yaml to sysctl.d
sudo cp --interactive \
  ${HOME}${DOTFILES_DIR}${ORIGIN_DIR}/${TARGET_FILE} \
  ${ORIGIN_DIR}/${TARGET_FILE}