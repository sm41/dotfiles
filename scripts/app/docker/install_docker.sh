# !/bin/bash
set -eu

# https://docs.docker.com
# https://docs.docker.com/engine/install/ubuntu/


# Run the following command to uninstall all conflicting packages:
# for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc
# do
#   sudo apt-get remove $pkg
# done


# Run the following command to uninstall all conflicting packages:
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


# To install the latest version, run:
sudo apt-get install \
  docker-ce \
  docker-ce-cli \
  containerd.io \
  docker-buildx-plugin \
  docker-compose-plugin


# Verify that the Docker Engine installation is successful by running the hello-world image.
sudo docker run hello-world

