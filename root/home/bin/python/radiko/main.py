from sys import argv, exit
import parse, variable, tenpai


#JP+都道府県コード ex) 北海道 => JP1    沖縄 => JP47
#国土交通省 https://nlftp.mlit.go.jp/ksj/gml/codelist/PrefCd.html
#Area ID: JP8   https://radiko.jp/v3/station/list/JP8.xml
#
#https://radiko.jp/v3/program/station/date/20301231/TBS.xml
#https://radiko.jp/v3/program/station/weekly/TBS.xml


def main():
  var_parts = variable.hoge()
  time      = variable.time(7)
  cnv_dict  = parse.convert_dict()

  if argv[1].startswith("-"):
    optional_arument = parse.parse_arg()

    cnv_dict.arg2dict(optional_arument)
    cnv_dict.minimum_dict(optional_arument)
    series_list = [ cnv_dict.argument_dict ]

  if not argv[1].startswith("-"):
    yaml_argument   = parse.parse_file()

    if   argv[1] == "dow":
      yaml_argument.today_list(var_parts.loaded_yaml, time.n_days_ago_dow)
    elif argv[1] != "dow":
      yaml_argument.series_name(var_parts.loaded_yaml, argv[1])

    cnv_dict.yaml2dict(yaml_argument.reserve_list)
    cnv_dict.fix_dict(cnv_dict.options_list)
    series_list = cnv_dict.series_list


  soup_dish: list = tenpai.arg2soup(series_list)
  pgm_list:  list = tenpai.search_program(cnv_dict.argument_dict['station_id'], soup_dish, time, var_parts)

  try:
    optional_arument
  except NameError:
    pass
  else:
    pgm_list = tenpai.single_match(pgm_list, optional_arument)

  tenpai.ddwwnn(pgm_list)