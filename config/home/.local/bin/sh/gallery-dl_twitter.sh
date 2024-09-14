#!/bin/bash
# set -eux

STORAGE_DIR=/mnt/640G
VAR_DIR=/.local/state
BASE_DIR=/gallery-dl
DOMAIN_DIR=/twitter
ORIGIN_FILE=twitter_list

# get the URL of each user in the list
while read -a TW_LIST
do
  LIST_URL=${TW_LIST[0]}
  LIST_TITLE=${TW_LIST[2]}

  if [[ ! ${LIST_URL} =~ ^https://x.com/i/lists/[0-9]{19}/members$ ]] ; then continue ; fi

  # make directory of member's in the list at the base directory
  mkdir -pv ${HOME}${VAR_DIR}${BASE_DIR}${DOMAIN_DIR}/${LIST_TITLE}
  mkdir -pv    ${STORAGE_DIR}${BASE_DIR}${DOMAIN_DIR}/${LIST_TITLE}

  gallery-dl --dump-json ${LIST_URL} \
    | jq --raw-output --compact-output '.[][2] | ["https://x.com/i/user/" + .rest_id, "# " + .legacy.screen_name] | @tsv' \
    | awk '{printf "%-50s %-s %-s\n",$1,$2,$3}' \
    | sort --ignore-case --key 3 \
  > ${HOME}${VAR_DIR}${BASE_DIR}${DOMAIN_DIR}/${LIST_TITLE}/${LIST_TITLE}_spread

done < <(awk '$1 !~ /^#/ {print $0}' ${HOME}${VAR_DIR}${BASE_DIR}${DOMAIN_DIR}/${ORIGIN_FILE} )

function check_diff(){
  LISTNAME_DIR=$(dirname ${SPREADSHEAT_FILE} | xargs basename)
  CHECK_NUMBER_SIGN=$(cat ${HOME}${VAR_DIR}${BASE_DIR}${DOMAIN_DIR}/${ORIGIN_FILE} | awk -v hoge=${LISTNAME_DIR} '$3 == hoge {print $1}' )

  if [[  ${CHECK_NUMBER_SIGN:0:1} = '#' ]] ; then continue ; fi

  REMOVE_USER_FROM_LIST=$(diff --old-line-format='-- %L' --unchanged-line-format='' --new-line-format='++ %L' \
      <(ls -l  ${STORAGE_DIR}${BASE_DIR}${DOMAIN_DIR}/${LISTNAME_DIR} | awk 'NR>=2{print $9}') \
      <(cat ${HOME}${VAR_DIR}${BASE_DIR}${DOMAIN_DIR}/${LISTNAME_DIR}/${LISTNAME_DIR}_spread | awk '{print $3}' | sort) \
  )
}

function download(){
  while read -a SPREADSHEAT_ROW
  do
    USER_ID=${SPREADSHEAT_ROW[0]}
    USER_DIR=${SPREADSHEAT_ROW[2]}

    mkdir -pv ${STORAGE_DIR}${BASE_DIR}${DOMAIN_DIR}/${LISTNAME_DIR}/${USER_DIR}

    gallery-dl \
      --directory ${STORAGE_DIR}${BASE_DIR}${DOMAIN_DIR}/${LISTNAME_DIR}/${USER_DIR} \
      --filter "extension not in ('mp4', 'wmv', 'gif')" \
    ${USER_ID}

  done < ${SPREADSHEAT_FILE}
}

function notify(){
  # notify
  if [[ ! -z "${REMOVE_USER_FROM_LIST}" ]] ; then
    notify-send  "⚠️ User is Not Found"   "${STORAGE_DIR}${BASE_DIR}${DOMAIN_DIR}/${LISTNAME_DIR}\n${REMOVE_USER_FROM_LIST}"
  fi
}

while read SPREADSHEAT_FILE
do
  check_diff
  download
  notify
done < <(ls -l ${HOME}${VAR_DIR}${BASE_DIR}${DOMAIN_DIR}/*/*_spread | awk '$5 > 0 {print $9}' )

notify-send "✅ Success" "$(basename $0)"