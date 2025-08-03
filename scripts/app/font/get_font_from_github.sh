# !/bin/bash
set -eu

work_path="$(realpath $(dirname "$0"))"
input_file="font_repo_list.sh"


function get_repsitory_path(){
  local url="$1"

  path=${url#*github.com/}

  # スラッシュで分割して配列にする
  IFS='/' read -ra parts <<< "$path"
  repo_path="${parts[0]}/${parts[1]}"

  echo "${repo_path}"
}

function get_name_and_dlurl(){
  local url="$1"
  local -n json_array="$2"

  mapfile -t json_array < <(
    curl -s -H "Accept: application/vnd.github.v3+json" "${url}" | \
    jq -c '.[] | select(.name | endswith(".ttf")) | {name: .name, url: .download_url}'
  )
}

function analyse_pb(){
  local url="$1"

  fuga=$(curl -s "${url}"  \
  | grep '^name:' \
  | sed -E "s/^name: ['\"](.*)['\"]/\\1/" \
  | tr ' ' '_')

  echo "${fuga}"
}


while read file_path
do

  declare -a font_jsons
  [[ -z "${file_path}" ]] && continue
  [[ "${file_path::1}" = "#" ]] && continue

  owner_and_repo=$(get_repsitory_path "${file_path}")
  repository_path="https://github.com/${owner_and_repo}"
  api_repository="https://api.github.com/repos/${owner_and_repo}"
  branch_name=$(curl -s -H "Accept: application/vnd.github.v3+json" "${api_repository}"  | jq -r '.default_branch' )
  dir_path=${file_path/"${repository_path}/tree/${branch_name}"/}
  protocol_buffers="https://raw.githubusercontent.com/${owner_and_repo}/${branch_name}${dir_path}/METADATA.pb"
  font_package_name=$(analyse_pb "${protocol_buffers}")
  get_name_and_dlurl "${api_repository}/contents${dir_path}" font_jsons

  echo "FILE_PATH      : ${file_path}"
  echo "OWNER/REPO     : ${owner_and_repo}"
  echo "REPOSITORY_PATH: ${repository_path}"
  echo "API_REPOSITORY : ${api_repository}"
  echo "BRANCH_NAME    : ${branch_name}"
  echo "DIR_PATH       : ${dir_path}"
  echo "METADATA.pb    : ${protocol_buffers}"
  echo "Font_Name      : ${font_package_name}"
  echo "API_URL        : ${api_repository}/contents${dir_path}"

  # mkdir -p "${XDG_DATA_HOME}/fonts/${font_package_name}"

  for font in "${font_jsons[@]}"; do
    name=$(jq -r '.name' <<< "${font}")
    url=$(jq -r '.url' <<< "${font}")
    echo "DL_NAME        : ${name}"
    echo "DL_URL         : ${url}"

    # curl -s -L -o "${HOME}/fonts/${font_package_name}/${name}" "${url}" --create-dirs
    echo "curl -s -L -o "${XDG_DATA_HOME}/fonts/${font_package_name}/${name}" "${url}" --create-dirs"

  done

  echo "----------------------------------------"

done < "${work_path}/${input_file}"


