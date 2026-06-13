# !/bin/bash
set -eu


function fedora(){
    var=dnf
    opt=
    sudo "${var}" check-update
}

function ubuntu(){
    var=apt-get
    opt=--no-install-recommends
    sudo "${var}" update
}


function main(){
    cd "${HOME}"
    sudo "${var}" install "${opt}" git
    mkdir -p "${HOME}/repository"
    cd "${HOME}/repository"
    git clone https://github.com/sm41/dotfiles.git
}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then

    id=$(. /etc/os-release && echo ${ID})

    if   [[ "${id}" == fedora ]] ; then
        echo "fedora"
        echo "main"
    elif [[ "${id}" == linuxmint ]] ; then
        echo "ubuntu"
        echo "main"
    fi

fi