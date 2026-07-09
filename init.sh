# !/bin/bash
set -eu


function main(){

    sudo apt-get update
    sudo apt-get install --no-install-recommends git

    mkdir -p "${HOME}/repository"
    cd "${HOME}/repository"

    git clone https://github.com/sm41/dotfiles.git

}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi