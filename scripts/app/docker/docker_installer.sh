# !/bin/bash
set -eu

# https://docs.docker.com


function fedora(){

    # https://docs.docker.com/engine/install/fedora/

    # Uninstall old versions
    sudo dnf remove docker \
        docker-client \
        docker-client-latest \
        docker-common \
        docker-latest \
        docker-latest-logrotate \
        docker-logrotate \
        docker-selinux \
        docker-engine-selinux \
        docker-engine

    # Install using the rpm repository
    # Set up the repository
    sudo dnf config-manager addrepo --from-repofile https://download.docker.com/linux/fedora/docker-ce.repo

    # 1.Install the Docker packages.
    sudo dnf install \
        docker-ce \
        docker-ce-cli \
        containerd.io \
        docker-buildx-plugin \
        docker-compose-plugin

    # 2.Start Docker Engine.
    sudo systemctl enable --now docker

    # 3.Verify that the installation is successful by running the hello-world image:
    sudo docker run hello-world
}


function ubuntu(){

    # https://docs.docker.com/engine/install/ubuntu/

    # Uninstall old versions
    while read -r pkg;
    do
        sudo apt-get remove "${pkg}"
    done <<EOF
        docker.io
        docker-doc
        docker-compose
        docker-compose-v2
        podman-docker
        containerd
        runc
EOF

    # Install using the apt repository
    # 1.Set up Docker's apt repository.
    # Add Docker's official GPG key:
    sudo apt-get update
    sudo apt-get install ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc

    # Add the repository to Apt sources:
    echo \
        "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
        $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
        sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update

    # 2.Install the Docker packages.
    # To install the latest version, run:
    sudo apt-get install \
        docker-ce \
        docker-ce-cli \
        containerd.io \
        docker-buildx-plugin \
        docker-compose-plugin

    # 3.Verify that the Docker Engine installation is successful by running the hello-world image.
    sudo docker run hello-world
}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    id=$(. /etc/os-release && echo ${ID})

    if   [[ "${id}" == fedora ]] ; then
        echo "fedooooooora"
    elif [[ "${id}" == linuxmint ]] ; then
        echo "minmiiiiiiin"
    fi

fi