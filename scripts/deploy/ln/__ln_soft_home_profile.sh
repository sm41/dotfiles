#!/usr/bin/bash
set -eu

REPOSITORY_DIR=/repository
DOTFILES_DIR=/dotfiles
ROOT_DIR=/root
FHS_DIR=/home

TEMP_PATH="${HOME}${REPOSITORY_DIR}${DOTFILES_DIR}${ROOT_DIR}${FHS_DIR}"

aaa=".bash_profile"
fff=".bashrc"
rrr=".profile"

while read USER_PROFILE
do

  if    [[ ! -e "${LOCAL_DIR}"  ]] ; then
    ln -s     "${TEMP_PATH}/sample${USER_PROFILE}"   "${HOME}/${USER_PROFILE}"

  elif  [[ -L "${LOCAL_DIR}"  ]] ; then
    ln -s -f  "${TEMP_PATH}/sample${USER_PROFILE}"   "${HOME}/${USER_PROFILE}"

  elif  [[ ! -L "${LOCAL_DIR}"  ]] ; then
    ln -s -b  "${TEMP_PATH}/sample${USER_PROFILE}"   "${HOME}/${USER_PROFILE}"

  fi

  # echo "ln -s   "${TEMP_PATH}/sample${USER_PROFILE}"   "${HOME}/${USER_PROFILE}" "


done << edf
  ${aaa}
  ${fff}
  ${rrr}
edf

exit 0

# source "${HOME}/.bash_profile"
