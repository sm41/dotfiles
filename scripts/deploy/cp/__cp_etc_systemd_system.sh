#!/bin/bash
set -eu

DOTFILES_DIR=/dotfiles/root
ORIGIN_DIR=/etc/systemd/system


while read unit_file
do
  sudo cp --interactive \
    ${HOME}${DOTFILES_DIR}${ORIGIN_DIR}/${unit_file} \
    ${ORIGIN_DIR}/${unit_file#sample.*}

done < <(find ${HOME}${DOTFILES_DIR}${ORIGIN_DIR} -type f -printf '%f\n' | sort )
