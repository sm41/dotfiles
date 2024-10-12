# !/bin/bash
set -eu

input_file=apt_packages.txt
work_path=$(realpath $(dirname "$0"))

sudo apt-get update
sudo apt-get upgrade

while read package_name
do

  [ -z ${package_name} ] && continue
  [ ${package_name::1} = "#" ] && continue

  sudo apt-get install --no-install-recommends ^${package_name}$

done < ${work_path}/${input_file}