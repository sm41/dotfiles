#!/bin/bash

# 初期化
group=""; mode=""; n=""

# 引数が3つ必要
[ $# -ne 3 ] && echo "Usage: $0 <st|dlc1|dlc2> <e|n|h|hdst|inf> <n (1〜...)>" && exit 1

# 各引数を順番に確認
for arg in "$@"; do
  case "$arg" in
    st|dlc1|dlc2) group="$arg" ;;
    e|n|h|hdst|inf) mode="$arg" ;;
    ''|*[!0-9]*) echo "Invalid number: $arg"; exit 1 ;;  # 数字でないものは除外
    *) n="$arg" ;;
  esac
done

# チェック
[ -z "$group" ] && echo "Missing group" && exit 1
[ -z "$mode" ] && echo "Missing mode" && exit 1
[ -z "$n" ] && echo "Missing n" && exit 1

# groupに応じたNを設定
case "$group" in
  st)    N=147 ;;
  dlc1)  N=19  ;;
  dlc2)  N=40  ;;
esac

# nのバリデーション
[ "$n" -lt 1 ] || [ "$n" -gt "$N" ] && echo "n must be between 1 and $N (got $n)" && exit 1

# グループ・モードごとの L, M を設定
case "$group" in
  st)
    case "$mode" in
      e)    L=0.5;  M=1.5  ;;
      n)    L=1.0;  M=2.4  ;;
      h)    L=2.0;  M=6.0  ;;
      hdst) L=7.0;  M=15.0 ;;
      inf)  L=16.0; M=28.0 ;;
      *) echo "Invalid mode: $mode"; exit 1 ;;
    esac
    ;;
  dlc1)
    case "$mode" in
      e)    L=2.0;  M=2.5  ;;
      n)    L=2.5;  M=3.0  ;;
      h)    L=7.0;  M=9.0  ;;
      hdst) L=15.0; M=18.0 ;;
      inf)  L=28.0; M=31.0 ;;
      *) echo "Invalid mode: $mode"; exit 1 ;;
    esac
    ;;
  dlc2)
    case "$mode" in
      e)    L=2.0;  M=2.5  ;;
      n)    L=3.0;  M=4.0  ;;
      h)    L=9.0;  M=11.0 ;;
      hdst) L=18.0; M=21.0 ;;
      inf)  L=31.0; M=35.0 ;;
      *) echo "Invalid mode: $mode"; exit 1 ;;
    esac
    ;;
esac

# 計算と出力
dc=$(echo "scale=3; $L + (($M - $L) * ($n - 1)) / ($N - 1)" | bc -l)

echo -e "・Mission_Pack : ${group} \n・Mission_Number : ${n} \n・難易度係数: ${dc}"