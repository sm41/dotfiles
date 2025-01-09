#!/usr/bin/python3

import urllib.request
from bs4   import BeautifulSoup
from plyer import notification
import re
import base64
import argparse
import sys
import os


def check_ststus_code(subject):
  if subject.getcode() != 200:
    print(f"Ststus Code is {subject.getcode()} !!")
    sys.exit()


def analyse_argment():
  parser = argparse.ArgumentParser()

  parser.add_argument('-s', help='station_id', type=str, required=True)
  parser.add_argument('-t', help='title',      type=str, required=True)

  optional_args = parser.parse_args()
  return optional_args


def search_program(search_term, url):
  get_xml = urllib.request.urlopen(url)
  check_ststus_code(get_xml)
  soup = BeautifulSoup(get_xml, "xml")
  prog = soup.find("title", text=re.compile(search_term)).parent

  time_ft:int  = prog.attrs['ft']
  time_to:int  = prog.attrs['to']
  title:str    = prog.title.string
  filename:str = f"{title}_{time_ft[0:4]}_{time_ft[4:6]}_{time_ft[6:8]}_{time_ft[8:12]}"
  return time_ft, time_to, filename


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
  partialkey = base64.b64encode(tmp_auth.encode('utf-8')).decode('utf-8')

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
  os.remove(f"{tmp}/{filename}.m4a")


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

