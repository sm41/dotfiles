#!/bin/bash
set -eu

DOTFILES_DIR=/dotfiles/root
ORIGIN_DIR=/etc/samba


while read piyopiyo
do
  sudo cp --interactive --backup=numbered \
    ${HOME}${DOTFILES_DIR}${ORIGIN_DIR}/${piyopiyo} \
    ${ORIGIN_DIR}/${piyopiyo#sample.*}

done < <(find ${HOME}${DOTFILES_DIR}${ORIGIN_DIR} -type f -printf '%f\n' | sort )