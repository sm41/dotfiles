#!/bin/bash
set -e

# usage
function show_usage(){
  cat << _EOT_
  Usage : find /hoge/fuga/ -name "*m4a" | $(basename "$0")  'container_type'
    stdin = PATH (or strings)
    \$1 = container_type
_EOT_
}


# change container extension
function change_container_ffmpeg(){

  INPUT_FILE=$1
  TARGET_EXT=$2

  ffmpeg \
    -n \
    -i ${INPUT_FILE} \
    -c copy \
  ${INPUT_FILE%.*}.${TARGET_EXT} \
  </dev/null
}


# main
function main(){
  while read target_file
  do
    if [[ ${target_file##*.} =~ ^(mp4|wmv|avi|mkv|webm)$ ]] && [[ $1 =~ ^(mp4|mkv)$ ]] ;  then
      change_container_ffmpeg  ${target_file}  $1
    else
      continue
    fi
  done
}

WORK_PATH=$(realpath $(dirname "$0"))

# check stdin
source ${WORK_PATH}/_func_check.sh

check_stdin
check_number_of_argment 1 $#
main $1