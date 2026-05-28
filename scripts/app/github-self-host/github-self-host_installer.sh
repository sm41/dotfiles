# !/bin/bash
set -eu

container_repo_list=(

    # Mirakurun EPGStation
    "https://github.com/l3tnun/docker-mirakurun-epgstation"

    # tt-rss
    "https://github.com/tt-rss/tt-rss"

)

function main(){

    if [[ ! -d "${HOME}/repository" ]]; then
        mkdir  "${HOME}/repository"
    fi

    cd ${HOME}/repository

    for repo_name in "${container_repo_list[@]}"
    do
        [[ -z "${repo_name}" ]] && continue
        [[ "${repo_name::1}" = "#" ]] && continue
        # git clone "${repo_name}.git"
        echo "${repo_name}.git"
    done
}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi