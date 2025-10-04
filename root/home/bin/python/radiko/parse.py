from argparse import ArgumentParser
from types import SimpleNamespace

class Parse_Arg:
  s_dict = {
    "TBS":     "TBSラジオ",
    "QRR":     "文化放送",
    "LFR":     "ニッポン放送",
    "RN1":     "ラジオNIKKEI第1",
    "RN2":     "ラジオNIKKEI第2",
    "INT":     "interfm",
    "FMT":     "tokyo fm",
    "FMJ":     "j-wave",
    "IBS":     "LuckyFM 茨城放送",
    "JORF":    "ラジオ日本",
    "BAYFM78": "bayfm",
    "NACK5":   "nack5",
    "YFM":     "fm yokohama",
    "JOAK":    "NHKラジオ第1（東京）",
    "JOAK-FM": "NHK-FM（東京）",
  }

  def __init__(self):
    parser = ArgumentParser()
    parser.add_argument('-s',   help='station_id',  required=True,   type=str.upper, choices = self.s_dict.keys())
    parser.add_argument('-t',   help='title',       required=True,   type=str)
    parser.add_argument('-ft',  help='ft',          required=False,  type=str)
    parser.add_argument('-dl',  help='download',    required=False,  action='store_true')

    opt_args         = parser.parse_args()
    self.station_id  = opt_args.s.upper()
    self.search_term = opt_args.t
    self.fftt        = opt_args.ft
    self.dl_flag     = opt_args.dl


class Parse_File:
  reserve_list = []

  def today_list(self, yaml_file:dict, y_dow_str):
    for key, value in yaml_file.items():
      for pln in value['dow']:
        if pln == y_dow_str:
          self.reserve_list.append({**value})

  def series_name(self, yaml_file:dict, args):
    for ttl, cnfg in yaml_file.items():
      if ttl == args:
        self.reserve_list.append({**cnfg})


class Convert_Dict:
  def yaml2dict(self, yaml_list:list):
    self.options_list = []
    key_to_option = {
      'station': '-s',
      'title':   '-t',
    }

    for yaml_value in yaml_list:
      today_series = {}
      for key, value in key_to_option.items():
        option = yaml_value.get(key)
        if option:
          today_series[value] = option
      self.options_list.extend([today_series])

  def arg2dict(self, optional_arument:Parse_Arg):
    self.options_list = [
      {
        '-s': optional_arument.station_id,
        '-t': optional_arument.search_term
      }
    ]

  def minimum_dict(self, optional_arument:Parse_Arg):
    self.argument_dict = {
      'station_id' : optional_arument.station_id,
      "title"      : optional_arument.search_term,
      "url"        : f"https://radiko.jp/v3/program/station/weekly/{optional_arument.station_id}.xml"
    }

  def fix_dict(self, options_list):
    self.series_list  = []
    for series in options_list:
      alt_optional_arg = SimpleNamespace(station_id=series['-s'].upper(), search_term=series['-t'])
      self.minimum_dict(alt_optional_arg)
      self.series_list.append(self.argument_dict)
