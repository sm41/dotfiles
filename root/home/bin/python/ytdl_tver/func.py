
from subprocess import run
from selenium import webdriver
from pathlib  import Path
from bs4  import BeautifulSoup
from time import sleep
from re  import compile
from os  import getenv
from sys import argv
from mytool import abc
from dataclasses import dataclass, field, InitVar


@dataclass
class gen_var:
  def __post_init__(self):
    self.arg          = argv[1]
    self.__env_dl     = getenv("CLIENT_NETWORK_STORAGE_misc")
    self.__env_state  = getenv("XDG_STATE_HOME")
    self.storage_path = abc.ctrl_path.anlys_path(self.__env_dl, "@tver")
    self.loaded_yaml  = abc.load_file(self.__env_state, "python", "tver.yaml")
    self.y_dow        = abc.dow_yesterday(1)


@dataclass
class scrp:
  def selenium(self, url):
    __fx_options = webdriver.FirefoxOptions()
    __fx_options.add_argument("--headless")
    __driver = webdriver.Firefox(options = __fx_options)
    __driver.get(url)
    sleep(5)
    __get_html = __driver.page_source
    self.soup = BeautifulSoup(__get_html, "html.parser")
    __driver.quit()

  def tver(self, soup:BeautifulSoup):
    __url    = soup.find(class_ = compile("episode-row_container")).attrs['href']
    self.url = "https://tver.jp" + __url


@dataclass
class anlys:
  result_list: list = field(default_factory=list)

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


@dataclass
class test:
  def get_base_yaml(self, loaded_yaml):
    self.config = loaded_yaml['tver']['_http']

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
    self.paths, self.output = Path(__filename).parent, abc.ctrl_file.zen2han(Path(__filename).stem)


def ytdlp(paths, id, ext, url):
  method = [
    "yt-dlp",
      "--embed-subs",
      "--paths",  str(paths),
      "--output", f"{id}.{ext}",
    url
  ]
  return method


def ccc(series, episode, url, ext, id, paths, output):
  method = ytdlp(paths, id, ext, url)
  # print(method)
  result = run(method)
  output = abc.ctrl_file.byte_count(output, 245)
  abc.ctrl_path.rnm_path(Path(paths, f"{id}.{ext}"), Path(paths, f"{output}.{ext}"))
  abc.ntfy(result, f"{series}\n{episode}")