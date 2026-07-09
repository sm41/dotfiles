# !/#/bash
set -eu



function main(){
    while read jjj
    do
        sudo chown -R "${USER}":"${USER}" "${jjj}"

    done < <(grep -oP "(STORAGE.*=)\K.*" <<< $(printenv))

}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi