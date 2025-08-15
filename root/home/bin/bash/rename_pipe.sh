#!/bin/bash
set -eu

# variable
WORK_PATH="$(realpath $(dirname "$0"))"

# source
source "${WORK_PATH}/_func_check.sh"
source "${WORK_PATH}/_func_rename_pipe.sh"

function show_usage(){
  cat << _EOT_
  Usage :
    find /hoge/fuga/ -name "*foo*" | $(basename "$0") 's/foo/bar/g'
    OR
    find /hoge/fuga/foo.txt | $(basename "$0") 'function_name' (ex : 'zen2han')

  Arguments :
    stdin : A list of file paths (e.g., from 'find')
    \$1   : (Either one)
          - a 'sed' expression like 's/foo/bar/g'
          - a function name defined in the script

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
    new_name="$("${SED_ARG}" <<< "${old_name}")"

    echo mv  \"${base_dir}/${old_name}\"  \"${base_dir}/${new_name}\"

  done
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
  check_number_of_argment 1 "$#"
  check_stdin
  check_sed_command "$1"
  main
fi
