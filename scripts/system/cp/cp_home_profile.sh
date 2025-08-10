#!/usr/bin/bash
set -eu

# スクリプト自身の絶対パスを取得（シンボリックリンクにも対応）
SCRIPT_PATH="$(readlink -f "$0")"
SCRIPT_DIR="$(dirname "$SCRIPT_PATH")"

# スクリプトが属するGitリポジトリのトップレベルを取得
GIT_TOPLEVEL=$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel 2>/dev/null)

ROOT_DIR=/root
FHS_DIR=/home

TEMP_PATH="${GIT_TOPLEVEL}${ROOT_DIR}${FHS_DIR}"

while read USER_PROFILE
do

  LOCAL_DIR="${HOME}/${USER_PROFILE}"

  # if    [[ ! -f "${LOCAL_DIR}"  ]] ; then
  #   cp     "${TEMP_PATH}/sample${USER_PROFILE}"   "${HOME}/${USER_PROFILE}"

  # elif  [[ -L "${LOCAL_DIR}"  ]] ; then
  #   cp -f  "${TEMP_PATH}/sample${USER_PROFILE}"   "${HOME}/${USER_PROFILE}"

  # elif  [[ ! -L "${LOCAL_DIR}"  ]] ; then
  #   cp -b  "${TEMP_PATH}/sample${USER_PROFILE}"   "${HOME}/${USER_PROFILE}"

  # fi

  # cp -b  "${TEMP_PATH}/sample${USER_PROFILE}"   "${HOME}/${USER_PROFILE}"
  cp  -b  --suffix=_`date +%Y%m%d_%H%M` "${TEMP_PATH}/sample${USER_PROFILE}"   "${HOME}/${USER_PROFILE}"

  # echo "ln -s   "${TEMP_PATH}/sample${USER_PROFILE}"   "${HOME}/${USER_PROFILE}" "

done << edf
  .profile
edf

exit 0

# source "${HOME}/.bash_profile"
