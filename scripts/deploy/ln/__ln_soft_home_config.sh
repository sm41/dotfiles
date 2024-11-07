#!/bin/bash
set -eu

REPOSITORY_DIR=/repository
DOTFILES_DIR=/dotfiles
ROOT_DIR=/root
FHS_DIR=/home
XDG_DIR=/.config

# ${HOME}/.config symbolic link
while read DOT_CONFIG
do
  CONFIG_DIR="${DOT_CONFIG/${REPOSITORY_DIR}${DOTFILES_DIR}${ROOT_DIR}${FHS_DIR}}"
  mkdir -p "${CONFIG_DIR%/*}"

  if    [[ ! -e "${CONFIG_DIR}"  ]] ; then
    ln -s "${DOT_CONFIG}"  "${CONFIG_DIR}"

  elif  [[ -L "${CONFIG_DIR}"  ]] ; then
    ln -s -f "${DOT_CONFIG}"  "${CONFIG_DIR}"

  elif  [[ ! -L "${CONFIG_DIR}"  ]] ; then
    ln -s -b "${DOT_CONFIG}"  "${CONFIG_DIR}"

  fi

  # echo "${DOT_CONFIG}  ===>   ${CONFIG_DIR}"

done < <( find "${HOME}${REPOSITORY_DIR}${DOTFILES_DIR}${ROOT_DIR}${FHS_DIR}${XDG_DIR}" -not \( -path "*/systemd/user*" \) -type f | sort )