#!/usr/bin/python3

from os import getenv, path
from plyer import notification
from subprocess import run
import func


#JP+都道府県コード ex) 北海道 => JP1    沖縄 => JP47
#国土交通省 https://nlftp.mlit.go.jp/ksj/gml/codelist/PrefCd.html
#Area ID: JP8   https://radiko.jp/v3/station/list/JP8.xml
#
#https://radiko.jp/v3/program/station/date/20301231/TBS.xml
#https://radiko.jp/v3/program/station/weekly/TBS.xml


#Options:
#  -t TITLE        Program title
#  -s STATION      Station ID (see https://radiko.jp/v3/station/region/full.xml)
#    ├ "TBS"      # TBSラジオ
#    ├ "QRR"      # 文化放送
#    ├ "LFR"      # ニッポン放送
#    ├ "RN1"      # ラジオNIKKEI第1
#    ├ "RN2"      # ラジオNIKKEI第2
#    ├ "INT"      # interfm
#    ├ "FMT"      # tokyo fm
#    ├ "FMJ"      # j-wave
#    ├ "IBS"      # LuckyFM 茨城放送
#    ├ "JORF"     # ラジオ日本
#    ├ "BAYFM78"  # bayfm
#    ├ "NACK5"    # nack5
#    ├ "YFM"      # fm yokohama
#    ├ "JOAK"     # NHKラジオ第1（東京）
#    └ "JOAK-FM"  # NHK-FM（東京）

s_dict = {
  "TBS":     "TBSラジオ",
  "QRR":     "文化放送",
  "LFR":     "ニッポン放送",
  "RN1":     "ラジオNIKKEI第1",
  "RN2":     "ラジオNIKKEI第2",
  "INT":     "interfm",
  "FMT":     "tokyo fm",
  "FMJ":     "j-wave",
  "IBS":     "LuckyFM 茨城放送",
  "JORF":    "ラジオ日本",
  "BAYFM78": "bayfm",
  "NACK5":   "nack5",
  "YFM":     "fm yokohama",
  "JOAK":    "NHKラジオ第1（東京）",
  "JOAK-FM": "NHK-FM（東京）",
}


optional_args = func.analyse_argment(s_dict)

station_id  = optional_args.s.upper()
search_term = optional_args.t
dl_flag = optional_args.dl
fftt = optional_args.ft


tmp_dir = "/tmp"
env_var = "CLIENT_NETWORK_STORAGE_www"
storage = getenv(env_var)
path = path.join(storage, "test", "@radiko")

url = f"https://radiko.jp/v3/program/station/weekly/{station_id}.xml"

auth1_url = "https://radiko.jp/v2/api/auth1"
auth2_url = "https://radiko.jp/v2/api/auth2"
authkey   = "bcd151073c03b352e1ef2fd66c32209da9ca0afa"

def main():

  today_now, days_ago = func.now_time(7)
  program_list = func.search_program(search_term, url, today_now, days_ago, fftt)
  time_ft, time_to, filename = func.branch(program_list, dl_flag)

  head_dict_1 = func.set_users_header()
  auth_one    = func.get_header(auth1_url, head_dict_1)
  head_res    = func.set_head_dict(auth_one)
  partialkey  = func.get_partial(head_res, authkey)
  head_dict_2 = func.set_head_dict_2(partialkey, head_res)
  auth_two    = func.get_header(auth2_url, head_dict_2)

  download = func.ffmpeg(head_dict_2['X-Radiko-AuthToken'], station_id, time_ft, time_to, tmp_dir, filename)
  result = run(download)

  encode = func.encode(tmp_dir, path, filename)
  result2 = run(encode)

  func.result(
    result,
    func.delete(tmp_dir, filename),
    "pass"
    )
  func.result(
    result2,
    notification.notify(title = "✅ Success", message = f"{filename}.mp3"),
    "pass"
    # notification.notify(title = "⚠️ failed",  message = f"{filename}.mp3")
    )


if __name__ == "__main__":
  main()