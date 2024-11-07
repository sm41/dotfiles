#!/bin/bash
set -eu

REPOSITORY_DIR=/repository
DOTFILES_DIR=/dotfiles
ROOT_DIR=/root
FHS_DIR=/home
ORIGIN_DIR=/.mozilla/firefox
PROFILE_DIR=/"$(find "${HOME}${ORIGIN_DIR}" -maxdepth 1 -type d -path "*default-release" -printf '%f\n')"

mkdir -p "${HOME}${ORIGIN_DIR}${PROFILE_DIR}/chrome"

while read FENNEC
do
  Intermediate="${FENNEC/${REPOSITORY_DIR}${DOTFILES_DIR}${ROOT_DIR}${FHS_DIR}}"
  processed_path="${Intermediate/"/default-release"/${PROFILE_DIR}}"

  if    [[ ! -e "${processed_path}"  ]] ; then
    ln -s "${FENNEC}"  "${processed_path}"

  elif  [[ -L "${processed_path}"  ]] ; then
    ln -s -f "${FENNEC}"  "${processed_path}"

  elif  [[ ! -L "${processed_path}"  ]] ; then
    ln -s -b "${FENNEC}"  "${processed_path}"

  fi

  # echo "${FENNEC}  ===>  ${processed_path}"

done < <( find "${HOME}${REPOSITORY_DIR}${DOTFILES_DIR}${ROOT_DIR}${FHS_DIR}${ORIGIN_DIR}" -type f | sort)