#!/usr/bin/bash
set -eu

SCRIPT_PATH="$(readlink -f "$0")"
SCRIPT_DIR="$(dirname "$SCRIPT_PATH")"

GIT_TOPLEVEL=$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel 2>/dev/null)

ROOT_FHS_DIR=/root/home
TEMP_PATH="${GIT_TOPLEVEL}${ROOT_FHS_DIR}"

while read USER_PROFILE
do
  # echo "${TEMP_PATH}/sample${USER_PROFILE}"
  cp -f -b --suffix=_`date +%Y%m%d_%H%M`  "${TEMP_PATH}/sample${USER_PROFILE}"  "${HOME}/${USER_PROFILE}"

done << edf
  .profile
edf

# source "${HOME}/.bash_profile"
