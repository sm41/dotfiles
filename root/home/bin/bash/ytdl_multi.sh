#!/bin/bash
set -eu

# variable
WORK_PATH="$(realpath $(dirname "$0"))"

# source
source "${WORK_PATH}"/_func_check.sh


function show_usage(){
  cat << _EOT_
  Usage : "$(basename "$0")"  'https://hoge/fuga' OR 'hoge_list'
    \$1 = url or function
_EOT_
}

function target_website(){
  REC_DIR="${CLIENT_LOCAL_STORAGE}/@$1"
  VAR_DIR="${XDG_STATE_HOME}/yt-dlp/$1"
  DL_FILE="$1_list"

  mkdir -pv "${REC_DIR}"
  mkdir -pv "${VAR_DIR}"
  touch  "$_/${DL_FILE}"
}

function category(){
  # CATEGORY_DIR=/"$(echo "$1" |awk -F "/" '{print $4}')"
  # ACT_NAME_DIR=/"$(echo "$1" |awk -F "/" '{print $5}')"

  CATEGORY_DIR=/"$(awk -F "/" '{print $4}'  <<<  "$1")"
  ACT_NAME_DIR=/"$(awk -F "/" '{print $5}'  <<<  "$1")"


  mkdir -pv "${REC_DIR}${CATEGORY_DIR}${ACT_NAME_DIR}"
  mkdir -pv "${VAR_DIR}${CATEGORY_DIR}${ACT_NAME_DIR}"
  touch     "$_/${ACT_NAME_DIR}.dllog"

  yt-dlp \
    --download-archive "${VAR_DIR}${CATEGORY_DIR}${ACT_NAME_DIR}${ACT_NAME_DIR}.dllog" \
    --paths "${REC_DIR}${CATEGORY_DIR}${ACT_NAME_DIR}" \
    --output "[%(upload_date>%Y-%m-%d)s]_[%(id)s]_%(title)s.%(ext)s" \
  "https://pornhub.com${CATEGORY_DIR}${ACT_NAME_DIR}/videos/upload"
}

function download_podcast_list(){
  yt-dlp \
    --batch-file "${VAR_DIR}/${DL_FILE}" \
    --paths "${REC_DIR}" \
    --output '[Podcast]_%(series)s_%(upload_date>%Y-%m-%d)s_%(title)s.%(ext)s'
}

function download_tver_list(){
  yt-dlp \
    --batch-file "${VAR_DIR}/${DL_FILE}" \
    --embed-subs \
    --paths "${REC_DIR}" \
    --output '[%(webpage_url_domain)s]_%(series)s_%(episode)s.%(ext)s'
}

function url_is_apple(){
  yt-dlp \
    --paths "${REC_DIR}" \
    --output '[Podcast]_%(series)s_%(upload_date>%Y-%m-%d)s_%(title)s.%(ext)s' \
  "$1"
}

function url_is_tver(){
  yt-dlp \
    --embed-subs \
    --paths "${REC_DIR}" \
    --output '[%(webpage_url_domain)s]_%(series)s_%(episode)s.%(ext)s' \
  "$1"
}

function viewkey(){
  yt-dlp \
    --paths "${REC_DIR}" \
    --output "[%(upload_date>%Y-%m-%d)s]_[%(id)s]_%(title)s.%(ext)s" \
  "$1"
}

function main(){
  if   [[ "$1" =~ (_list)$ ]] ; then
    target_website "${1%%_*}"
    check_empty_file  "${VAR_DIR}/${DL_FILE}"
    download_"${1%%_*}"_list

  elif [[ "$1" =~ ^https://tver.jp/episodes/ ]] ; then
    target_website 'tver'
    url_is_tver  "$1"

  elif [[ "$1" =~ ^https://podcasts.apple.com/ ]] ; then
    target_website 'podcast'
    url_is_apple  "$1"

  elif [[ "$1" =~ pornhub.com/model/|pornhub.com/pornstar/ ]] ; then
    target_website 'ph'
    category  "$1"

  elif [[ "$1" =~ viewkey=.+$ ]] ; then
    target_website 'ph'
    viewkey  "$1"

  else
    show_usage ; exit 1
  fi
}

check_number_of_argment 1 "$#"
main "$1"