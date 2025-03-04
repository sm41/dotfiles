
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
    self.loaded_yaml  = abc.load_yaml(__env_state, "python", "vvv.yaml")


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



def out_get_dow(deploy_yaml:list, find_value):

  dow_list:list = []

  for pltfrm, prpty in deploy_yaml.items():
    for genre, param in prpty.items():
      if genre == 'config':
        continue
      for cntnts, series in param.items():
        if cntnts != "contents":
          continue
        for title, spec in series.items():
          for hoge in spec['dow']:
            if hoge == find_value:
              hypr = {
                **spec,
                'header': param['header'],
                }
              dow_list.append(hypr)
  return dow_list


def www(deploy_yaml:list, keyword:str):

  hogefuga = []

  for pltfrm, prpty in deploy_yaml.items():
    for genre, param in prpty.items():
      if param == 'config':
        continue
      for cntnts, series in param.items():
        if cntnts != "contents":
          continue
        for title, spec in series.items():
          if title == keyword:
            hypr = {
              **spec,
              'header': param['header'],
              }
            hogefuga.append(hypr)
  return hogefuga



def www2(deploy_yaml, keyword):

  hogefuga = []

  for genre, prpty in deploy_yaml['tver'].items():
    if genre == 'config':
      continue
    for aaa, bbb in deploy_yaml['tver'][genre]['contents'].items():
      if aaa != keyword:
        continue
      else:
        hypr = {
          **bbb,
          "header": prpty['header']
          }
        hogefuga.append(hypr)
  return hogefuga


