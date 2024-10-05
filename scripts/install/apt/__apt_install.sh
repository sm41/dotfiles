# !/bin/bash
set -eu

if [[ ! $1 =~ ^(server|client)$  ]] ; then
  echo "wrong argument"
  exit 1
fi

input_file=apt_packages_${1}.txt
work_path=$(cd $(dirname $0) && pwd)

sudo apt-get update
sudo apt-get upgrade

while read package_name
do

  [ -z ${package_name} ] && continue
  [ ${package_name::1} = "#" ] && continue

  sudo apt-get install --no-install-recommends ^${package_name}$

done < ${work_path}/${input_file}