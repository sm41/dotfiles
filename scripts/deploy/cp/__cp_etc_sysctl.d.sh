#!/bin/bash
set -eu

DOTFILES_DIR=/dotfiles/root
ORIGIN_DIR=/etc/sysctl.d


while read ipv6_conf
do
  sudo cp --interactive --backup=numbered \
    ${HOME}${DOTFILES_DIR}${ORIGIN_DIR}/${ipv6_conf} \
    ${ORIGIN_DIR}/${ipv6_conf#sample.*}

done < <(find ${HOME}${DOTFILES_DIR}${ORIGIN_DIR} -type f -printf '%f\n' | sort )