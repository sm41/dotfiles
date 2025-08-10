#!/bin/bash
set -eu

# variable
WORK_PATH="$(realpath $(dirname "$0"))"
arg_str="$1"
old_ext=png
new_ext=jpg
hogefuga="_[encoded]"

# source
source "${WORK_PATH}/_func_check.sh"
source "${WORK_PATH}/_func_rename_pipe.sh"

function show_usage(){
  cat << _EOT_
  Usage :
    $(basename "$0") ~/foo/bar/
    OR
    $(basename "$0") ~/foo/bar/foo.png

    Convert image files with the .${old_ext} extension to .${new_ext} format.
    If a directory is specified, all .${old_ext} files inside will be processed.
    If a file is specified, only that file will be processed.

  Arguments
    \$1   = sed command OR 'function_name'
_EOT_
}

function check_argment(){
  if [[ -d "${arg_str}" ]] ; then
    if [[ "${arg_str}" =~ ^.*/$ ]] ; then
      arg_str="${arg_str/%\//}"
    fi

    if [[ ${arg_str} =~ ^(.*)/(.+)$ ]]; then
      base_path="${BASH_REMATCH[1]}"
      old_dir="${BASH_REMATCH[2]}"
      new_dir="$(zen2han <<< "${old_dir}${hogefuga}")"

      old_path="${base_path}/${old_dir}"
      new_path="${base_path}/${new_dir}"
      mkdir -p "${new_path}"
    fi

  elif [[ -f "${arg_str}" && "${arg_str}" =~ ".${old_ext}"$ ]] ; then
    if [[ ${arg_str} =~ ^(.*)/(.+)$ ]]; then
      base_path="${BASH_REMATCH[1]}"
      old_path="${base_path}"
      new_path="${base_path}"
    fi

  else
    echo "${FUNCNAME[0]}"
    show_usage
    exit 1
  fi
}

function main(){
  while read inputfile
  do
    filename="${inputfile##*/}"
    old_file="${filename%.*}"
    new_file="$(zen2han <<< "${old_file}")"

    ffmpeg \
      -nostdin \
      -loglevel warning \
      -i "${old_path}/${old_file}.${old_ext}" \
          "${new_path}/${new_file}.${new_ext}"

    # echo "${old_path}/${old_file}.${old_ext}"
    # echo "${new_path}/${new_file}.${new_ext}"

  done < <(find "${arg_str}" -type f -name "*.${old_ext}" | sort -V)
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
  check_number_of_argment 1 "$#"
  check_argment
  main
fi