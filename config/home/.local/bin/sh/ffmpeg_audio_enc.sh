#!/bin/bash
set -e

function show_usage(){
  cat << _EOT_
  Usage : find /hoge/fuga/ -name "*m4a" | $(basename "$0")  'codec_type'
    stdin = PATH (or strings)
    \$1 = codec_type
_EOT_
}

DOTFILES=/dotfiles/root/home
LOCAL_LIB=/.local/lib/bash

# check stdin
source ${HOME}${DOTFILES}${LOCAL_LIB}/_func_check.bash
check_stdin

# check argment
check_number_of_argment 1 $#

while read target_file
do
  if [[ ${target_file##*.} =~ ^(m4a)$ ]] && [[ $1 =~ ^(mp3)$ ]] ; then
    enc_audio_ffmpeg ${target_file}  $1
  else
    continue
  fi
done
