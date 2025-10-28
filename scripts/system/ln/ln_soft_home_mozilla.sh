#!/bin/bash
set -eu

# スクリプト自身の絶対パスを取得（シンボリックリンクにも対応）
SCRIPT_PATH="$(readlink -f "$0")"
SCRIPT_DIR="$(dirname "$SCRIPT_PATH")"

# スクリプトが属するGitリポジトリのトップレベルを取得
GIT_TOPLEVEL=$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel 2>/dev/null)

ROOT_FHS_DIR=/root/home
ORIGIN_DIR=/.mozilla/firefox
PROFILE_DIR=/"$(find "${HOME}${ORIGIN_DIR}" -maxdepth 1 -type d -path "*default-release" -printf '%f\n')"

# mkdir -p "${HOME}${ORIGIN_DIR}${PROFILE_DIR}/chrome"

while read FENNEC
do
  Intermediate="${FENNEC/${GIT_TOPLEVEL}${ROOT_FHS_DIR}}"
  processed_path="${HOME}${Intermediate/"/default-release"/${PROFILE_DIR}}"

  # ln -s -f "${FENNEC}"  "${processed_path}"
  echo "${FENNEC}  ===>  ${processed_path}"

done < <( find "${GIT_TOPLEVEL}${ROOT_FHS_DIR}${ORIGIN_DIR}" -type f | sort)