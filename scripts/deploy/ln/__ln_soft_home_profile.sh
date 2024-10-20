#!/usr/bin/bash
set -eu

REPOSITORY_DIR=/repository
DOTFILES_DIR=/dotfiles
ROOT_DIR=/root
FHS_DIR=/home

# deploy .bashrc & .profile

while read USER_PROFILE
do
  # echo "${USER_PROFILE}"
  echo ""${HOME}${REPOSITORY_DIR}${DOTFILES_DIR}${ROOT_DIR}${FHS_DIR}/${USER_PROFILE}"   "${HOME}/${USER_PROFILE#sample*}" "

done < <( find "${HOME}${REPOSITORY_DIR}${DOTFILES_DIR}${ROOT_DIR}${FHS_DIR}"  -maxdepth 1  -name "sample*"  -type f -printf '%f\n' | sort )

# source "${HOME}/.bash_profile"
