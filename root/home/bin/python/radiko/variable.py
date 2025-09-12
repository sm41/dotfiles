from os  import getenv
from sys import exit
from mytool import utils
from datetime import datetime, timedelta


class local_path:
  tmp_dir = "/tmp"

  def __init__(self):
    __env_dir         = getenv("CLIENT_NETWORK_STORAGE_misc")
    __state_file_dir  = getenv("XDG_CONFIG_HOME")
    self.loaded_yaml  = utils.Gen_Obj.safe_load_file(__state_file_dir, "script_python", "radiko.yaml")
    self.storage_path = utils.Ctrl_Path.anlys_path(__env_dir, "@radiko")


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



def search_program(station_id, find_lists, today_now, days_ago, tmp, storage):
  program_list = []

  for find_list in find_lists:
    for keyword in find_list:
      prog_detail = keyword.parent
      if   days_ago >  prog_detail.attrs['to'] >  today_now:
        continue
      elif days_ago <= prog_detail.attrs['to'] <= today_now:
        ddd = {
          "station_id":  station_id,
          "ft":          prog_detail.attrs['ft'],
          "to":          prog_detail.attrs['to'],
          "date":     f"{prog_detail.attrs['ft'][0:4]}-{prog_detail.attrs['ft'][4:6]}-{prog_detail.attrs['ft'][6:8]}",
          "start":    f"{prog_detail.attrs['ftl']}",
          "end":      f"{prog_detail.attrs['tol']}",
          "img":      prog_detail.img.string,
          'tmp':      tmp,
          'storage':  storage,
          "title":    utils.Ctrl_File.zen2han(prog_detail.title.string),
        }
        program_list.append(ddd)

  return program_list
