#!/bin/bash

# 初期化
GROUP=""; MODE=""; TARGET_MISSION=""

# 引数が3つ必要
[ $# -ne 3 ] && echo "Usage: $0 <st|dlc1|dlc2> <e|n|h|hdst|inf> <TARGET_MISSION (1〜...)>" && exit 1

# 各引数を順番に確認
for arg in "$@"; do
  case "${arg}" in
    st|dlc1|dlc2) GROUP="${arg}" ;;
    e|n|h|hdst|inf) MODE="${arg}" ;;
    ''|*[!0-9]*) echo "Invalid number: ${arg}"; exit 1 ;;  # 数字でないものは除外
    *) TARGET_MISSION="${arg}" ;;
  esac
done

# チェック
[ -z "${GROUP}" ] && echo "Missing GROUP" && exit 1
[ -z "${MODE}" ]  && echo "Missing MODE"  && exit 1
[ -z "${TARGET_MISSION}" ] && echo "Missing TARGET_MISSION" && exit 1

# GROUPに応じたLAST_MISSIONを設定
case "$GROUP" in
  st)    LAST_MISSION=147 ;;
  dlc1)  LAST_MISSION=19  ;;
  dlc2)  LAST_MISSION=40  ;;
esac

# TARGET_MISSIONのバリデーション
[ "${TARGET_MISSION}" -lt 1 ] || [ "${TARGET_MISSION}" -gt "${LAST_MISSION}" ] && echo "TARGET_MISSION must be between 1 and ${LAST_MISSION} (got ${TARGET_MISSION})" && exit 1

# グループ・モードごとの MIN_D, MAX_D を設定
case "$GROUP" in
  st)
    case "$MODE" in
      e)    MIN_D=0.5;  MAX_D=1.5  ;;
      n)    MIN_D=1.0;  MAX_D=2.4  ;;
      h)    MIN_D=2.0;  MAX_D=6.0  ;;
      hdst) MIN_D=7.0;  MAX_D=15.0 ;;
      inf)  MIN_D=16.0; MAX_D=28.0 ;;
      *) echo "Invalid MODE: $MODE"; exit 1 ;;
    esac
    ;;
  dlc1)
    case "$MODE" in
      e)    MIN_D=2.0;  MAX_D=2.5  ;;
      n)    MIN_D=2.5;  MAX_D=3.0  ;;
      h)    MIN_D=7.0;  MAX_D=9.0  ;;
      hdst) MIN_D=15.0; MAX_D=18.0 ;;
      inf)  MIN_D=28.0; MAX_D=31.0 ;;
      *) echo "Invalid MODE: $MODE"; exit 1 ;;
    esac
    ;;
  dlc2)
    case "$MODE" in
      e)    MIN_D=2.0;  MAX_D=2.5  ;;
      n)    MIN_D=3.0;  MAX_D=4.0  ;;
      h)    MIN_D=9.0;  MAX_D=11.0 ;;
      hdst) MIN_D=18.0; MAX_D=21.0 ;;
      inf)  MIN_D=31.0; MAX_D=35.0 ;;
      *) echo "Invalid MODE: $MODE"; exit 1 ;;
    esac
    ;;
esac

# 計算と出力
difficulty_coefficient=$(bc -l <<< "scale=3; ${MIN_D} + ((${MAX_D} - ${MIN_D}) * (${TARGET_MISSION} - 1)) / (${LAST_MISSION} - 1)")

cat << EOF
・Mission_Pack   : ${GROUP}
・Mission_Number : ${TARGET_MISSION}
・難易度係数     : ${difficulty_coefficient}
EOF