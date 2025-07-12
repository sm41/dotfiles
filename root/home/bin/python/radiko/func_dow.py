
from dataclasses import dataclass, field, InitVar
from os  import getenv
from mytool import abc


@dataclass
class gen_var:
  station_id: InitVar[str]
  tmp_dir = "/tmp"

  def __post_init__(self, station_id):
    # __env_dir         = getenv("CLIENT_NETWORK_STORAGE_misc")
    __state_file_dir  = getenv("XDG_STATE_HOME")
    self.loaded_yaml  = abc.Gen_Obj.load_file(__state_file_dir, "python", "radiko.yaml")
    # self.storage_path = abc.Ctrl_Path.anlys_path(__env_dir, "@radiko")
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




def ggg(data):
  key_to_option = {
    'station': '-s',
    'title':   '-t',
  }

  args = []

  for key, value in data.items():
    option = key_to_option.get(key)
    if option:
      args.extend([option, value])

  return args


