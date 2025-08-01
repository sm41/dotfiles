# !/bin/bash
set -eu

if [ $# -lt 1 ]; then
  echo "Usage: $0 [ desktop | server ]"
  exit 1

elif [[ "$1" == "desktop" || "$1" == "server" ]] ; then
  type="apt_packages_${1}.sh"

else
  echo "Invalid argument"
  exit 1
fi

work_path="$(realpath $(dirname "$0"))"
input_file="$(find ${work_path}  -name ${type}   -not \( -path $0 \)  -type f  -printf "%f\n")"


# sudo apt-get update

while read package_name
do
  [ -z "${package_name}" ] && continue
  [ "${package_name::1}" = "#" ] && continue

  echo "${package_name}"
  # sudo apt-get install --no-install-recommends ^"${package_name}"$

done < "${work_path}/${input_file}"