#!/usr/bin/python3

import urllib.request
from argparse import ArgumentParser
from base64 import b64encode
from bs4   import BeautifulSoup
from os import remove
from plyer import notification
from re import compile, IGNORECASE
from sys import exit
from datetime import datetime, timedelta
# from locale   import setlocale, LC_TIME


def check_ststus_code(subject):
  if subject.getcode() != 200:
    print(f"Ststus Code is {subject.getcode()} !!")
    exit()


def analyse_argment():
  parser = ArgumentParser()

  parser.add_argument('-s',  help='station_id',     type=str, required=True)
  parser.add_argument('-t',  help='title',          type=str, required=True)
  parser.add_argument('-ft', help='ft',             type=str, required=False)
  parser.add_argument('-dl', help='dl',  action='store_true', required=False)

  optional_args = parser.parse_args()
  return optional_args


def now_time(day_int:int):
  get_now = datetime.now()
  get_past = get_now - timedelta( days = day_int )

  today_now:str = get_now.strftime('%Y%m%d%H%M')+'00'
  days_ago:str = get_past.strftime('%Y%m%d%H%M')+'00'
  # return today_now.strftime('%Y%m%d%H%M')+'00'
  return today_now, days_ago


def search_program(search_term, url, today_now, days_ago, fftt):
  get_xml = urllib.request.urlopen(url)
  check_ststus_code(get_xml)
  soup = BeautifulSoup(get_xml, "xml")
  keyword_list = soup.find_all("title", text=compile(search_term, flags=IGNORECASE))

  program_list = []

  for keyword in keyword_list:
    prog_detail = keyword.parent
    if   days_ago >  prog_detail.attrs['to'] >  today_now:
      continue
    elif days_ago <= prog_detail.attrs['to'] <= today_now:
      ddd = {
        "ft":       prog_detail.attrs['ft'],
        "to":       prog_detail.attrs['to'],
        "time":     f"{prog_detail.attrs['ft'][0:4]}_{prog_detail.attrs['ft'][4:6]}_{prog_detail.attrs['ft'][6:8]}_{prog_detail.attrs['ft'][8:12]}",
        "title":    prog_detail.title.string,
      }
      program_list.append(ddd)


  if fftt is None:
    return program_list

  elif len(fftt) != 14:
    print("There is an error in the '-ft' option")
    exit()

  elif len(fftt) == 14:
    hogefuga_list = []
    for rrr in program_list:
      if rrr['ft'] == fftt:
        hogefuga_list.append(rrr)
    return hogefuga_list


def branch(program_list, dl_flag):

  if   len(program_list) > 1:
    if dl_flag == True:
      notification.notify(title = "⚠️ failed",  message = "upper")
    elif dl_flag == False:
      for vvv in program_list:
        print(vvv)
      print(f"Result {len(program_list)} Programs")
    exit()

  elif len(program_list) == 1:
    if dl_flag == True:
      return program_list[0]['ft'], program_list[0]['to'], f"{program_list[0]['title']}_{program_list[0]['time']}"
    elif dl_flag == False:
      print(program_list)
      print("You can download it by adding '-dl' flag")
    exit()

  elif len(program_list) == 0:
    if dl_flag == True:
      notification.notify(title = "⚠️ failed",  message = "upper")
    elif dl_flag == False:
      print("Program is Not Found !!")
    exit()


def set_users_header():
  head_dict_1 = {
  "X-Radiko-App":         "pc_html5",
  "X-Radiko-App-Version": "0.0.1",
  "X-Radiko-Device":      "pc",
  "X-Radiko-User":        "dummy_user"
  }
  return head_dict_1


def get_header(auth_n_url:str, head_dict_n:list):
  req = urllib.request.Request(url=auth_n_url, headers=head_dict_n, method="GET")
  with urllib.request.urlopen(req) as res:
    auth_n = res.headers
  return auth_n


def set_head_dict(auth_one):
  head_res = {
    "AuthToken": str(auth_one['x-radiko-authtoken']),
    "KeyLength": int(auth_one["x-radiko-keylength"]),
    "KeyOffset": int(auth_one["x-radiko-keyoffset"]),
  }
  return head_res


def get_partial(head_res, authkey):
  tmp_auth = authkey[head_res['KeyOffset']:  head_res['KeyOffset'] + head_res['KeyLength']]
  partialkey = b64encode(tmp_auth.encode('utf-8')).decode('utf-8')

  return partialkey


def set_head_dict_2(partialkey, head_res):
  head_dict_2 = {
    "X-Radiko-Device":      "pc",
    "X-Radiko-User":        "dummy_user",
    "X-Radiko-AuthToken":   head_res['AuthToken'],
    "X-Radiko-PartialKey":  partialkey
  }
  return head_dict_2


def ffmpeg(authtoken, station_id, time_ft, time_to, path, filename):
  download = [
    "ffmpeg",
      "-loglevel", "warning",
      "-n",
      "-fflags", "+discardcorrupt",
      "-headers", f"X-Radiko-Authtoken: {authtoken}",
      "-i", f"https://radiko.jp/v2/api/ts/playlist.m3u8?station_id={station_id}&l=15&ft={time_ft}&to={time_to}",
      "-acodec", "copy",
      "-vn",
      "-bsf:a", "aac_adtstoasc",
      "-movflags", "faststart",
    f"{path}/{filename}.m4a"
  ]
  return download


def encode(tmp, path, filename):
  encode = [
    "ffmpeg",
      "-n",
      "-i",  f"{tmp}/{filename}.m4a",
      "-loglevel", "warning",
      "-b:a", "48k",
    f"{path}/{filename}.mp3"
  ]
  return encode


def delete(tmp, filename):
  remove(f"{tmp}/{filename}.m4a")


def result(result, success, failure):
  if result.returncode == 0:
    success
  else:
    failure


# def ntfy(result, upper:str):
#   if result.returncode == 0:
#     notification.notify(title = "✅ Success", message = upper)
#   else:
#     notification.notify(title = "⚠️ failed",  message = upper)

