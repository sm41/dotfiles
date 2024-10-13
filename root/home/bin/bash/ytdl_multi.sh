#!/bin/bash
# set -x

function show_usage(){
  cat << _EOT_
  Usage : $(basename "$0")  'https://hoge/fuga' OR 'hoge_list'
    \$1 = url or function
_EOT_
}

DOTFILES=/repository/dotfiles/root/home
LOCAL_LIB=/.local/lib/bash

source  ${HOME}${DOTFILES}${LOCAL_LIB}/_func_ytdl.bash
source  ${HOME}${DOTFILES}${LOCAL_LIB}/_func_check.bash

# check argment
check_number_of_argment 1 $#

# make directory and file
function target_website(){
  REC_DIR=/mnt/640G/@$1
  VAR_DIR=/.local/state/yt-dlp/$1
  DL_FILE=$1_list

  mkdir -pv ${REC_DIR}
  mkdir -pv ${HOME}${VAR_DIR}
  touch     $_/${DL_FILE}
}

if   [[ $1 =~ (_list)$ ]] ; then
  grep \
    --quiet \
    "function download_$1(){" \
  ${HOME}${DOTFILES}${LOCAL_LIB}/_func_ytdl.bash

  GGG=$?

  if [[ ${GGG} = 0 ]] ; then
    target_website ${1%%_*}
    check_empty_file  ${HOME}${VAR_DIR}/${DL_FILE}
    download_${1%%_*}_list
  else
    show_usage ; exit 1
  fi

elif [[ $1 =~ ^https://tver.jp/episodes/ ]] ; then
  target_website 'tver'
  url_is_tver  $1

elif [[ $1 =~ ^https://podcasts.apple.com/ ]] ; then
  target_website 'podcast'
  url_is_apple  $1

elif [[ $1 =~ pornhub.com/model/|pornhub.com/pornstar/ ]] ; then
  target_website 'ph'
  category  $1

elif [[ $1 =~ viewkey=.+$ ]] ; then
  target_website 'ph'
  viewkey  $1

else
  show_usage ; exit 1
fi
