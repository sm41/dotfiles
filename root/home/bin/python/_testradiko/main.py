from os import remove
from re import compile, IGNORECASE
from subprocess import run
import func, auth, parse, variable, download
from mytool import utils
from sys import argv, exit
import __main__


#JP+都道府県コード ex) 北海道 => JP1    沖縄 => JP47
#国土交通省 https://nlftp.mlit.go.jp/ksj/gml/codelist/PrefCd.html
#Area ID: JP8   https://radiko.jp/v3/station/list/JP8.xml
#
#https://radiko.jp/v3/program/station/date/20301231/TBS.xml
#https://radiko.jp/v3/program/station/weekly/TBS.xml


def majisuka(series_list, vbn:func.icpo, time:variable.time, var_parts:variable.local_path):
  for series_dict in series_list:
    station_id  = series_dict['station_id']
    search_term = series_dict['title']
    url         = series_dict['url']

    soup      = utils.Gen_Obj.data2soup(url, "xml")
    find_list = soup.find_all("title", text=compile(search_term, flags=IGNORECASE))
    vbn.search_program(station_id, find_list, time.today_now, time.days_ago, var_parts.tmp_dir, var_parts.storage_path)


def siingle_match(vbn:func.icpo, setarg:func.set_arg):

  if len(vbn.program_list) != 1:

      if not setarg.fftt:
          for iii in vbn.program_list:
            srx = {
              'station_id': iii['station_id'],
              'day':        iii['date'],
              'time':       f"{iii['ft'][8:10]}:{iii['ft'][10:12]}-{iii['to'][8:10]}:{iii['to'][10:12]}",
              'title':      iii['title']
            }
            print(srx)
          print(f"📢 Result {len(vbn.program_list)} Programs")
          exit()

      elif len(setarg.fftt) != 14:
          exit("There is an error in the '-ft' option")

      elif len(setarg.fftt) == 14:
          hogefuga_list = []
          for rrr in vbn.program_list:
              if rrr['ft'] == setarg.fftt:
                  hogefuga_list.append(rrr)
                  break
          vbn.program_list = hogefuga_list
          print(vbn.program_list)
          print("✅ You can download it by adding '-dl' flag")

  elif len(vbn.program_list) == 1:

      if not setarg.dl_flag:
          print(vbn.program_list)
          print("✅ You can download it by adding '-dl' flag")
          exit()


def ddwwnn(vbn:func.icpo, fst:download.fastforward, ooo:auth.oth):
  for dl_dict in vbn.program_list:
    fst.dl(ooo.xrat, dl_dict)
    fst.enc(dl_dict)
    result_1 = run(fst.ffmpeg_dl)
    result_2 = run(fst.ffmpeg_enc)
    # print(fst.ffmpeg_dl)

    if result_1.returncode == 0:
        remove(f"{dl_dict['tmp']}/{dl_dict['title']}_{dl_dict['date']}.m4a")

    utils.ntfy(result_2, f"{dl_dict['title']}_{dl_dict['date']}.mp3")




def main():
  time      = variable.time(7)
  vbn       = func.icpo()
  var_parts = variable.local_path()
  fst       = download.fastforward()
  ooo       = auth.oth()

  if argv[1].startswith("-"):
    setarg    = func.set_arg()
    series_list = [
      {
        'station_id' : setarg.station_id,
        "title"      : setarg.search_term,
        "url"        : f"https://radiko.jp/v3/program/station/weekly/{setarg.station_id}.xml"
      }
    ]

    majisuka(series_list, vbn, time, var_parts)
    siingle_match(vbn, setarg)


  if not argv[1].startswith("-"):
    argment   = parse.parse_file()
    cd        = utils.Ctrl_Date(1)

    if   argv[1] == "dow":
      argment.today_list(var_parts.loaded_yaml, cd.y_dow)
    elif argv[1] != "dow":
      argment.series_name(var_parts.loaded_yaml, argv[1])

    options_list = parse.yaml2arg(argment.reserve_list)

    series_list = []
    for series in options_list:
      station_id = series['-s'].upper()
      hoge = {
        'station_id': station_id,
        'title'     : series['-t'],
        'url'       : f"https://radiko.jp/v3/program/station/weekly/{station_id}.xml"
      }
      series_list.append(hoge)

    majisuka(series_list, vbn, time, var_parts)


  ddwwnn(vbn, fst, ooo)