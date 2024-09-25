#!/usr/bin/bash
set -eu

work_path=$(cd $(dirname $0) && pwd)
array_file=( $(find  ${work_path}/zzz  -type f -printf "%f\n" | sort) )

# question
read -p "🗨️  select  [ `echo ${array_file[@]}` ]  ==>  "  category_of_func

# check input word
  if printf '%s\n' "${array_file[@]}"  |  grep -qx ${category_of_func} ; then
    echo "┗━ ✅ [ Match file name ]"
  else
    echo "┗━ ❌ [ Not match file name ]"
    exit 1
  fi

echo "+----------------------------------------------------------------+"
# shell script file
while read jjj || [[ -n ${jjj} ]]
do
  [[ ${jjj::1} = "#" ]] && continue
  echo "📜  ${jjj##*/}"
done < ${work_path}/zzz/${category_of_func}

echo "+----------------------------------------------------------------+"

while read list_of_func <&3 || [[ -n ${list_of_func} ]]
do

  [[ ${list_of_func::1} = "#" ]] && continue

  read -p "┏━ 💲 ${list_of_func##*/}  [ y | n ]  ==>  "  selected_func

  case ${selected_func} in
    [Yy])
      echo "┗━ ✅ execute"
      eval $(echo ${list_of_func}) <&3
    ;;
    [Nn])
      echo "┗━ ❌ cancel"
    ;;
  esac

  echo "+----------------------------------------------------------------+"

done 3< ${work_path}/zzz/${category_of_func}