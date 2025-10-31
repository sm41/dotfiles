#!/bin/bash
set -eu

# variable
WORK_PATH="$(realpath $(dirname "$0"))"
arg_str=$(realpath "$1")
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
  arg_str="$(realpath "$1")"
  input_path="$2"

  input_dirname="${input_path%/*}"
  input_basename="${input_path##*/}"
  input_filename="${input_basename%.*}"
  input_extention="${input_basename##*.}"
  output_filename="$(zen2han <<< ${input_filename})"

  if [[ -d "${arg_str}" ]] ; then
    if [[ "${arg_str}" =~ ^.*/$ ]] ; then
      arg_str="${arg_str/%\//}"
    fi

    parent_dir="${input_dirname}"
    child_dir="${parent_dir/${arg_str}/}"

    old_base_dir="${arg_str}"
    new_base_dir="$(zen2han <<< "${old_base_dir}${hogefuga}")"

    before_dir="${old_base_dir}${child_dir}"
    after_dir="${new_base_dir}${child_dir}"

    mkdir -p "${after_dir}"

  elif [[ -f "${arg_str}" ]] ; then
    if [[ "${arg_str}" =~ ^(.*)/(.+)\."${old_ext}"$ ]] ; then
      before_dir="${input_dirname}"
      after_dir="${input_dirname}"
    fi

  else
    echo "${FUNCNAME[0]}"
    show_usage
    exit 1
  fi
}

function main(){
  while read input_path
  do
    check_argment "${arg_str}" "${input_path}"

    ffmpeg \
      -nostdin \
      -loglevel warning \
      -i  "${before_dir}/${input_filename}.${input_extention}" \
          "${after_dir}/${output_filename}.${new_ext}"

  done < <(find "${arg_str}" -type f -name "*.${old_ext}" | sort -V)
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
  check_number_of_argment 1 "$#"
  main
fi
