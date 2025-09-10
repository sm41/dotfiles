from mytool import utils
from sys import argv, exit
import auth, parse, variable, download, tenpai


#JP+都道府県コード ex) 北海道 => JP1    沖縄 => JP47
#国土交通省 https://nlftp.mlit.go.jp/ksj/gml/codelist/PrefCd.html
#Area ID: JP8   https://radiko.jp/v3/station/list/JP8.xml
#
#https://radiko.jp/v3/program/station/date/20301231/TBS.xml
#https://radiko.jp/v3/program/station/weekly/TBS.xml


def main():
  var_parts = variable.local_path()
  time      = variable.time(7)
  fst       = download.fastforward()
  cnv_dict  = parse.convert_dict()
  xrat      = auth.iinntt()

  if argv[1].startswith("-"):
    optional_arument = parse.parse_arg()

    cnv_dict.arg2dict(optional_arument.station_id, optional_arument.search_term)
    cnv_dict.minimum_dict(optional_arument.station_id, optional_arument.search_term)
    series_list = [ cnv_dict.argument_dict ]


  if not argv[1].startswith("-"):
    yaml_argument   = parse.parse_file()
    cd              = utils.Ctrl_Date(1)

    if   argv[1] == "dow":
      yaml_argument.today_list(var_parts.loaded_yaml, cd.y_dow)
    elif argv[1] != "dow":
      yaml_argument.series_name(var_parts.loaded_yaml, argv[1])

    cnv_dict.yaml2dict(yaml_argument.reserve_list)

    series_list  = []
    for series in cnv_dict.options_list:
      station_id = series['-s'].upper()
      cnv_dict.minimum_dict(station_id, series['-t'])
      series_list.append(cnv_dict.argument_dict)


  soup_dish: list = tenpai.arg2soup(series_list)
  pgm_list:  list = variable.search_program(cnv_dict.argument_dict['station_id'], soup_dish, time.today_now, time.days_ago, var_parts.tmp_dir, var_parts.storage_path)

  try:
    optional_arument
  except NameError:
    pass
  else:
    pgm_list = tenpai.single_match(pgm_list, optional_arument)
    # print(pgm_list)


  print(pgm_list)
  exit()

  tenpai.ddwwnn(pgm_list, fst, xrat)