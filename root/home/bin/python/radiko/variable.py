from sys import exit
from mytool import ctrl_path as cp, ctrl_date as cd

class Set_Variable:
  def __init__(self):
    lp = cp.Storage("@radiko")
    ld = cp.Local_Data("radiko.yaml")

    self.tmp_dir      = lp.tmp_dir
    self.storage_dir  = lp.storage_dir
    self.loaded_yaml  = cp.Yaml_Tool.yaml_safe_load(ld.local_data_path)


class Time:
  def __init__(self, day_int):
    aaa = cd.Date().yesterday(day_int)

    self.today_now      = aaa.format(aaa.today_now, '%Y%m%d%H%M'+'00').format_time
    self.n_days_ago     = aaa.format(aaa.n_days_ago_now, '%Y%m%d%H%M'+'00').format_time
    self.n_days_ago_dow = aaa.n_days_ago_dow


  def convert_time_hhmm_no_colon(time_str):
    hour   = int(time_str[:2])
    minute = int(time_str[2:])

    if  hour >= 24:
        hour -= 24

    return f"{hour:02}{minute:02}"

