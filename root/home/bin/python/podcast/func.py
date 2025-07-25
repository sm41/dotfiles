
from datetime import datetime
from locale import setlocale, LC_TIME, LC_ALL
from mytool import utils
from os  import getenv
from sys import argv


class Gen_Var:
  def __init__(self):
    self.tmp_dir     = "/tmp"
    self.arg         = argv[1]
    download_dir     = getenv("CLIENT_NETWORK_STORAGE_misc")
    state_file_dir   = getenv("XDG_STATE_HOME")
    self.storage_dir = utils.Ctrl_Path.anlys_path(download_dir, "@podcast")
    self.loaded_yaml = utils.Gen_Obj.load_file(state_file_dir, "python", "podcast.yaml")
    self.root_string = next(iter(self.loaded_yaml))


class Gen_Tag:
  def __init__(self, soup):
    __root_obj = soup.find("channel")
    __item_obj = soup.find("item")

    self.series  = utils.Ctrl_File.zen2han(__root_obj.title.string)
    self.episode = utils.Ctrl_File.zen2han(__item_obj.title.string)
    self.date    = change_format(__item_obj.pubDate.string)
    self.img     = __root_obj.image.url.string.split('?')[0]
    self.url     = __item_obj.enclosure.attrs['url'].split('?')[0]
    self.ext     = utils.Ctrl_File.get_ext(self.url)
    self.name    = utils.Ctrl_File.byte_count(f"[Podcast]_{self.series}_{self.date}_{self.episode}")


class Check_Arg:
  def __init__(self, root_obj: str):
    self._platform = root_obj
    self.reserve_list: list[dict] = []

  def today_list(self, y_data, y_dow_str):
    for key, value in y_data[self._platform].items():
      if y_dow_str in value.get('dow', []):
        self.reserve_list.append({**value})

  def series_name(self, y_data, args):
    for ttl, cnfg in y_data[self._platform].items():
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