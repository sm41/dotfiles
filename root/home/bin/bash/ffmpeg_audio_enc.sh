#!/bin/bash
set -eu

# variable
WORK_PATH="$(realpath $(dirname "$0"))"

# source
source "${WORK_PATH}/_func_check.sh"
source "${WORK_PATH}/_func_ffmpeg.sh"


function show_usage(){
  cat << _EOT_
  Usage : find /hoge/fuga/ -name "*m4a" | $(basename "$0")  'codec_type'
    stdin = PATH (or strings)
    \$1 = codec_type
_EOT_
}

function main(){
  while read target_file
  do
    if [[ "${target_file##*.}" =~ ^(m4a)$ ]] && [[ "$1" =~ ^(mp3)$ ]] ; then
      enc_audio_ffmpeg "${target_file}"  "$1"
    else
      continue
    fi
  done
}

check_stdin
check_number_of_argment 1 "$#"
main