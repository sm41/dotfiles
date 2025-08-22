# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login exists.


# XDG Base Directory - ArchWiki
# https://wiki.archlinux.jp/index.php/XDG_Base_Directory

# XDG Base Directory - ArchWiki
# https://wiki.archlinux.org/title/XDG_Base_Directory

HOSTNAME="${HOSTNAME:-$(hostname)}"


function share(){
  # XDG
  export  XDG_CACHE_HOME="${HOME}/.cache"
  export XDG_CONFIG_HOME="${HOME}/.config"
  export   XDG_DATA_HOME="${HOME}/.local/share"
  export  XDG_STATE_HOME="${HOME}/.local/state"

  # NetWork
  export DESKTOP_IP_ADDRESS="192.168.1.9"
  export  SERVER_IP_ADDRESS="192.168.1.38"
  export NETWORK_INTERFACE="$(ip -br link show | awk '$2 == "UP" { print $1 }')"

}

function desktop(){
  # /mnt
  export CLIENT_NETWORK_STORAGE_misc="/mnt/samba/misc"

  # PATH
  export PATH="${PATH}":"${HOME}/bin/bash"
  export PATH="${PATH}":"${HOME}/bin/python"
  export PATH="${PATH}":"${HOME}/.local/bin"


  # 1. コマンドラインと環境 — Python 3.13.0 ドキュメント
  # https://docs.python.org/ja/3/using/cmdline.html#environment-variables

  # python
  export              PYTHONPATH="${PYTHONPATH:+$PYTHONPATH:}${HOME}/bin/python"
  export          PYTHON_HISTORY="${XDG_STATE_HOME}/python/history"
  export     PYTHONPYCACHEPREFIX="${XDG_CACHE_HOME}/python"
  # export          PYTHONUSERBASE="${XDG_DATA_HOME}/python"
  # export PYTHONDONTWRITEBYTECODE=1

  # export PYTHONPATH="${PYTHONPATH}":"${PYTHONUSERBASE}"

}

function server(){
  # /mnt
  export SERVER_LOCAL_STORAGE_misc="/mnt/local/misc"

  # docker
  export  DOCKER_CONFIG="${XDG_CONFIG_HOME}/docker"

}

share


if   [[ "${HOSTNAME}" =~ ^.*desktop$ ]] ; then
  desktop
elif [[ "${HOSTNAME}" =~ ^.*server$ ]] ; then
  server
fi
