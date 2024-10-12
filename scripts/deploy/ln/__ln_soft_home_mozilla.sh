#!/bin/bash
set -eu

DOTFILES_DIR=/dotfiles/root/home
ORIGIN_DIR=/.mozilla/firefox
PROFILE_DIR=/$(find "${HOME}${ORIGIN_DIR}" -maxdepth 1 -type d -path "*default-release" -printf '%f\n' )

mkdir --parents ${HOME}${ORIGIN_DIR}${PROFILE_DIR}/chrome

while read FENNEC
do
  Intermediate=${FENNEC/${DOTFILES_DIR}}
  processed_path=${Intermediate/"/default-release"/${PROFILE_DIR}}
  # echo "${FENNEC}  ===>  ${processed_path}"
  ln --symbolic --force ${FENNEC}  ${processed_path}

done < <( find ${HOME}${DOTFILES_DIR}${ORIGIN_DIR} -type f | sort)