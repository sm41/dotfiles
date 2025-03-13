
from subprocess import run
from selenium import webdriver
from pathlib  import Path
from bs4  import BeautifulSoup
from time import sleep
from re  import compile
from os  import getenv
from sys import argv
from mytool import abc


class gen_var:
  def __init__(self):
    self.arg          = argv[1]
    __env_dl          = getenv("CLIENT_NETWORK_STORAGE_misc")
    __env_state       = getenv("XDG_STATE_HOME")
    self.storage_path = abc.ctrl_path.anlys_path(__env_dl, "@tver")
    self.loaded_yaml  = abc.load_yaml(__env_state, "python", "tver.yaml")
    self.y_dow        = abc.dow_yesterday(1)


class scrp:
  def __init__(self):
    pass

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


class rty:
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


class test:
  def __init__(self):
    self.__pre_series  = "series"
    self.__pre_episode = "episode"
    self.__pre_url     = "original_url"
    self.__pre_filname = "filename"
    self.__pre_ext     = "ext"
    self.__pre_id      = "id"

  def get_base_yaml(self, loaded_yaml):
    self.config = loaded_yaml['tver']['_http']

  def integrate(self, url, down_dir, yaml_config):
    __header = yaml_config['header']
    __cmd_ytdlp = [
      "yt-dlp",
        "--paths",  f"home:{down_dir}",
        "--output", f"{__header}",
        "--print",  self.__pre_series,
        "--print",  self.__pre_episode,
        "--print",  self.__pre_url,
        "--print",  self.__pre_filname,
        "--print",  self.__pre_ext,
        "--print",  self.__pre_id,
      url
    ]
    __ddd = run(__cmd_ytdlp, capture_output=True, text=True).stdout.strip()
    self.series, self.episode, self.url, __ppp, self.ext, self.id = __ddd.splitlines()
    self.paths, self.output = Path(__ppp).parent, abc.ctrl_file.zen2han(Path(__ppp).stem)


def ytdlp(paths, id, ext, link):
  method = [
    "yt-dlp",
      "--embed-subs",
      "--paths",  str(paths),
      "--output", f"{id}.{ext}",
    link
  ]
  return method


def ccc(series, episode, url, ext, id, paths, output):
  method = ytdlp(paths, id, ext, url)
  # print(method)
  result = run(method)
  output = abc.ctrl_file.byte_count(output, 245)
  abc.ctrl_path.rnm(Path(paths, f"{id}.{ext}"), Path(paths, f"{output}.{ext}"))
  abc.ntfy(result, f"{series}\n{episode}")