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

function fedora(){
    var=dnf
    opt=
    echo "sudo ${var} check-update"
}

function ubuntu(){
    var=apt-get
    opt=--no-install-recommends
    echo "sudo ${var} update"
}


function main(){
    for package_name in "${common_application[@]}"  "${type[@]}"
    do
        [[ -z "${package_name}" ]] && continue
        [[ "${package_name::1}" = "#" ]] && continue

        echo "sudo ${var} install ${opt} ^"${package_name}"$"
    done
}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then

    id=$(. /etc/os-release && echo ${ID})
    HOSTNAME="${HOSTNAME:-$(hostname)}"

    if   [[ ${HOSTNAME} =~ ^.*desktop$ ]] ; then
        type=("${desktop_application[@]}")
    elif [[ ${HOSTNAME} =~ ^.*server$ ]] ; then
        type=("${server_application[@]}")
    else
        echo "Invalid argument"
        exit 1
    fi

    if   [[ "${id}" == fedora ]] ; then
        fedora
        main
    elif [[ "${id}" == linuxmint ]] ; then
        ubuntu
        main
    fi

fi