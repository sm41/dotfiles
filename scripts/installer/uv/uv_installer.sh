# !/bin/bash
set -eu


function main(){
    curl -LsSf https://astral.sh/uv/install.sh | sh
}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi