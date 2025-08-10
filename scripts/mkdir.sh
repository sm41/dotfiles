# !/#/bash
set -eu

HOSTNAME="${HOSTNAME:-$(hostname)}"


function share(){
  # XDG
  mkdir -p "${XDG_CONFIG_HOME}"
  mkdir -p "${XDG_CACHE_HOME}"
  mkdir -p "${XDG_DATA_HOME}"
  mkdir -p "${XDG_STATE_HOME}"

  # /home
  mkdir -p "${HOME}/XDG_USER_DIRS/Desktop"
  mkdir -p "${HOME}/XDG_USER_DIRS/Documents"
  mkdir -p "${HOME}/XDG_USER_DIRS/Downloads"
  mkdir -p "${HOME}/XDG_USER_DIRS/Music"
  mkdir -p "${HOME}/XDG_USER_DIRS/Pictures"
  mkdir -p "${HOME}/XDG_USER_DIRS/Public"
  mkdir -p "${HOME}/XDG_USER_DIRS/Templates"
  mkdir -p "${HOME}/XDG_USER_DIRS/Videos"

}

function desktop() {
  # /home
  mkdir -p "${HOME}/bin/{appimage,bash,python}"
  mkdir -p "${HOME}/repository"

  # /mnt
  sudo mkdir -p "${CLIENT_NETWORK_STORAGE_misc}"
  # sudo mkdir -p "${CLIENT_NETWORK_STORAGE_rec}"

  # python
  mkdir -p "${PYTHONPATH}"
  mkdir -p "${PYTHON_HISTORY}"
  mkdir -p "${PYTHONPYCACHEPREFIX}"
  # mkdir -p "${PYTHONUSERBASE}"

}

function server() {
  # /home
  mkdir -p "${HOME}/repository"

  # /mnt
  sudo mkdir -p "${SERVER_LOCAL_STORAGE_misc}"
  # sudo mkdir -p "${SERVER_LOCAL_STORAGE_rec}"

  # docker
  mkdir -p "${DOCKER_CONFIG}"
}




if   [[ ${HOSTNAME} =~ ^*desktop$ ]] ; then
  desktop
elif [[ ${HOSTNAME} =~ ^*server$ ]] ; then
  server
else
  :
fi

