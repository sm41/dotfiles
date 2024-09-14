#!/bin/bash
set -eu

DOTFILES_DIR=/dotfiles/root/home

# ${HOME}/.config symbolic link
while read DOT_CONFIG
do
  CONFIG_DIR=${DOT_CONFIG/${DOTFILES_DIR}}
  mkdir --parents ${CONFIG_DIR%/*}
  # echo "${DOT_CONFIG}  ===>   ${CONFIG_DIR}"
  ln --symbolic --force ${DOT_CONFIG}  ${CONFIG_DIR}
done < <( find ${HOME}${DOTFILES_DIR}/.config -not \( -path "*/systemd/*" \) -type f | sort )