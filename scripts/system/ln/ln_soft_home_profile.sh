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

  # if    [[ ! -e "${LOCAL_DIR}"  ]] ; then
  #   ln -s     "${TEMP_PATH}/sample${USER_PROFILE}"   "${HOME}/${USER_PROFILE}"

  # elif  [[ -L "${LOCAL_DIR}"  ]] ; then
  #   ln -s -f  "${TEMP_PATH}/sample${USER_PROFILE}"   "${HOME}/${USER_PROFILE}"

  # elif  [[ ! -L "${LOCAL_DIR}"  ]] ; then
  #   ln -s -b  "${TEMP_PATH}/sample${USER_PROFILE}"   "${HOME}/${USER_PROFILE}"

  # fi

  echo "ln -s   "${TEMP_PATH}/sample${USER_PROFILE}"   "${HOME}/${USER_PROFILE}" "

done << edf
  ".bash_profile"
  ".bashrc"
  ".profile"
edf

exit 0

# source "${HOME}/.bash_profile"
