#!/bin/sh
set -eu

rrr=$(cd $(dirname $0) && pwd)
. ${rrr}/.env

# wget \
#     --header="Accept: application/vnd.github+json" \
#     --header="Authorization: Bearer ${token}" \
#     "https://api.github.com/repos/sm41/cicd-feed/actions/workflows"

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

