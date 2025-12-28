#!/bin/bash
set -eu

# スクリプト自身の絶対パスを取得（シンボリックリンクにも対応）
SCRIPT_PATH="$(readlink -f "$0")"
SCRIPT_DIR="$(dirname "$SCRIPT_PATH")"

# スクリプトが属するGitリポジトリのトップレベルを取得
GIT_TOPLEVEL=$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel 2>/dev/null)

ROOT_FHS_DIR=/root/home
XDG_DIR=/.config




while read DOT_CONFIG
do
  CONFIG_DIR="${HOME}${DOT_CONFIG/${GIT_TOPLEVEL}${ROOT_FHS_DIR}}"
  # mkdir -p "${CONFIG_DIR%/*}"

  # ln -s -f "${DOT_CONFIG}"  "${CONFIG_DIR}"
  echo "${DOT_CONFIG}  ===>   ${CONFIG_DIR}"

done < <( find "${GIT_TOPLEVEL}${ROOT_FHS_DIR}${XDG_DIR}" -not \( -path "*/systemd/user*" \) -type f | sort )