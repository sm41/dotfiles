import yaml
import inspect
from pathlib import Path
from mytool import ctrl_path as cp


def get_yaml_path():
  lp = cp.Local_Data("scraping.yaml")

  state_file_PATH = lp.local_data_path
  return state_file_PATH


def get_function_names(instance):
  function_names = [
    name for name, obj in inspect.getmembers(instance, inspect.ismethod)
    if name != '__init__'
  ]
  return function_names


def generate_method(instance_name, method_name):
  unite_method = getattr(instance_name, method_name)
  unite_method()


def isexist_dict(method_name, state_file: Path):
  if not state_file.exists():
    with open(state_file, 'w', encoding='utf-8') as f:
      return None
  else:
    with open(state_file, 'r', encoding='utf-8') as f:
      for dict_of_siteinfo in yaml.safe_load_all(f):
        for key_of_sitename in dict_of_siteinfo.keys():
          if key_of_sitename == method_name:
            return dict_of_siteinfo


def rewrite_dict(state_file, data):
  with open(state_file, 'w', encoding='utf-8') as f:
    yaml.safe_dump_all(data, f, allow_unicode=True, sort_keys=False)
