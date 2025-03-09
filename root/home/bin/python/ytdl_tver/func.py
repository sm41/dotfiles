
from selenium import webdriver
from bs4  import BeautifulSoup
from time import sleep
from re   import compile
from os  import getenv
from sys import argv
from mytool import abc



class gen_var:
  def __init__(self):
    self.arg = argv[1]
    __env_dl    = getenv("CLIENT_NETWORK_STORAGE_misc")
    __env_state = getenv("XDG_STATE_HOME")
    self.storage_path = abc.anlys_path(__env_dl, "@tver")
    # self.loaded_yaml  = abc.load_yaml(__env_state, "python", "vvv.yaml")
    self.loaded_yaml  = abc.load_yaml(__env_state, "python", "test.yaml")


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



def find_key_dict(data, target_key):
  result_list = []

  if isinstance(data, dict):
    for key, value in data.items():
      if key.startswith("_"):
        continue
      if key == target_key:
        result_list.append(value)
        return result_list
      result = find_key_dict(value, target_key)
      if result is not None:
        return result


def find_key_value_list(data, target_key):
    result_list = []

    for key1, value1 in data.items():
        if key1.startswith("_"):
            continue

        if "dow" not in value1:
            result_list.extend(find_key_value_list(value1, target_key))
        else:
            for dow_item in value1['dow']:
                if dow_item == target_key:
                    result_list.append(value1)
                    break  # 同じtitleのデータが複数回追加されないようにする

    return result_list
