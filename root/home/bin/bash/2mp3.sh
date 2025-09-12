# !/bin/bash

input_file="$1"

filename=${input_file##*/}
basename=${filename%.*}
ext=${filename##*.}




ffmpeg \
  -i "${input_file}" \
  -map 0:a \
  -map 0:v:0 \
  -c:a libmp3lame \
  -b:a 48k \
  -disposition:1 attached_pic \
  -id3v2_version 3 \
  -metadata:s:v title="Album cover" \
  -metadata:s:v comment="Cover (front)" \
  "${basename}.mp3"
