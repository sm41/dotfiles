# enc
function enc_audio_ffmpeg(){

  INPUT_FILE=$1
  TARGET_EXT=$2

  ffmpeg \
    -n \
    -i ${INPUT_FILE} \
    -loglevel info \
    -b:a 48k \
  ${INPUT_FILE%.*}.${TARGET_EXT} \
  </dev/null

  ENC_RET_VAL=$?
}

function del_audio_ffmpeg(){
  if   [[ ${ENC_RET_VAL} -eq 0 ]]  ; then
    rm $1  &&  notify-send "✅ Success" "🎵 $(basename ${1%.*}.$2)"
  elif [[ ${ENC_RET_VAL} -eq 1 ]]  ; then
    rm $1  &&  notify-send "❌ Failed"  "🎵 $(basename $1)"
  fi
}

# change aspect ratio
function change_asp_ffmpeg(){

  VIDEO_FILE_PATH=$1
  ASPECT_RATIO=$2

  ffmpeg \
    -n \
    -i ${VIDEO_FILE_PATH} \
    -c copy \
    -aspect ${ASPECT_RATIO} \
  ${VIDEO_FILE_PATH%/*}/__${VIDEO_FILE_PATH##*/}
}

# change container extension
function change_container_ffmpeg(){

  INPUT_FILE=$1
  TARGET_EXT=$2

  ffmpeg \
    -n \
    -i ${INPUT_FILE} \
    -c copy \
  ${INPUT_FILE%.*}.${TARGET_EXT} \
  </dev/null
}