# !/bin/bash
set -eu




work_path="$(realpath $(dirname "$0"))"
input_file="uv_tool_package.txt"


while read package_name
do

    [ -z "${package_name}" ] && continue
    [ "${package_name::1}" = "#" ] && continue

    uv tool install "${package_name}"

done < "${work_path}/${input_file}"