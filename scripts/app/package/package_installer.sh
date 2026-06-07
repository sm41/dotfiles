# !/bin/bash
set -eu

common_application=(
    git
    samba
)

desktop_application=(
    mpv
    audacious
)

server_application=(

)


function main(){

    HOSTNAME="${HOSTNAME:-$(hostname)}"

    if   [[ ${HOSTNAME} =~ ^.*desktop$ ]] ; then
        type=("${desktop_application[@]}")

    elif [[ ${HOSTNAME} =~ ^.*server$ ]] ; then
        type=("${server_application[@]}")

    else
        echo "Invalid argument"
        exit 1
    fi

    # sudo apt-get update

    for package_name in "${common_application[@]}"  "${type[@]}"
    do
        [ -z "${package_name}" ] && continue
        [ "${package_name::1}" = "#" ] && continue

        echo "${package_name}"
        # sudo apt-get install --no-install-recommends ^"${package_name}"$
    done
}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi