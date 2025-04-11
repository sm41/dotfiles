
from datetime import datetime
from locale import setlocale, LC_TIME, LC_ALL
from mytool import abc
from os  import getenv
from sys import argv
from dataclasses import dataclass, InitVar, field

@dataclass
class gen_var:
  tmp_dir:str = "/tmp"

  def __post_init__(self):
    self.arg          = argv[1]
    __download_dir    = getenv("CLIENT_NETWORK_STORAGE_misc")
    __state_file_dir  = getenv("XDG_STATE_HOME")
    self.storage_dir  = abc.ctrl_path.anlys_path(__download_dir, "@podcast")
    self.loaded_yaml  = abc.gen_obj.load_file(__state_file_dir, "python", "ppp.yaml")
    self.y_dow        = abc.dow_yesterday(1)


@dataclass
class gen_tag:
  soup: InitVar

  def __post_init__(self, soup):
    __root_obj = soup.find("channel")
    __item_obj = soup.find("item")

    self.series  = abc.ctrl_file.zen2han(__root_obj.title.string)
    self.episode = abc.ctrl_file.zen2han(__item_obj.title.string)
    self.date    = change_format(__item_obj.pubDate.string)
    self.img     = __root_obj.image.url.string.split('?')[0]
    self.url     = __item_obj.enclosure.attrs['url'].split('?')[0]
    self.ext     = abc.ctrl_file.get_ext(self.url)
    self.name    = abc.ctrl_file.byte_count(f"[Podcast]_{self.series}_{self.date}_{self.episode}")


@dataclass
class check_arg:
  reserve_list: list = field(default_factory=list)
  __platform: str = 'megaphone'

  def today_list(self, y_data, y_dow_str):
    for key, value in y_data[self.__platform].items():
      for pln in value['dow']:
        if pln == y_dow_str:
          self.reserve_list.append({**value, "plan": pln})

  def series_name(self, y_data, args):
    for ttl, cnfg in y_data[self.__platform].items():
      if ttl == args:
        self.reserve_list.append({**cnfg})


def change_format(episode_date):
  setlocale(LC_TIME, (None,None))

  format_str_tz = "%a, %d %b %Y %H:%M:%S %z"
  dt_tz = datetime.strptime(episode_date, format_str_tz)
  yyy = dt_tz.strftime("%Y-%m-%d")
  return yyy


def dl(url, img, filename, ext, tmp_dir):
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
    f"{tmp_dir}/{filename}{ext}"
  ]
  return download