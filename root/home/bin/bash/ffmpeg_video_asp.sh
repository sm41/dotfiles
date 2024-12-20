#!/bin/bash
set -eu

# variable
VIDEO_FILE_PATH="$1"
ASPECT_RATIO="$2"
WORK_PATH="$(realpath $(dirname "$0"))"

# source
source "${WORK_PATH}/_func_check.sh"


function show_usage(){
  cat << _EOT_
  Usage : $(basename "$0")  func_name  '/hoge/fuga/foo.mp4'  '16:9'
    \$1 = Video file PATH      (set video codec extention to PATH)
    \$2 = Video aspect ratio   (e.g. 4:3, 16:9, etc...)
_EOT_
}

function check_container_and_aspect(){
  if [[ ! "${VIDEO_FILE_PATH##*.}" =~ ^(mp4|wmv|avi|mkv)$ ]] || [[ ! "${ASPECT_RATIO}" =~ ^(4:3|16:9)$ ]] ; then
    show_usage ; exit 1
  fi
}

function main(){

  ffmpeg \
    -n \
    -i "${VIDEO_FILE_PATH}" \
    -c copy \
    -aspect "${ASPECT_RATIO}" \
  "${VIDEO_FILE_PATH%/*}/__${VIDEO_FILE_PATH##*/}"

}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
  check_number_of_argment 2 "$#"
  check_container_and_aspect
  main "$1" "$2"
fi