# !/bin/bash
set -eu

work_path="$(realpath $(dirname "$0"))"
input_file="docker_repo_list.sh"


# cd ${HOME}/repository

while read repo_name
do
  [[ -z "${repo_name}" ]] && continue
  [[ "${repo_name::1}" = "#" ]] && continue

  # git clone "${repo_name}.git"
  echo "${repo_name}.git"

done < "${work_path}/${input_file}"