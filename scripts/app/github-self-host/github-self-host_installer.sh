# !/bin/bash
set -eu


required_vars=(
    SELFHOSTED_DIRECTORY
)

selfhost_repo_list=(

    # Mirakurun EPGStation
    "https://github.com/l3tnun/docker-mirakurun-epgstation"

    # tt-rss
    "https://github.com/tt-rss/tt-rss"

)

function main(){

    for var in "${required_vars[@]}"; do
        if [[ ! -v $var ]]; then
            echo "ERROR: '$var' が未定義です。"
            exit 1
        fi

        if [[ -z ${!var} ]]; then
            echo "ERROR: '$var' は空文字です。"
            exit 1
        fi
    done



    selfhot_directory="${HOME}/self-host"
    # selfhot_directory="${SELFHOSTED_DIRECTORY}"

    if [[ ! -d "${selfhot_directory}" ]]; then
        mkdir  "${selfhot_directory}"
    fi

    cd "${selfhot_directory}"

    for repo_name in "${selfhost_repo_list[@]}"
    do
        [[ -z "${repo_name}" ]] && continue
        [[ "${repo_name::1}" = "#" ]] && continue

        # echo "${repo_name}.git"
        git clone "${repo_name}.git"
    done
}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi