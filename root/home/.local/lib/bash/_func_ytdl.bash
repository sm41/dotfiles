#
function category(){
  CATEGORY_DIR=/$(echo $1 |awk -F "/" '{print $4}')
  ACT_NAME_DIR=/$(echo $1 |awk -F "/" '{print $5}')

  mkdir -pv        ${REC_DIR}${CATEGORY_DIR}${ACT_NAME_DIR}
  mkdir -pv ${HOME}${VAR_DIR}${CATEGORY_DIR}${ACT_NAME_DIR}
  touch     $_/${ACT_NAME_DIR}.dllog

  yt-dlp \
    --download-archive ${HOME}${VAR_DIR}${CATEGORY_DIR}${ACT_NAME_DIR}${ACT_NAME_DIR}.dllog \
    --paths ${REC_DIR}${CATEGORY_DIR}${ACT_NAME_DIR} \
    --output "[%(upload_date>%Y-%m-%d)s]_[%(id)s]_%(title)s.%(ext)s" \
  "https://pornhub.com${CATEGORY_DIR}${ACT_NAME_DIR}/videos/upload"
}


function viewkey(){
  yt-dlp \
    --paths ${REC_DIR} \
    --output "[%(upload_date>%Y-%m-%d)s]_[%(id)s]_%(title)s.%(ext)s" \
  $1
}


function download_podcast_list(){
  yt-dlp \
    --batch-file ${HOME}${VAR_DIR}/${DL_FILE} \
    --paths ${REC_DIR} \
    --output '[Podcast]_%(series)s_%(upload_date>%Y-%m-%d)s_%(title)s.%(ext)s'
}


function url_is_apple(){
  yt-dlp \
    --paths ${REC_DIR} \
    --output '[Podcast]_%(series)s_%(upload_date>%Y-%m-%d)s_%(title)s.%(ext)s' \
  "$1"
}


function download_tver_list(){
  yt-dlp \
    --batch-file ${HOME}${VAR_DIR}/${DL_FILE} \
    --embed-subs \
    --paths ${REC_DIR} \
    --output '[%(webpage_url_domain)s]_%(series)s_%(episode)s.%(ext)s'
}


function url_is_tver(){
  yt-dlp \
    --embed-subs \
    --paths ${REC_DIR} \
    --output '[%(webpage_url_domain)s]_%(series)s_%(episode)s.%(ext)s' \
  $1
}