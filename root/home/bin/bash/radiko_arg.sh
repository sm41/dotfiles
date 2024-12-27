#!/bin/bash
set -eu

# variable
TEMP_DIR="/tmp"
REC_DIR="${CLIENT_NETWORK_STORAGE_www}/test/@radiko"
VAR_DIR="${XDG_STATE_HOME}/radiko"
WORK_PATH="$(realpath $(dirname "$0"))"

# source
source "${WORK_PATH}"/_func_check.sh
source "${WORK_PATH}"/_func_ffmpeg.sh


function show_usage(){
  cat << _EOT_
  Usage: $(basename "$0") -s "Station ID" -t "Program title"
    # -t `date +"%m%d%H%M"`.+TITLE
    # -t `date +"%m%d" -d "last monday"`.+TITLE
  Options:
    -t TITLE        Program title
    -s STATION      Station ID (see https://radiko.jp/v3/station/region/full.xml)
      ├ "TBS"      # TBSラジオ
      ├ "QRR"      # 文化放送
      ├ "LFR"      # ニッポン放送
      ├ "RN1"      # ラジオNIKKEI第1
      ├ "RN2"      # ラジオNIKKEI第2
      ├ "INT"      # interfm
      ├ "FMT"      # tokyo fm
      ├ "FMJ"      # j-wave
      ├ "IBS"      # LuckyFM 茨城放送
      ├ "JORF"     # ラジオ日本
      ├ "BAYFM78"  # bayfm
      ├ "NACK5"    # nack5
      ├ "YFM"      # fm yokohama
      ├ "JOAK"     # NHKラジオ第1（東京）
      └ "JOAK-FM"  # NHK-FM（東京）
_EOT_
}

function authorization(){
  # get authorize key
  pid="$$"
  working_path="${HOME}"
  auth1_res="${working_path}/auth1_res.${pid}"

  # Define authorize key value (from http://radiko.jp/apps/js/playerCommon.js)
  AUTHKEY_VALUE="bcd151073c03b352e1ef2fd66c32209da9ca0afa"

  # Create authorize key file
  authkey="${working_path}/authkey.txt"
  if [[ ! -f "${authkey}" ]]  ; then
    printf "%s" "${AUTHKEY_VALUE}" > "${authkey}"
  fi

  # Authorize 1    --cookie "${cookie}" \
  curl \
    --silent \
    --insecure \
    --header "X-Radiko-App: pc_html5" \
    --header "X-Radiko-App-Version: 0.0.1" \
    --header "X-Radiko-Device: pc" \
    --header "X-Radiko-User: dummy_user" \
    --dump-header "${auth1_res}" \
    --output /dev/null \
  "https://radiko.jp/v2/api/auth1"

  # Get partial key
  authtoken=$(awk 'tolower($0) ~/^x-radiko-authtoken: / {print substr($0,21,length($0)-21)}' < "${auth1_res}")
  keyoffset=$(awk 'tolower($0) ~/^x-radiko-keyoffset: / {print substr($0,21,length($0)-21)}' < "${auth1_res}")
  keylength=$(awk 'tolower($0) ~/^x-radiko-keylength: / {print substr($0,21,length($0)-21)}' < "${auth1_res}")
  partialkey=$(dd "if=${authkey}" bs=1 "skip=${keyoffset}" "count=${keylength}" 2> /dev/null | base64)

  # Authorize 2    --cookie "${cookie}" \
  curl \
    --silent \
    --insecure \
    --header "X-Radiko-Device: pc" \
    --header "X-Radiko-User: dummy_user" \
    --header "X-Radiko-AuthToken: ${authtoken}" \
    --header "X-Radiko-PartialKey: ${partialkey}" \
    --output /dev/null \
  "https://radiko.jp/v2/api/auth2"
}

function change_argment_to_URL(){
  if [[ -z "${KKK[@]}" ]] ; then
    notify-send "❌ Error!!" "Contents is not found"
    rm_authkey && exit 1
  else
    TIME_FT="${KKK[0]}"
    TIME_TO="${KKK[1]}"
    DUR="${KKK[2]}"
    TITLE="${KKK[3]}"
  fi

  FILENAME="${TITLE}_${TIME_FT:0:4}-${TIME_FT:4:2}-${TIME_FT:6:2}-${TIME_FT:8:4}"
}


# function conditional_branch(){
#   if   [[ -e "${REC_DIR}/${FILENAME}.m4a" ]]  &&  [[ -e "${REC_DIR}/${FILENAME}.mp3" ]]  ; then
#     ENC_RET_VAL=0
#     del_audio_ffmpeg  "$1"  "$2"
#   elif [[ -e "${REC_DIR}/${FILENAME}.m4a" ]]  &&  [[ ! -e "${REC_DIR}/${FILENAME}.mp3" ]]  ; then
#     enc_audio_ffmpeg  "$1"  "$2"
#     del_audio_ffmpeg  "$1"  "$2"
#   elif [[ ! -e "${REC_DIR}/${FILENAME}.m4a" ]]  &&  [[ -e "${REC_DIR}/${FILENAME}.mp3" ]]  ; then
#     :
#   elif [[ ! -e "${REC_DIR}/${FILENAME}.m4a" ]]  &&  [[ ! -e "${REC_DIR}/${FILENAME}.mp3" ]]  ; then
#     download_by_ffmpeg
#     enc_audio_ffmpeg  "$1"  "$2"
#     del_audio_ffmpeg  "$1"  "$2"
#   fi
# }


function test_branch(){
  download_by_ffmpeg
  enc_audio_ffmpeg    "${TEMP_DIR}/${FILENAME}.m4a"   "mp3"
  delfile             "${TEMP_DIR}/${FILENAME}.m4a"
  move_file           "${TEMP_DIR}/${FILENAME}.mp3"   "${REC_DIR}/${FILENAME}.mp3"
}


# download
# Description = https://kazkn.com/post/2017/bash-loop-ffmpeg/
# 結論からいうと、ffmpeg に </dev/null を足せば解決する。
function download_by_ffmpeg(){
  ffmpeg \
    -loglevel warning \
    -n \
    -fflags +discardcorrupt \
    -headers "X-Radiko-Authtoken: ${authtoken}" \
    -i "https://radiko.jp/v2/api/ts/playlist.m3u8?station_id=${STATION_ID^^}&l=15&ft=${TIME_FT}&to=${TIME_TO}" \
    -acodec copy \
    -vn \
    -bsf:a aac_adtstoasc \
    -movflags faststart \
  "${TEMP_DIR}/${FILENAME}.m4a" \
  </dev/null
}

function delfile(){
  if   [[ "${ENC_RET_VAL}" -eq 0 ]]  ; then
    rm "$1"
  fi
}

function move_file(){
  mv "$1" "$2"
}

function rm_authkey(){
  rm "auth1_res.${pid}" "authkey.txt"
}

function ntfy(){
  if   [[ "${ENC_RET_VAL}" -eq 0 ]]  ; then
    notify-send   "✅ Success"   "🎵 $(basename "${1%.*}"."$2")"
  elif [[ "${ENC_RET_VAL}" -eq 1 ]]  ; then
    notify-send   "❌ Failed"    "🎵 $(basename "$1")"
  fi
}


function main(){
  while read -a KKK
  do
    authorization
    change_argment_to_URL
    # conditional_branch      "${TEMP_DIR}/${FILENAME}.m4a"  "mp3"
    test_branch
    rm_authkey
    ntfy                "${TEMP_DIR}/${FILENAME}.m4a"   "mp3"

  done < <(awk '($2 > '`date +"%Y%m%d%H%M%S" --date '168 hours ago'`') && ($2 < '`date +"%Y%m%d%H%M%S"`')' "${VAR_DIR}/week_${STATION_ID^^}_list" | grep -iP ${TITLE_REGEX} )
}



if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then

  mkdir -pv "${REC_DIR}"

  check_number_of_argment 4 "$#"

  # set option
  while getopts ":s:t:" opt ;
  do
    case $opt in
      s ) STATION_ID="${OPTARG}" ;;
      t ) TITLE_REGEX="${OPTARG}" ;;
      \? ) show_usage ; exit 1 ;;
    esac
  done

  main

fi