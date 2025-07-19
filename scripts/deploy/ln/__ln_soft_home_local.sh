#!/bin/bash
set -eu

# スクリプト自身の絶対パスを取得（シンボリックリンクにも対応）
SCRIPT_PATH="$(readlink -f "$0")"
SCRIPT_DIR="$(dirname "$SCRIPT_PATH")"

# スクリプトが属するGitリポジトリのトップレベルを取得
GIT_TOPLEVEL=$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel 2>/dev/null)

if [ $? -ne 0 ]; then
  echo "このスクリプトは Git リポジトリの中にありません。"
  exit 1
fi


ROOT_DIR=/root
FHS_DIR=/home
XDG_DIR=/.local

# ${HOME}/.local symbolic link
while read DOT_LOCAL
do
  LOCAL_DIR="${HOME}${DOT_LOCAL/${GIT_TOPLEVEL}${ROOT_DIR}${FHS_DIR}}"
  mkdir -p "${LOCAL_DIR%/*}"

  # if    [[ ! -e "${LOCAL_DIR}"  ]] ; then
  #   ln -s "${DOT_LOCAL}"  "${LOCAL_DIR}"

  # elif  [[ -L "${LOCAL_DIR}"  ]] ; then
  #   ln -s -f "${DOT_LOCAL}"  "${LOCAL_DIR}"

  # elif  [[ ! -L "${LOCAL_DIR}"  ]] ; then
  #   ln -s -b "${DOT_LOCAL}"  "${LOCAL_DIR}"

  # fi

  echo "${DOT_LOCAL}  ===>   ${LOCAL_DIR}"

done < <( find "${GIT_TOPLEVEL}${ROOT_DIR}${FHS_DIR}${XDG_DIR}" -type f | sort )