from sys import argv
from datetime import datetime
from locale import setlocale, LC_TIME, LC_ALL
from mytool import ctrl_date, ctrl_file, ctrl_file, local_path


class gen_var:
  def __init__(self):
    lp = local_path.storage("@podcast")
    ld = local_path.local_data("podcast.yaml")

    self.arg         = argv[1]
    self.tmp_dir     = lp.tmp_dir
    self.storage_dir = lp.storage_dir
    self.loaded_yaml = ctrl_file.yaml_tool.yaml_safe_load(ld.local_data_path)


class gen_tag:
  def __init__(self, soup):
    __root_obj = soup.find("channel")
    __item_obj = soup.find("item")

    self.series  = ctrl_file.ctrl_file.zen2han(__root_obj.title.string)
    self.episode = ctrl_file.ctrl_file.zen2han(__item_obj.title.string)
    self.date    = time.change_format(__item_obj.pubDate.string)
    self.img     = __root_obj.image.url.string.split('?')[0]
    self.url     = __item_obj.enclosure.attrs['url'].split('?')[0]
    self.ext     = ctrl_file.ctrl_file.get_ext(self.url)
    self.name    = ctrl_file.ctrl_file.byte_count(f"[Podcast]_{self.series}_{self.date}_{self.episode}")


class check_arg:
  def __init__(self):
    self.reserve_list: list[dict] = []

  def today_list(self, y_data:list, y_dow_str):
    for value in y_data.values():
      if y_dow_str in value.get('dow', []):
        self.reserve_list.append({**value})

  def series_name(self, y_data:list, args):
    for key, value in y_data.items():
      if key == args:
        self.reserve_list.append({**value})



class time:
  def __init__(self, day_int):
    aaa = ctrl_date.ctrl_date()
    self.n_days_ago_dow = aaa.yesterday(day_int).n_days_ago_dow


  @staticmethod
  def change_format(episode_date):
    setlocale(LC_TIME, (None,None))

    format_str_tz = "%a, %d %b %Y %H:%M:%S %z"
    dt_tz = datetime.strptime(episode_date, format_str_tz)
    yyy = dt_tz.strftime("%Y-%m-%d")
    return yyy


def dl(source:gen_tag, tmp_dir):
  download = [
    "ffmpeg",
      "-loglevel", "warning",
      "-i",   source.url,
      "-i",   source.img,
      "-map", "0:a",
      "-map", "1:v",
      "-metadata:s:v", "title='Album cover'",
      "-metadata:s:v", "comment='Cover (Front)'",
      "-codec", "copy",
    f"{tmp_dir}/{source.name}{source.ext}"
  ]
  return download