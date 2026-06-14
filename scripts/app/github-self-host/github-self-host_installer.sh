# !/bin/bash
set -eu

selfhost_repo_list=(

    # Mirakurun EPGStation
    "https://github.com/l3tnun/docker-mirakurun-epgstation"

    # tt-rss
    "https://github.com/tt-rss/tt-rss"

)

function main(){

    if [[ ! -d "${HOME}/self-host" ]]; then
        mkdir  "${HOME}/self-host"
    fi

    cd ${HOME}/self-host

    for repo_name in "${selfhost_repo_list[@]}"
    do
        [[ -z "${repo_name}" ]] && continue
        [[ "${repo_name::1}" = "#" ]] && continue

        echo "${repo_name}.git"
        # git clone "${repo_name}.git"
    done
}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi