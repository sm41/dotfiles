# !/bin/bash
set -eu

# cd ${HOME}/repository

function main(){
    work_path="$(realpath $(dirname "$0"))"
    input_file="container_repo_list.sh"

    while read repo_name
    do
        [[ -z "${repo_name}" ]] && continue
        [[ "${repo_name::1}" = "#" ]] && continue
        # git clone "${repo_name}.git"
        echo "${repo_name}.git"
    done < "${work_path}/${input_file}"
}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi