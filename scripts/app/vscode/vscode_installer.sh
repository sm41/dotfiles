# !/bin/bash
set -eu


function main(){
    curl -L https://go.microsoft.com/fwlink/?LinkID=760868 -o vscode.deb
    sudo apt-get install ./vscode.deb
    rm ./vscode.deb
}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi