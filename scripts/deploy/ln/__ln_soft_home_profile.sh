#!/usr/bin/bash
set -eu

REPOSITORY_DIR=/repository
DOTFILES_DIR=/dotfiles
ROOT_DIR=/root
FHS_DIR=/home

# deploy .bashrc & .profile
ln -s -b "${HOME}${REPOSITORY_DIR}${DOTFILES_DIR}${ROOT_DIR}${FHS_DIR}/sample.bash_profile"   "${HOME}/.bash_profile"
ln -s -b "${HOME}${REPOSITORY_DIR}${DOTFILES_DIR}${ROOT_DIR}${FHS_DIR}/sample.bashrc"         "${HOME}/.bashrc"
ln -s -b "${HOME}${REPOSITORY_DIR}${DOTFILES_DIR}${ROOT_DIR}${FHS_DIR}/sample.profile"        "${HOME}/.profile"

source "${HOME}/.bash_profile"
