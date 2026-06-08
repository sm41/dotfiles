# !/bin/bash
set -eu


function main(){

    id=$(. /etc/os-release && echo ${ID})

    if   [[ "${id}" == linuxmint ]] ; then
        curl -L https://go.microsoft.com/fwlink/?LinkID=760868 -o vscode.deb
        sudo apt-get install ./vscode.deb
        rm ./vscode.deb

    elif [[ "${id}" == fedora ]] ; then
        # 1.Install the key and yum repository:
        sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc &&
        echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\nautorefresh=1\ntype=rpm-md\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" | sudo tee /etc/yum.repos.d/vscode.repo > /dev/null

        # 2.Update the package cache and install the package with dnf on Fedora 22 and later:
        dnf check-update &&
        sudo dnf install code # or code-insiders
    fi

}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi