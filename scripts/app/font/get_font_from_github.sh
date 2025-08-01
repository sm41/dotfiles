# !/bin/bash
set -eu

work_path="$(realpath $(dirname "$0"))"
input_file="font_repo_list.sh"


function get_api_path(){
  local url="$1"

  api_url=$(echo "${url}" | sed -E 's|https://github.com/|https://api.github.com/repos/|; s|/tree/[^/]+|/contents|')
  echo "${api_url}"

}

function get_json_v2(){
  local url="$1"
  local -n json_array="$2"

  mapfile -t json_array < <(
    curl -s -H "Accept: application/vnd.github.v3+json" "${url}" | \
    jq -c '.[] | select(.name | endswith(".ttf")) | {name: .name, url: .download_url}'
  )
}

function get_metadata_pb(){
  local url="$1"

  curl -s -H "Accept: application/vnd.github.v3+json" ${url} | \
  jq -r '.[] | select(.name == "METADATA.pb") | .download_url'

}

function analyse_pb(){
  local url="$1"

  fuga=$(curl -s "${url}"  \
  | grep '^name:' \
  | sed -E "s/^name: ['\"](.*)['\"]/\\1/" \
  | tr ' ' '_')

  echo "${fuga}"
}


while read repo_name
do

  declare -a font_jsons
  [[ -z "${repo_name}" ]] && continue
  [[ "${repo_name::1}" = "#" ]] && continue

  backed_api=$(get_api_path "${repo_name}")
  meta=$(get_metadata_pb "${backed_api}")
  font_package_name=$(analyse_pb "${meta}")
  get_json_v2 "${backed_api}" font_jsons

  echo "API_URL     : ${backed_api}"
  echo "METADATA.pb : ${meta}"
  echo "Font_Name   : ${font_package_name}"

  # mkdir -p "${XDG_DATA_HOME}/fonts/${font_package_name}"

  for font in "${font_jsons[@]}"; do
    name=$(jq -r '.name' <<< "${font}")
    url=$(jq -r '.url' <<< "${font}")
    echo "DL_NAME     : ${name}"
    echo "DL_URL      : ${url}"

    # curl -s -L -o "${HOME}/fonts/${font_package_name}/${name}" "${url}"
    echo "curl -s -L -o "${HOME}/fonts/${font_package_name}/${name}" "${url}"  "

  done

  echo "----------------------------------------"

done < "${work_path}/${input_file}"


