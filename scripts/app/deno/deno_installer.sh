# !/bin/bash
set -eu


function main(){
    curl -fsSL https://deno.land/install.sh | sh
}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi