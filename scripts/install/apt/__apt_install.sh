# !/bin/bash
set -eu

work_path="$(realpath $(dirname "$0"))"
input_file="$(find ${work_path}  -not \( -path $0 \)  -type f  -printf "%f\n")"

sudo apt-get update
sudo apt-get upgrade

while read package_name
do

  [ -z "${package_name}" ] && continue
  [ "${package_name::1}" = "#" ] && continue

  sudo apt-get install --no-install-recommends ^"${package_name}"$

done < "${work_path}/${input_file}"