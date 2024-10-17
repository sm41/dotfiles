# enc
function enc_audio_ffmpeg(){

  INPUT_FILE="$1"
  TARGET_EXT="$2"

  ffmpeg \
    -n \
    -i "${INPUT_FILE}" \
    -loglevel info \
    -b:a 48k \
  "${INPUT_FILE%.*}.${TARGET_EXT}" \
  </dev/null

  ENC_RET_VAL="$?"
}

