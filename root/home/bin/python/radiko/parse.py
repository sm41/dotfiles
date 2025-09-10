from argparse import ArgumentParser


class parse_arg:
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
    __parser = ArgumentParser()
    __parser.add_argument('-s',   help='station_id',  required=True,   type=str.upper, choices = self.s_dict.keys())
    __parser.add_argument('-t',   help='title',       required=True,   type=str)
    __parser.add_argument('-ft',  help='ft',          required=False,  type=str)
    __parser.add_argument('-dl',  help='download',    required=False,  action='store_true')

    __opt_args       = __parser.parse_args()
    self.station_id  = __opt_args.s.upper()
    self.search_term = __opt_args.t
    self.fftt        = __opt_args.ft
    self.dl_flag     = __opt_args.dl


class parse_file:
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


class convert_dict:
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

  def arg2dict(self, station_id, search_term):
    self.options_list = [
      {
        '-s': station_id,
        '-t': search_term
      }
    ]

  def minimum_dict(self, station_id, search_term):
    self.argument_dict = {
      'station_id' : station_id,
      "title"      : search_term,
      "url"        : f"https://radiko.jp/v3/program/station/weekly/{station_id}.xml"
    }
