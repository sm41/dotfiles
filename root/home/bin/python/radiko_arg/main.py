
from os import getenv, remove
from re import compile, IGNORECASE
from plyer import notification
from subprocess import run
import func, func_auth, func_dl
from mytool import abc


#JP+都道府県コード ex) 北海道 => JP1    沖縄 => JP47
#国土交通省 https://nlftp.mlit.go.jp/ksj/gml/codelist/PrefCd.html
#Area ID: JP8   https://radiko.jp/v3/station/list/JP8.xml
#
#https://radiko.jp/v3/program/station/date/20301231/TBS.xml
#https://radiko.jp/v3/program/station/weekly/TBS.xml


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

station_id    = optional_args.s.upper()
search_term   = optional_args.t
download_flag = optional_args.dl
fftt = optional_args.ft

url = f"https://radiko.jp/v3/program/station/weekly/{station_id}.xml"
auth1_url = "https://radiko.jp/v2/api/auth1"
auth2_url = "https://radiko.jp/v2/api/auth2"
authkey   = "bcd151073c03b352e1ef2fd66c32209da9ca0afa"

tmp_dir  = "/tmp"
env_dir  = getenv("CLIENT_NETWORK_STORAGE_misc")
storage_dir = abc.anlys_path(env_dir, "@radiko")


def main():

  today_now, days_ago = func.now_time(7)
  soup      = abc.makesoup(url)
  find_list = soup.find_all("title", text=compile(search_term, flags=IGNORECASE))
  program_list = func.search_program(find_list, today_now, days_ago, fftt)
  time_ft, time_to, filename, img = func.branch(program_list, download_flag)

  authtoken = func_auth.auth(auth1_url, auth2_url, authkey)

  download = func_dl.ffmpeg(authtoken['X-Radiko-AuthToken'], station_id, time_ft, time_to, tmp_dir, filename)
  result_1 = run(download)

  encode   = func_dl.encode(tmp_dir, storage_dir, filename, img)
  result_2 = run(encode)


  if result_1.returncode == 0:
    remove(f"{tmp_dir}/{filename}.m4a"),
  else:
    pass

  if result_2.returncode == 0:
    notification.notify(title = "✅ Success", message = f"{filename}.mp3"),
  else:
    notification.notify(title = "⚠️ failed",  message = f"{filename}.mp3")


if __name__ == "__main__":
  main()
