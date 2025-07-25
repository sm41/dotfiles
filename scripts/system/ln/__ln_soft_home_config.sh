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
XDG_DIR=/.config

# ${HOME}/.config symbolic link
while read DOT_CONFIG
do
  CONFIG_DIR="${HOME}${DOT_CONFIG/${GIT_TOPLEVEL}${ROOT_DIR}${FHS_DIR}}"
  mkdir -p "${CONFIG_DIR%/*}"

  # if    [[ ! -e "${CONFIG_DIR}"  ]] ; then
  #   ln -s "${DOT_CONFIG}"  "${CONFIG_DIR}"

  # elif  [[ -L "${CONFIG_DIR}"  ]] ; then
  #   ln -s -f "${DOT_CONFIG}"  "${CONFIG_DIR}"

  # elif  [[ ! -L "${CONFIG_DIR}"  ]] ; then
  #   ln -s -b "${DOT_CONFIG}"  "${CONFIG_DIR}"

  # fi

  echo "${DOT_CONFIG}  ===>   ${CONFIG_DIR}"

done < <( find "${GIT_TOPLEVEL}${ROOT_DIR}${FHS_DIR}${XDG_DIR}" -not \( -path "*/systemd/user*" \) -type f | sort )