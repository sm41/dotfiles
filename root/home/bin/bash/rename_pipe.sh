#!/bin/bash
set -eu

# variable
WORK_PATH="$(realpath $(dirname "$0"))"

# source
source "${WORK_PATH}/_func_check.sh"
source "${WORK_PATH}/_func_rename_pipe.sh"

function show_usage(){
  cat << _EOT_
  Usage : find /hoge/fuga/foo.txt | $(basename "$0") 's/foo/bar/g' OR 'function_name'
    stdin = PATH (or strings)
    \$1   = sed command OR 'function_name'
_EOT_
}

function check_sed_command(){
  if [[ "$1" =~ [sy][/|].*[/|]g?$  ]] ; then
    SED_COMMAND="$1"
    SED_ARG="sed_arg"
  else
    SED_ARG="$1"
  fi
}

function main(){
  while read TARGET_FILE
  do
    base_dir="${TARGET_FILE%/*}"
    old_name="${TARGET_FILE##*/}"
    new_name="$(echo "${old_name}" | "${SED_ARG}")"

    echo mv  \"${base_dir}/${old_name}\"  \"${base_dir}/${new_name}\"

  done
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
  check_stdin
  check_number_of_argment 1 "$#"
  check_sed_command "$1"
  main
fi
