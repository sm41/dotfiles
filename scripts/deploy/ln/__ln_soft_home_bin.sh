#!/bin/bash
set -eu

REPOSITORY_DIR=/repository
DOTFILES_DIR=/dotfiles
ROOT_DIR=/root
FHS_DIR=/home
XDG_DIR=/bin

# ${HOME}/.config symbolic link
while read BIN_FILE
do
  HOME_BIN="${BIN_FILE/${REPOSITORY_DIR}${DOTFILES_DIR}${ROOT_DIR}${FHS_DIR}}"
  mkdir -p "${HOME_BIN%/*}"

  if    [[ ! -e "${HOME_BIN}"  ]] ; then
    ln -s "${BIN_FILE}"  "${HOME_BIN}"

  elif  [[ -L "${HOME_BIN}"  ]] ; then
    ln -s -f "${BIN_FILE}"  "${HOME_BIN}"

  elif  [[ ! -L "${HOME_BIN}"  ]] ; then
    ln -s -b "${BIN_FILE}"  "${HOME_BIN}"

  fi

  # echo "${BIN_FILE}  ===>   ${HOME_BIN}"

done < <( find "${HOME}${REPOSITORY_DIR}${DOTFILES_DIR}${ROOT_DIR}${FHS_DIR}${XDG_DIR}" -not \( -path "*/__pycache__/*" \) -type f | sort )