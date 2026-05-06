# !/bin/bash
set -eu

cd ${HOME}/repository


container_repo_list=(

    # Mirakurun EPGStation
    "https://github.com/l3tnun/docker-mirakurun-epgstation"

    # # qbittorrent-nox
    # https://github.com/qbittorrent/docker-qbittorrent-nox

    # tt-rss
    "https://github.com/tt-rss/tt-rss"

)


function main(){
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