#!/bin/bash
set -eu

DOTFILES_DIR=/dotfiles/root/home

# ${HOME}/.config hard link
while read SYSTEMD_JOB
do
  JOB_DIR=${SYSTEMD_JOB/${DOTFILES_DIR}}
  mkdir --parents ${JOB_DIR%/*}
  # echo "${SYSTEMD_JOB}  ===>  ${JOB_DIR}"
  ln --force ${SYSTEMD_JOB}    ${JOB_DIR}
done < <(find ${HOME}${DOTFILES_DIR}/.config/systemd/user -type f | sort)

