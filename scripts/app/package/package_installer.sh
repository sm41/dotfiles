# !/bin/bash
set -eu

common_application=(
    git
    ffmpeg
    fcitx5
    fcitx5-mozc
)

desktop_application=(
    mpv
    audacious
)


function main(){

    sudo apt-get update

    for package_name in "${common_application[@]}"  "${type[@]}"
    do
        [[ -z "${package_name}" ]] && continue
        [[ "${package_name::1}" = "#" ]] && continue

        sudo apt-get install --no-install-recommends ^"${package_name}"$
    done
}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then

    HOSTNAME="${HOSTNAME:-$(hostname)}"

    if   [[ ${HOSTNAME} =~ ^.*desktop$ ]] ; then
        type=("${desktop_application[@]}")
    else
        echo "Invalid argument"
        exit 1
    fi

    main

fi