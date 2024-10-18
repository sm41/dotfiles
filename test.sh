#!/usr/bin/bash
set -eu

AAA="$(cd $(dirname "$0") && pwd)"
BBB="$(realpath "$(dirname "$0")")"
CCC="$(readlink -f "$(dirname "$0")")"
ddd=$(cd $(dirname "$0") && pwd)

echo "$0"
echo "${BASH_SOURCE:-"$0"}"
echo ------
realpath "$0"
realpath "${BASH_SOURCE}"
realpath "${BASH_SOURCE:-"$0"}"
echo ------
echo "${AAA}"
echo "${BBB}"
echo "${CCC}"
echo ------

echo "${GITHUB_WORKSPACE}"
echo "${HOME}"


