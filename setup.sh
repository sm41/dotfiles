#!/usr/bin/bash
set -eu

work_path=$(cd $(dirname $0) && pwd)

read -p " 🗨️  select  [ client | server | network | link ]  ==>  "  category_of_func
echo "+----------------------------------------------------------------+"




# eval $(cat ${work_path}/zzz/${category_of_func})





while read list_of_func <&3 || [[ -n ${list_of_func} ]]
do

  read -p "┏━ 💲 ${list_of_func##*/}  [ y/n ]  ==>  "  selected_func

  case ${selected_func} in
    [Yy])
      echo "┗━ ✅ execute"
      eval $(cat ${list_of_func}) <&3
    ;;
    [Nn])
      echo "┗━ ❌ cancel"
    ;;
  esac

  echo "+----------------------------------------------------------------+"

done 3< ${work_path}/zzz/${category_of_func}