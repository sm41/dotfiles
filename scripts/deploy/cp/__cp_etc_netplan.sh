#!/bin/bash
set -eu

DOTFILES_DIR=/dotfiles/root
ORIGIN_DIR=/etc/netplan


while read hogefuga
do
  sudo cp --interactive --backup=numbered \
    ${HOME}${DOTFILES_DIR}${ORIGIN_DIR}/${hogefuga} \
    ${ORIGIN_DIR}/${hogefuga#sample.*}

done < <(find ${HOME}${DOTFILES_DIR}${ORIGIN_DIR} -type f -printf '%f\n' | sort )