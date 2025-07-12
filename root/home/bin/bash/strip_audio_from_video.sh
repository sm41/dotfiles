#!/bin/bash
set -eu

# variable
hogefuga=_muted
arg_str="${1:-}"
# if [[ -z "$arg_str" ]]; then
#   echo "❌ 第1引数（ディレクトリパス）を指定してください。" >&2
#   show_usage
#   exit 1
# fi

# source
source "${WORK_PATH}/_func_check.sh"

function show_usage(){
  cat << _EOT_
  Usage :
    $(basename "$0") ~/hoge/fuga/
    OR
    $(basename "$0") ~/hoge/fuga/foo.mp4

  Arguments:
    \$1 : Directory containing .mp4 files to process.

_EOT_
}

function check_argment(){
  if [[ -d "${arg_str}" ]] || [[ "${arg_str}" =~ ".mp4"$ ]]; then
    old_path="${arg_str%/*}"
    new_path="${arg_str%/*}"
  else
    echo "${FUNCNAME[0]}"
    show_usage
    exit 1
  fi
}


function main() {
  while read filepath
  do
    audio_streams="$(ffprobe -v error -select_streams a -show_entries stream=index -of csv=p=0 "${filepath}")"

    if [[ -n "${audio_streams}" ]]; then
      filename="${filepath##*/}"
      old_file="${filename%.*}"
      new_file="${old_file%.*}${hogefuga}"

      echo "▶️   Strip  Audio : \"${old_path}/${old_file}.mp4\" → \"${new_path}/${new_file}.mp4\""

      # ffmpeg \
      #   -nostdin \
      #   -i "${old_path}/${old_file}.mp4" \
      #   -c copy \
      #   -an \
      #   -loglevel warning \
      #     "${new_path}/${new_file}.mp4" \

    else
      echo "⚠️   Skip Process : \"${old_path}/${old_file}.mp4\""
    fi

  done < <(find "${arg_str}"  -maxdepth 1  -type f -name "*.mp4" | sort -V)
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
  check_number_of_argment 1 "$#"
  check_argment
  main
  echo "📢  処理が完了しました。"
fi
