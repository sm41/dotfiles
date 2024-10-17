#!/bin/bash
set -e

# usage
function show_usage(){
  cat << _EOT_
  Usage : $(basename "$0")  func_name  '/hoge/fuga/foo.mp4'  '16:9'
    \$1 = Video file PATH      (set video codec extention to PATH)
    \$2 = Video aspect ratio   (e.g. 4:3, 16:9, etc...)
_EOT_
}

# check extention
# check aspect argment
function check_container_and_aspect(){
  if [[ ! "${VIDEO_FILE_PATH##*.}" =~ ^(mp4|wmv|avi|mkv)$ ]] || [[ ! "${ASPECT_RATIO}" =~ ^(4:3|16:9)$ ]] ; then
    show_usage ; exit 1
  fi
}

# change aspect ratio
function main(){

  ffmpeg \
    -n \
    -i "${VIDEO_FILE_PATH}" \
    -c copy \
    -aspect "${ASPECT_RATIO}" \
  "${VIDEO_FILE_PATH%/*}/__${VIDEO_FILE_PATH##*/}"

}

VIDEO_FILE_PATH="$1"
ASPECT_RATIO="$2"
WORK_PATH="$(realpath $(dirname "$0"))"

source "${WORK_PATH}/_func_check.sh"

check_number_of_argment 2 "$#"
check_container_and_aspect
main "$1" "$2"