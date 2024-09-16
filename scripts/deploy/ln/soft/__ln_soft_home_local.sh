#!/bin/bash
set -eu

DOTFILES_DIR=/dotfiles/root/home

# ${HOME}/.local symbolic link
while read DOT_LOCAL
do
  LOCAL_DIR=${DOT_LOCAL/${DOTFILES_DIR}}
  mkdir --parents ${LOCAL_DIR%/*}
  # echo "${DOT_LOCAL}  ===>   ${LOCAL_DIR}"
  ln --symbolic --force ${DOT_LOCAL}   ${LOCAL_DIR}

done < <( find ${HOME}${DOTFILES_DIR}/.local -not \( -path "*/__pycache__/*" \) -type f | sort )