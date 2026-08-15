# !/bin/bash
set -eu


REQUIRED_VARS_ARRAY=(
    # SELFHOSTED_DIRECTORY
    hogefuga
)


selfhost_repo_list=(

    # Mirakurun EPGStation
    "https://github.com/l3tnun/docker-mirakurun-epgstation"

    # tt-rss
    "https://github.com/tt-rss/tt-rss"

)


function check_env(){

    local target_array=("${@}")

    for target_var in "${target_array[@]}"; do
        if [[ ! -v ${target_var} ]]; then
            echo "ERROR: '${target_var}' は未定義です。"
            exit 1
        fi

        if [[ -z ${!target_var} ]]; then
            echo "ERROR: '${target_var}' は空文字です。"
            exit 1
        else
            echo "${target_var} は '${!target_var}' として定義されています。"
        fi
    done

    echo "✅ Required Vars Array is passed"

}


function main(){

    check_env "${REQUIRED_VARS_ARRAY[@]}"
    exit 0

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

        echo "${repo_name}.git"
        # git clone "${repo_name}.git"
    done
}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi