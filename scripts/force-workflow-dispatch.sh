# !/bin/bash
set -eu

# curl \
#     -H "Accept: application/vnd.github.v3+json" \
#     -H "Authorization: token xxxxxxx" \
#     "https://api.github.com/repos/sm41/cicd-feed/actions/workflows"

function ccc(){
    curl \
        -X POST \
        -H "Accept: application/vnd.github+json" \
        -H "Authorization: Bearer ${token}" \
    "https://api.github.com/repos/${owner}/${repo}/actions/workflows/${workflow_id}/dispatches" \
        -d '{
            "ref":"main"
        }'
}

function www(){
    wget \
        --method=POST \
        --header="Accept: application/vnd.github+json" \
        --header="Authorization: Bearer ${token}" \
        --header="Content-Type: application/json" \
        --body-data='{
            "ref":"main"
        }' \
        -O - \
    "https://api.github.com/repos/${owner}/${repo}/actions/workflows/${workflow_id}/dispatches"
}

function main(){
    www
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    main
fi
