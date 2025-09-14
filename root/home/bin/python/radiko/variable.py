from os  import getenv
from sys import exit
from mytool import ctrl_path, gen_obj
from datetime import datetime, timedelta


class local_path:
  tmp_dir = "/tmp"

  def __init__(self):
    __env_dir         = getenv("CLIENT_NETWORK_STORAGE_misc")
    __state_file_dir  = getenv("XDG_CONFIG_HOME")
    self.loaded_yaml  = gen_obj.gen_obj.safe_load_file(__state_file_dir, "script_python", "radiko.yaml")
    self.storage_path = ctrl_path.ctrl_path.anlys_path(__env_dir, "@radiko")


class time:
  def __init__(self, day_int):
    __get_now      = datetime.now()
    __get_past     = __get_now - timedelta(day_int)
    self.today_now = __get_now.strftime('%Y%m%d%H%M')+'00'
    self.days_ago  = __get_past.strftime('%Y%m%d%H%M')+'00'

  def convert_time_hhmm_no_colon(time_str):
    hour   = int(time_str[:2])
    minute = int(time_str[2:])

    if  hour >= 24:
        hour -= 24

    return f"{hour:02}{minute:02}"

