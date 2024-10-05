#!/bin/bash
set -eu

DOTFILES_DIR=/dotfiles/root/home




# ${HOME}/.config symbolic link
while read bin_file
do
  homebin=${bin_file/${DOTFILES_DIR}}
  mkdir --parents ${homebin%/*}
  # echo "${bin_file}  ===>   ${homebin}"
  ln --symbolic --force ${bin_file}  ${homebin}

done < <( find ${HOME}${DOTFILES_DIR}/bin -type f | sort )