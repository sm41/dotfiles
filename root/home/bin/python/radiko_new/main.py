# from subprocess import run
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
  ooo       = auth.oth()

  if argv[1].startswith("-"):
    optional_arument = parse.parse_arg()
    series_list = [
      {
        'station_id' : optional_arument.station_id,
        "title"      : optional_arument.search_term,
        "url"        : f"https://radiko.jp/v3/program/station/weekly/{optional_arument.station_id}.xml"
      }
    ]

    pgm_list:list = tenpai.majisuka(series_list, time, var_parts)
    tenpai.siingle_match(pgm_list, optional_arument)


  if not argv[1].startswith("-"):
    yaml_argument   = parse.parse_file()
    cd        = utils.Ctrl_Date(1)

    if   argv[1] == "dow":
      yaml_argument.today_list(var_parts.loaded_yaml, cd.y_dow)
    elif argv[1] != "dow":
      yaml_argument.series_name(var_parts.loaded_yaml, argv[1])

    options_list = parse.yaml2arg(yaml_argument.reserve_list)

    series_list = []
    for series in options_list:
      station_id = series['-s'].upper()
      hoge = {
        'station_id': station_id,
        'title'     : series['-t'],
        'url'       : f"https://radiko.jp/v3/program/station/weekly/{station_id}.xml"
      }
      series_list.append(hoge)

    pgm_list:list = tenpai.majisuka(series_list, time, var_parts)


  tenpai.ddwwnn(pgm_list, fst, ooo)