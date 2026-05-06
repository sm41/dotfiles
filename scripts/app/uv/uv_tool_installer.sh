# !/bin/bash
set -eu


uv_tool_package=(
    yt-dlp
    gallery-dl
)


function main(){

    for package_name in "${uv_tool_package[@]}"
    do
        [ -z "${package_name}" ] && continue
        [ "${package_name::1}" = "#" ] && continue

        # uv tool install "${package_name}"
        echo "uv tool install "${package_name}""
    done
}


if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi