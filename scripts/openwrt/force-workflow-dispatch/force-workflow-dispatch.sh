#!/bin/sh
set -eu

rrr=$(cd $(dirname $0) && pwd)
. ${rrr}/.env

# wget \
#     --header="Accept: application/vnd.github+json" \
#     --header="Authorization: Bearer ${token}" \
#     "https://api.github.com/repos/sm41/cicd-feed/actions/workflows"

# curl \
#     -H "Accept: application/vnd.github.v3+json" \
#     -H "Authorization: token xxxxxxxxxxxx" \
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


# POSIX 準拠のシェルでは、return コマンドを関数内以外（スクリプトのトップレベル）で実行すると、「source された時だけ呼び出し元に制御を戻す」という特性があります。
# 直接実行された場合はエラーになるか無視されます。
# この特性とエラー表示を消す技（2>/dev/null）を組み合わせることで、直接実行時のみ main を動かすことができます。
# https://unix.stackexchange.com/questions/424492/how-to-define-a-shell-script-to-be-sourced-not-run


return 0 2>/dev/null
main
