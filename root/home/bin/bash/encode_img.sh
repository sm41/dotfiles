#!/bin/bash
set -eu

WORK_PATH="$(realpath $(dirname "$0"))"
source "${WORK_PATH}/_func_rename_pipe.sh"

old_ext=png
new_ext=jpg
arg_str="$1"
base_path="$(dirname "${arg_str}")"
old_dir="$(basename "${arg_str}")"
new_dir="$(echo "${old_dir}_[encoded]" | zen2han)"

function check_file(){
  if find "${arg_str}" -type f -name "*.${old_ext}" | grep -q . ; then
    :
  else
    echo "${FUNCNAME[0]}"
    exit 1
  fi
}

function check_argment(){
  if [[ -d "${arg_str}" ]] ; then
    check_file
    old_path="${base_path}/${old_dir}"
    new_path="${base_path}/${new_dir}"
    mkdir -p "${new_path}"
  elif [[ "${arg_str}" =~ ".${old_ext}"$ ]] ; then
    old_path="${base_path}"
    new_path="${base_path}"
  else
    echo "${FUNCNAME[0]}"
    exit 1
  fi
}

function main(){
  while read inputfile
  do
    filename="${inputfile##*/}"
    old_file="${filename%.*}"
    new_file="$(echo "${old_file}" | zen2han)"

    ffmpeg \
      -nostdin \
      -i "${old_path}/${old_file}.${old_ext}" \
          "${new_path}/${new_file}.${new_ext}"

  done < <(find "${arg_str}" -type f -name "*.${old_ext}" | sort -V)
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
  # check_file
  check_argment
  main
fi