
from datetime import datetime, date, timedelta
from locale import setlocale, LC_TIME, LC_ALL
# from bs4 import BeautifulSoup
from re  import match
from mytool import abc
from os  import getenv
from sys import argv


class gen_var:
  def __init__(self):
    self.arg            = argv[1]
    self.tmp_dir        = "/tmp"
    self.download_dir   = getenv("CLIENT_NETWORK_STORAGE_misc")
    self.state_file_dir = getenv("XDG_STATE_HOME")
    self.storage_dir    = abc.anlys_path(self.download_dir, "@podcast")


def change_format(episode_date):
  setlocale(LC_TIME, (None,None))

  format_str_tz = "%a, %d %b %Y %H:%M:%S %z"
  dt_tz = datetime.strptime(episode_date, format_str_tz)
  yyy = dt_tz.strftime("%Y-%m-%d")
  return yyy


def get_searchitem(rrr, search_term):

  if search_term is None:
    search_term = ".+"

  for iii in rrr:
    if match(search_term, iii.title.string):
      target_item = iii
      break

  return target_item


class gen_tag:
  def __init__(self, soup, search_term):
    __root_obj   = soup.find("channel")
    __item_list  = soup.find_all("item", limit=50)
    __target_obj = get_searchitem(__item_list, search_term)

    self.series  = abc.zen2han(__root_obj.title.string)
    self.episode = abc.zen2han(__target_obj.title.string)
    self.date    = change_format(__target_obj.pubDate.string)
    self.img     = __root_obj.image.url.string.split('?')[0]
    self.url     = __target_obj.enclosure.attrs['url'].split('?')[0]
    self.name    = f"[Podcast]_{self.series}_{self.date}_{self.episode}.mp3"


class check_arg:
  def __init__(self):
    self.eee = []

  def get_today_list2(self, y_data, y_dow_str):
    for key, value in y_data['megaphone'].items():
      for pln in value['plan']:
        if pln['dow'] == y_dow_str:
          self.eee.append({**value, "plan": pln})

  def yui2(self, y_data, args):
    for ttl, cnfg in y_data['megaphone'].items():
      if ttl == args:
        self.eee.append({**cnfg, "plan": cnfg['plan'][0]})



def dl(url, img, filename, tmp_dir):
  download = [
    "ffmpeg",
      "-loglevel", "warning",
      "-i",   url,
      "-i",   img,
      "-map", "0:a",
      "-map", "1:v",
      "-metadata:s:v", "title='Album cover'",
      "-metadata:s:v", "comment='Cover (Front)'",
      "-codec", "copy",
    f"{tmp_dir}/{filename}"
  ]
  return download