# !/bin/bash
set -eu


function main(){
    curl -sSL https://get.docker.com | sh

    sudo usermod -aG docker $USER

}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi