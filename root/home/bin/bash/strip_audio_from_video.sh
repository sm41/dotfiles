
#!/bin/bash
set -eu

# 引数チェック
arg_str="${1:-}"
if [[ -z "$arg_str" ]]; then
  echo "❌ 第1引数（ディレクトリパス）を指定してください。" >&2
  exit 1
fi


function main() {
  while IFS= read -r filepath
  do

    base_path="${filepath%/*}"
    audio_streams="$(ffprobe -v error -select_streams a -show_entries stream=index -of csv=p=0 "${filepath}")"

    if [[ -n "${audio_streams}" ]]; then
      hogefuga=_muted
      filename="${filepath##*/}"
      old_file="${filename%.*}"
      new_file="${old_file%.*}${hogefuga}"

      echo "▶️   Strip  Audio : \"${base_path}/${old_file}.mp4\" → \"${base_path}/${new_file}.mp4\""

      # ffmpeg \
      #   -nostdin \
      #   -i "${base_path}/${old_file}.mp4" \
      #   -c copy \
      #   -an \
      #   -loglevel error \
      #     "${base_path}/${new_file}.mp4" \

    else
      echo "⚠️   Skip Process : \"${base_path}/${old_file}.mp4\""
    fi

  done < <(find "${arg_str}" -type f -name "*.mp4" | sort -V)
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
  main
  echo "📢  処理が完了しました。"
fi
