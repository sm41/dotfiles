#
function sed_arg(){
  sed -e "${SED_COMMAND}"
}

function zen2han(){
  sed \
    -e 'y/ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ/ABCDEFGHIJKLMNOPQRSTUVWXYZ/' \
    -e 'y/ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ/abcdefghijklmnopqrstuvwxyz/' \
    -e 'y/０１２３４５６７８９/0123456789/' \
    -e 'y/＃：（）/#:\(\)/' \
    -e 'y/ 　/__/'
}