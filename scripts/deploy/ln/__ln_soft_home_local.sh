#!/bin/bash
set -eu

REPOSITORY_DIR=/repository
DOTFILES_DIR=/dotfiles
ROOT_DIR=/root
FHS_DIR=/home
XDG_DIR=/.local

# ${HOME}/.local symbolic link
while read DOT_LOCAL
do
  LOCAL_DIR="${DOT_LOCAL/${REPOSITORY_DIR}${DOTFILES_DIR}${ROOT_DIR}${FHS_DIR}}"
  mkdir -p "${LOCAL_DIR%/*}"

  if    [[ ! -e "${LOCAL_DIR}"  ]] ; then
    ln -s "${DOT_LOCAL}"  "${LOCAL_DIR}"

  elif  [[ -L "${LOCAL_DIR}"  ]] ; then
    ln -s -f "${DOT_LOCAL}"  "${LOCAL_DIR}"

  elif  [[ ! -L "${LOCAL_DIR}"  ]] ; then
    ln -s -b "${DOT_LOCAL}"  "${LOCAL_DIR}"

  fi

  # echo "${DOT_LOCAL}  ===>   ${LOCAL_DIR}"

done < <( find "${HOME}${REPOSITORY_DIR}${DOTFILES_DIR}${ROOT_DIR}${FHS_DIR}${XDG_DIR}" -type f | sort )