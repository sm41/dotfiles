#!/bin/bash
# set -x

function show_usage(){
  cat << _EOT_
  Usage : find /hoge/fuga/foo.txt | $(basename "$0") 's/foo/bar/g' OR 'function_name'
    stdin = PATH (or strings)
    \$1   = sed command OR 'function_name'
_EOT_
}

DOTFILES=/repository/dotfiles/root/home
LOCAL_LIB=/.local/lib/bash

source ${HOME}${DOTFILES}${LOCAL_LIB}/_func_check.bash
source ${HOME}${DOTFILES}${LOCAL_LIB}/_func_rename.bash

# check stdin and argment
check_stdin
check_number_of_argment 1 $#

# sed script OR function
if [[ $1 =~ [sy]/.*/g?$  ]] ; then
  SED_COMMAND=$1
  SED_ARG=sed_arg
else
  SED_ARG=$1
fi


while read TARGET_FILE
do
  echo \""${TARGET_FILE##*/}"\" \
  | ${SED_ARG}  \
  | xargs -I {} \
  echo mv  \""${TARGET_FILE%/*}"/"${TARGET_FILE##*/}"\"  \""${TARGET_FILE%/*}"/{}\"  2> /dev/null
done
