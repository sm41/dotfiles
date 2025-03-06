
from datetime import datetime, timedelta
from argparse import ArgumentParser
from plyer  import notification
from sys import exit
from mytool import abc
from os  import getenv


class check_arg:

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

  def __init__(self):
    __parser = ArgumentParser()
    __parser.add_argument('-s',  help='station_id', required=True,  type=str.upper, choices=self.s_dict.keys())
    __parser.add_argument('-t',  help='title',      required=True,  type=str)
    __parser.add_argument('-ft', help='ft',         required=False, type=str)
    __parser.add_argument('-dl', help='download',   required=False, action='store_true')

    __optional_args = __parser.parse_args()

    self.station_id  = __optional_args.s.upper()
    self.search_term = __optional_args.t
    self.dl_flag     = __optional_args.dl
    self.fftt        = __optional_args.ft


class gen_var:
  def __init__(self):
    self.tmp_dir  = "/tmp"
    __env_dir  = getenv("CLIENT_NETWORK_STORAGE_misc")
    self.storage_path = abc.anlys_path(__env_dir, "@radiko")


class gen_link:
  def __init__(self, station_id):
    self.auth1_url = "https://radiko.jp/v2/api/auth1"
    self.auth2_url = "https://radiko.jp/v2/api/auth2"
    self.authkey   = "bcd151073c03b352e1ef2fd66c32209da9ca0afa"
    self.url = f"https://radiko.jp/v3/program/station/weekly/{station_id}.xml"


class time:
  def __init__(self, day_int):
    __get_now  = datetime.now()
    __get_past = __get_now - timedelta( days = day_int )
    self.today_now = __get_now.strftime('%Y%m%d%H%M')+'00'
    self.days_ago = __get_past.strftime('%Y%m%d%H%M')+'00'


def search_program(find_list, today_now, days_ago, fftt):

  program_list = []

  for keyword in find_list:
    prog_detail = keyword.parent
    if   days_ago >  prog_detail.attrs['to'] >  today_now:
      continue
    elif days_ago <= prog_detail.attrs['to'] <= today_now:
      ddd = {
        "ft":       prog_detail.attrs['ft'],
        "to":       prog_detail.attrs['to'],
        "time":     f"{prog_detail.attrs['ft'][0:4]}-{prog_detail.attrs['ft'][4:6]}-{prog_detail.attrs['ft'][6:8]}-{prog_detail.attrs['ft'][8:12]}",
        "img":      prog_detail.img.string,
        "title":    abc.zen2han(prog_detail.title.string),
      }
      program_list.append(ddd)


  if fftt is None:
    return program_list

  elif len(fftt) != 14:
    exit("There is an error in the '-ft' option")

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
      print(f"📢 Result {len(program_list)} Programs")
    exit()

  elif len(program_list) == 1:
    if dl_flag == True:
      return program_list[0]['ft'], program_list[0]['to'], f"{program_list[0]['title']}_{program_list[0]['time']}", program_list[0]['img']
    elif dl_flag == False:
      print(program_list)
      print("✅ You can download it by adding '-dl' flag")
    exit()

  elif len(program_list) == 0:
    if dl_flag == True:
      notification.notify(title = "⚠️ failed",  message = "upper")
    elif dl_flag == False:
      print("⚠️ Program is Not Found !!")
    exit()



class s_pr:
  def __init__(self, find_list, today_now, days_ago, fftt):

    for keyword in find_list:
      prog_detail = keyword.parent
      if   days_ago >  prog_detail.attrs['to'] >  today_now:
        continue
      elif days_ago <= prog_detail.attrs['to'] <= today_now:

        self.ft =  prog_detail.attrs['ft'],
        self.to =  prog_detail.attrs['to'],
        self.time  =  f"{prog_detail.attrs['ft'][0:4]}-{prog_detail.attrs['ft'][4:6]}-{prog_detail.attrs['ft'][6:8]}-{prog_detail.attrs['ft'][8:12]}",
        self.title =  abc.zen2han(prog_detail.title.string),
        self.img   =  prog_detail.img.string,



class fastforward:
  def __init__(self):
    pass

  def dl(self, authtoken, station_id, time_ft, time_to, path, filename):
    self.download = [
      "ffmpeg",
        "-loglevel", "warning",
        "-n",
        "-headers", f"X-Radiko-Authtoken: {authtoken}",
        "-i", f"https://radiko.jp/v2/api/ts/playlist.m3u8?station_id={station_id}&l=15&ft={time_ft}&to={time_to}",
        "-codec", "copy",
      f"{path}/{filename}.m4a"
    ]

  def enc(self, tmp, path, filename, img):
    self.encode = [
      "ffmpeg",
        "-loglevel", "warning",
        "-n",
        "-i",  f"{tmp}/{filename}.m4a",
        "-i",  f"{img}",
        "-map", "0",
        "-map", "1",
        "-metadata:s:v", "title='Album cover'",
        "-metadata:s:v", "comment='Cover (Front)'",
        "-b:a", "48k",
      f"{path}/{filename}.mp3"
    ]