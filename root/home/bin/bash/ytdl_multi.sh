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

function make_recdir(){
  REC_DIR="${CLIENT_LOCAL_STORAGE}/@$1"
  mkdir -pv "${REC_DIR}"
}

function make_statedir(){
  VAR_DIR="${XDG_STATE_HOME}/yt-dlp/$1"
  mkdir -pv "${VAR_DIR}"
}

function category(){
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

function opop(){

  if [[ "${ppp}" =~ ^https://tver.jp/episodes/ ]] ; then
    make_recdir   'tver'
    url_is_tver   "${ppp}"
  elif [[ "${ppp}" =~ ^https://podcasts.apple.com/ ]] ; then
    make_recdir   'podcast'
    url_is_apple  "${ppp}"
  elif [[ "${ppp}" =~ pornhub.com/model/|pornhub.com/pornstar/ ]] ; then
    make_recdir   'ph'
    make_statedir 'ph'
    category      "${ppp}"
  elif [[ "${ppp}" =~ viewkey=.+$ ]] ; then
    make_recdir   'ph'
    viewkey       "${ppp}"
  else
    show_usage ; exit 1
  fi

}

function sub(){
  if   [[ -f "$1" ]] ; then
    # check_empty_file  "$1"
    while read ppp
    do
      if [[ "${ppp}" =~ ^#|^$ ]] ; then
        :
      else
        opop "${ppp}"
      fi
    done < "$1"

  elif [[ "$1" =~ ^https:// ]] ; then
    ppp="$1"
    opop "${ppp}"

  else
    show_usage ; exit 1
  fi
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
  check_number_of_argment 1 "$#"
  sub "$1"
fi