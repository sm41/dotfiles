
from dataclasses import dataclass, field, InitVar
from os  import getenv
from mytool import abc
import __main__


@dataclass
class gen_var:
  tmp_dir = "/tmp"

  def __post_init__(self):
    # __env_dir         = getenv("CLIENT_NETWORK_STORAGE_misc")
    __state_file_dir  = getenv("XDG_CONFIG_HOME")
    self.loaded_yaml  = abc.gen_obj.load_file(__state_file_dir, "script_python", "radiko.yaml")
    # self.storage_path = abc.ctrl_path.anlys_path(__env_dir, "@radiko")
    # self.url          = f"https://radiko.jp/v3/program/station/weekly/{station_id}.xml"


@dataclass
class check_arg:
  reserve_list: list = field(default_factory=list)
  __platform: str = 'radiko'

  def today_list(self, y_data, y_dow_str):
    for key, value in y_data[self.__platform].items():
      for pln in value['dow']:
        if pln == y_dow_str:
          self.reserve_list.append({**value})

  def series_name(self, y_data, args):
    for ttl, cnfg in y_data[self.__platform].items():
      if ttl == args:
        self.reserve_list.append({**cnfg})


def ggg(data:dict):
  key_to_option = {
    'station': '-s',
    'title':   '-t',
  }

  args = []

  for key, value in key_to_option.items():
    option = data.get(key)
    if option:
      args.extend([value, option])

  return args


def convert_d2l(today_list:list):

  ttg = []

  for www in today_list:
    cvb = ggg(www)
    cvb.insert(0, __main__.__file__)
    ttg.append(cvb)
  return ttg
