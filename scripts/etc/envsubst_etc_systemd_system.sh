#!/bin/bash
set -eu

# lsblk -dno UUID | awk 'NF'
# lsblk -o NAME,SIZE,FSTYPE,UUID,LABEL,PARTUUID,PARTLABEL,MOUNTPOINT

# -d, --nodeps         スレーブデバイスやホルダーを表示しません
# -n, --noheadings     ヘッダを表示しません
# -o, --output <list>  出力する列を指定します

REQUIRED_VARS_ARRAY=(
    UUID
)

function desktop(){
    temp_path="${CLIENT_LOCAL_STORAGE_misc#/}"
    template_file="template.mnt-local-xxx.mount"
    export UUID=$(lsblk -dno UUID | awk 'NF')
}


function check_env(){

    local target_array=("${@}")

    for target_var in "${target_array[@]}"; do
        if [[ ! -v ${target_var} ]]; then
            echo "ERROR: '${target_var}' は未定義です。"
            exit 1
        fi

        if [[ -z ${!target_var} ]]; then
            echo "ERROR: '${target_var}' は空文字です。"
            exit 1
        else
            echo "${target_var} は '${!target_var}' として定義されています。"
        fi
    done

    echo "✅ Required Vars Array is passed"

}


function main(){

    desktop

    check_env "${REQUIRED_VARS_ARRAY[@]}"
    exit 0

    HOSTNAME="${HOSTNAME:-$(hostname)}"

    redefinition_path="${temp_path//\//-}"
    generate_file="${redefinition_path}.mount"

    SCRIPT_DIRECTORY="$(dirname "$(readlink -f "$0")" )"
    GIT_TOPLEVEL=$(git -C "${SCRIPT_DIRECTORY}" rev-parse --show-toplevel 2>/dev/null)
    ROOT_DIRECTORY=/root
    FHS_ORIGIN_DIRECTORY=/etc/systemd/system

    TEMPLATE_PATH="${GIT_TOPLEVEL}${ROOT_DIRECTORY}${FHS_ORIGIN_DIRECTORY}/${template_file}"
    GENERATE_PATH="${FHS_ORIGIN_DIRECTORY}/${generate_file}"

    echo ${TEMPLATE_PATH}
    echo ${GENERATE_PATH}
    # envsubst < "${TEMPLATE_PATH}" | sudo tee "${GENERATE_PATH}" > /dev/null

}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi