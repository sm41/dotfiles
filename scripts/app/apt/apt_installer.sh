# !/bin/bash
set -eu


desktop_application=(
    mpv
    audacious
)

server_application=(

)


function main(){

    if [ $# -lt 1 ]; then
        echo "Usage: $0 [ desktop | server ]"
        exit 1

    elif [[ "$1" == "desktop" ]] ; then
        type="${desktop_application}"

    elif [[ "$1" == "server" ]] ; then
        type="${server_application}"

    else
        echo "Invalid argument"
        exit 1
    fi

    # sudo apt-get update

    for package_name in "${type[@]}"
    do
        [ -z "${package_name}" ] && continue
        [ "${package_name::1}" = "#" ] && continue
        echo "${package_name}"
        # sudo apt-get install --no-install-recommends ^"${package_name}"$
    done
}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main $1
fi