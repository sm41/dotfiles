#!/bin/bash
set -eu

# JP+都道府県コード ex) 北海道 => JP1    沖縄 => JP47
# 国土交通省 https://nlftp.mlit.go.jp/ksj/gml/codelist/PrefCd.html
# Area ID: JP8   https://radiko.jp/v3/station/list/JP8.xml

# https://radiko.jp/v3/program/station/date/20301231/TBS.xml
# https://radiko.jp/v3/program/station/weekly/TBS.xml

VAR_DIR=/.local/state/radiko

mkdir -pv ${HOME}${VAR_DIR}

# check status code
if   [[ $(curl -s -o /dev/null -w '%{http_code}\n' "https://radiko.jp/v3/station/list/JP8.xml") != 200 ]] ; then
  notify-send "❌ Error" "AREA_ID_HTTP_STATUS_CODE" && exit 1
elif [[ $(curl -s -o /dev/null -w '%{http_code}\n' "https://radiko.jp/v3/program/station/weekly/TBS.xml") = !200 ]] ; then
  notify-send "❌ Error" "WEEKLY_HTTP_STATUS_CODE"  && exit 1
fi

# [ ',' / csv ],[ ' ' / list ]
function var_style(){
  paste --delimiters="$1" \
    <(grep -oP '(?<=ft=")[0-9]+(?=")'       ${HOME}${VAR_DIR}/week_${STATION_ID}.xml ) \
    <(grep -oP '(?<=to=")[0-9]+(?=")'       ${HOME}${VAR_DIR}/week_${STATION_ID}.xml ) \
    <(grep -oP '(?<=dur=")[0-9]+(?=")'      ${HOME}${VAR_DIR}/week_${STATION_ID}.xml | awk '{print $1 / 60}' ) \
    <(grep -oP '(?<=<title>).+(?=</title>)' ${HOME}${VAR_DIR}/week_${STATION_ID}.xml | sed -e 's/ /_/g' ) \
    | sed -E '/^[0-9]{8}050000.[0-9]{14}/i \ ' \
    | awk '{printf "%14s %14s %3s %s\n",$1,$2,$3,$4}' \
  > ${HOME}${VAR_DIR}/week_${STATION_ID}_"$2" \
  && rm ${HOME}${VAR_DIR}/week_${STATION_ID}.xml
}

# download program list
while read STATION_ID
do
  curl --silent "https://radiko.jp/v3/program/station/weekly/${STATION_ID}.xml" > ${HOME}${VAR_DIR}/week_${STATION_ID}.xml
  var_style ' ' list
done < <(curl --silent "https://radiko.jp/v3/station/list/JP8.xml" | grep --only-matching --perl-regexp '(?<=<id>).+(?=</id>)' )

notify-send "✅ Success" "$(basename $0)"