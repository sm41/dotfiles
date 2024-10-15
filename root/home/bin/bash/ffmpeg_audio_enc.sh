#!/bin/bash
set -e

# usage
function show_usage(){
  cat << _EOT_
  Usage : find /hoge/fuga/ -name "*m4a" | $(basename "$0")  'codec_type'
    stdin = PATH (or strings)
    \$1 = codec_type
_EOT_
}

# main
function main(){
  while read target_file
  do
    if [[ ${target_file##*.} =~ ^(m4a)$ ]] && [[ $1 =~ ^(mp3)$ ]] ; then
      enc_audio_ffmpeg ${target_file}  $1
    else
      continue
    fi
  done
}

WORK_PATH=$(realpath $(dirname "$0"))

# check stdin
source ${WORK_PATH}/_func_check.sh
source ${WORK_PATH}/_func_ffmpeg.sh


check_stdin
check_number_of_argment 1 $#
main