#!/bin/bash
set -eu

desktop=(
  /home/bin
  /home/.config
)

server=(
  /home/.config
  /home/.mozilla
)

ignore_path=(
  /__pycache__
  /systemd/user
)

SCRIPT_PATH="$(readlink -f "$0")"
SCRIPT_DIR="$(dirname "$SCRIPT_PATH")"
GIT_TOPLEVEL=$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel 2>/dev/null)

HOSTNAME="${HOSTNAME:-$(hostname)}"
ROOT_DIR=/root


if  [[ ${HOSTNAME} =~ ^.*desktop$ ]] ; then
  machine_type=("${desktop[@]}")

elif [[ ${HOSTNAME} =~ ^.*server$ ]] ; then
  machine_type=("${server[@]}")

else
  # echo "Invalid argument"
  exit 1

fi


for any_dir in "${machine_type[@]}";
do

  while read get_path
  do

    for ignr in "${ignore_path[@]}";
    do
      if [[ "${get_path}" =~ .*"${ignr}".* ]] ; then
        continue 2
      fi

    done

    echo "${get_path}"

  done < <( find "${GIT_TOPLEVEL}${ROOT_DIR}${any_dir}"  -type f | sort )

done