#!/bin/bash
set -eu

REPOSITORY_DIR=/repository
DOTFILES_DIR=/dotfiles
ROOT_DIR=/root
FHS_DIR=/etc
ORIGIN_DIR=/netplan


while read hogefuga
do
  sudo cp \
    --interactive \
    --backup=numbered \
    ${HOME}${REPOSITORY_DIR}${DOTFILES_DIR}${ROOT_DIR}${FHS_DIR}${ORIGIN_DIR}/${hogefuga} \
    ${FHS_DIR}${ORIGIN_DIR}/${hogefuga#sample.*}

done < <(find ${HOME}${REPOSITORY_DIR}${DOTFILES_DIR}${ROOT_DIR}${FHS_DIR}${ORIGIN_DIR} -type f -printf '%f\n' | sort )