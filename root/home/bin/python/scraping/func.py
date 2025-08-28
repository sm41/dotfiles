from selenium import webdriver
from bs4  import BeautifulSoup
from time import sleep
import yaml
from pathlib import Path
import inspect


def get_yaml_path(filename="state.yaml"):
  script_dir = Path(__file__).resolve().parent
  state_file = script_dir / filename
  return state_file


def isexist_dict(method_name, state_file):
  if not state_file.exists():
    with open(state_file, 'w', encoding='utf-8') as f:
      return None
  else:
    with open(state_file, 'r', encoding='utf-8') as f:
      for dict_of_siteinfo in yaml.safe_load_all(f):
        for key_of_sitename in dict_of_siteinfo.keys():
          if key_of_sitename == method_name:
            return dict_of_siteinfo


def get_function_names(instance):
  function_names = [
    name for name, obj in inspect.getmembers(instance, inspect.ismethod)
    if name != '__init__'
  ]
  return function_names


def generate_method(instance_name, method_name):
  unite_method = getattr(instance_name, method_name)
  unite_method()


def selenium(url):
  __fx_options = webdriver.FirefoxOptions()
  __fx_options.add_argument("--headless")
  __driver = webdriver.Firefox(options = __fx_options)
  __driver.get(url)
  sleep(5)
  __get_html = __driver.page_source
  soup = BeautifulSoup(__get_html, "html.parser")
  __driver.quit()
  return soup


def rewrite_dict(state_file, data):
  with open(state_file, 'w', encoding='utf-8') as f:
    yaml.safe_dump_all(data, f, allow_unicode=True, sort_keys=False)
