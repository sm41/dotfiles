# !/bin/bash
set -eu

work_path="$(realpath $(dirname "$0"))"
input_file="font_repo_list.sh"

source ${work_path}/font_repo_list.sh


# function encode_api(){
#   blob_url=$1

#   echo ${blob_url} | \
#     sed -e "s|/github.com/|/api.github.com/repos/|" \
#         -e "s|/blob/main/|/contents/|"
# }


function encode_api(){
  blob_url=$1

    sed -e "s|/github.com/|/api.github.com/repos/|" \
        -e "s|/blob/main/|/contents/|" \
        <<< "${blob_url}"
}


function get_name_and_dlurl(){
  local url="$1"
  local -n json_array="$2"

  mapfile -t json_array < <(
    curl -s -H "Accept: application/vnd.github.v3+json" "${url}" | \
    jq -c 'select(.name | endswith(".ttf") or endswith(".otf") ) | {name: .name, url: .download_url}'
  )
}


for var in $(set | grep -F '[url_1]=' | awk -F= '{print $1}') ;
do

  font_dir="${XDG_DATA_HOME}/fonts/${var}"
  # echo "mkdir -p ${font_dir}"
  declare -n ref=${var}

  for val in "${ref[@]}"; do

    declare -a font_jsons
    blob_api=$(encode_api   ${val})
    get_name_and_dlurl "${blob_api}" font_jsons

    for font in "${font_jsons[@]}";
    do
      name=$(jq -r '.name' <<< "${font}")
      url=$(jq -r '.url' <<< "${font}")

      echo "BLOB_PATH   : ${val}"
      echo "BLOB_API    : ${blob_api}"
      echo "DL_NAME     : ${name}"
      echo "DL_URL      : ${url}"

      # if curl -f -s -S -L -o "${font_dir}/${name}" "${url}" --create-dirs ; then
      #   echo "✅ Downloaded: ${name} to ${font_dir}"
      # else
      #   echo "🆖 Failed to download: ${name} from ${url}"
      # fi

    done

    echo "----------------------------------------"

    # break

  done

  # break

done

