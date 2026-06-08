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


    id=$(. /etc/os-release && echo ${ID})

    if   [[ "${id}" == linuxmint ]] ; then
        var=apt-get
        opt=--no-install-recommends
        echo "sudo ${var} update"
    elif [[ "${id}" == fedora ]] ; then
        var=dnf
        opt=
        echo "sudo ${var} check-update"
    fi


    for package_name in "${common_application[@]}"  "${type[@]}"
    do
        [ -z "${package_name}" ] && continue
        [ "${package_name::1}" = "#" ] && continue

        # echo "${var} ${package_name}"
        echo "sudo ${var} install ${opt} ^"${package_name}"$"
    done
}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi