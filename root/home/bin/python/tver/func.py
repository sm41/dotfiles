from subprocess import run
from pathlib  import Path
from sys import argv
from mytool import ctrl_date, ctrl_path, ctrl_file, notify, local_path
import func

class Gen_Var:
  def __init__(self):
    lp = local_path.storage("@tver")
    ld = local_path.local_data("tver.yaml")

    self.arg          = argv[1]
    self.storage_dir  = lp.storage_dir
    self.loaded_yaml  = ctrl_file.yaml_tool.yaml_safe_load(ld.local_data_path)


class time:
  def __init__(self, day_int):
    self.date = ctrl_date.ctrl_date()
    self.date.yesterday(day_int)
    self.date.quarte().quarte_date



class Anlys:
  def __init__(self):
    self.result_list = []

  def find_key_dict(self, data, target_key):
    if isinstance(data, dict):
      for key, value in data.items():
        if key.startswith("_"):
          continue
        if key == target_key:
          self.result_list.append(value)
          return self.result_list
        result = self.find_key_dict(value, target_key)
        if result is not None:
          return result

  def find_key_value_list(self, data, target_key):
    if isinstance(data, dict):
      for key1, value1 in data.items():
        if key1.startswith("_"):
          continue
        if "dow" not in value1:
          self.find_key_value_list(value1, target_key)
        else:
          for dow_item in value1['dow']:
            if dow_item == target_key:
              self.result_list.append(value1)
              # break  # 同じtitleのデータが複数回追加されないようにする


class Gen_Tag:
  def get_base_yaml(self, loaded_yaml):
    self.config = loaded_yaml['_http']

  def integrate(self, url, down_dir, yaml_config):
    __header = yaml_config['header']
    __cmd_ytdlp = [
      "yt-dlp",
        "--paths",  f"home:{down_dir}",
        "--output", f"{__header}",
        "--print",  "series",
        "--print",  "episode",
        "--print",  "original_url",
        "--print",  "filename",
        "--print",  "ext",
        "--print",  "id",
      url
    ]
    __ddd = run(__cmd_ytdlp, capture_output=True, text=True).stdout.strip()
    self.series, self.episode, self.url, __filename, self.ext, self.id = __ddd.splitlines()
    self.paths, self.output = Path(__filename).parent, ctrl_file.ctrl_file.zen2han(Path(__filename).stem)


def insert_quoter(filename:str, year, q_date):

  # if year is None or q_date is None:
  if None in (year, q_date):
    return filename

  if filename.startswith("[ドラマ]"):
    return filename.replace('_', f'_[{year}-Q{q_date}]_', 1)
  else:
    return filename


def ytdlp(paths, id, ext, url):
  method = [
    "yt-dlp",
      "--embed-subs",
      "--paths",  str(paths),
      "--output", f"{id}.{ext}",
    url
  ]
  return method


def ccc(tag_tag:func.Gen_Tag, year, q_date):
  method = ytdlp(tag_tag.paths, tag_tag.id, tag_tag.ext, tag_tag.url)
  result = run(method)
  tag_tag.output = insert_quoter(tag_tag.output, year, q_date)
  tag_tag.output = ctrl_file.ctrl_file.byte_count(tag_tag.output, 245)
  ctrl_path.ctrl_path.rnm_path(Path(tag_tag.paths, f"{tag_tag.id}.{tag_tag.ext}"), Path(tag_tag.paths, f"{tag_tag.output}.{tag_tag.ext}"))
  notify.ntfy(result, f"{tag_tag.series}\n{tag_tag.episode}")