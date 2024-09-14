#!/bin/bash
set -e

function show_usage(){
  cat << _EOT_
  Usage : $(basename "$0")  func_name  '/hoge/fuga/foo.mp4'  '16:9'
    \$1 = Video file PATH      (set video codec extention to PATH)
    \$2 = Video aspect ratio   (e.g. 4:3, 16:9, etc...)
_EOT_
}

VIDEO_FILE_PATH=$1
ASPECT_RATIO=$2

# check argment
if [[ $# != 2 ]]; then show_usage ; exit 1 ; fi

# check extention
# check aspect argment
if [[ ! ${VIDEO_FILE_PATH##*.} =~ ^(mp4|wmv|avi|mkv)$ ]] || [[ ! ${ASPECT_RATIO} =~ ^(4:3|16:9)$ ]] ; then
  show_usage ; exit 1
fi

source ${HOME}${DOTFILES}${LOCAL_LIB}/_func_ffmpeg.bash
change_asp_ffmpeg
