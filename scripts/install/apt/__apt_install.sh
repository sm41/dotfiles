#!/bin/bash
set -eu

input_file=apt_packages_${1}.txt
work_path=$(cd $(dirname $0) && pwd)

# sudo apt update
# sudo apt upgrade

while read package_name
do
  [ -z ${package_name} ] && continue
  [ ${package_name::1} = "#" ] && continue

  sudo apt install --no-install-recommends ^${package_name}$

done < ${work_path}/${input_file}