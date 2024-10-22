#!/usr/bin/bash
set -eu

REPOSITORY_DIR=/repository
DOTFILES_DIR=/dotfiles
ROOT_DIR=/root
FHS_DIR=/home

aaa=".bash_profile"
fff=".bashrc"
rrr=".profile"

while read USER_PROFILE
do
  echo "ln -s -b   "${HOME}${REPOSITORY_DIR}${DOTFILES_DIR}${ROOT_DIR}${FHS_DIR}/sample${USER_PROFILE}"   "${HOME}/${USER_PROFILE}" "

done << edf
  ${aaa}
  ${fff}
  ${rrr}
edf

exit 0

# source "${HOME}/.bash_profile"
