from os import remove
from re import compile, IGNORECASE
from subprocess import run
from mytool import utils
from sys import exit
import auth, parse, variable, download


def majisuka(series_list, time:variable.time, var_parts:variable.local_path):
  for series_dict in series_list:
    station_id  = series_dict['station_id']
    search_term = series_dict['title']
    url         = series_dict['url']

    soup      = utils.Gen_Obj.data2soup(url, "xml")
    find_list = soup.find_all("title", text=compile(search_term, flags=IGNORECASE))
    pgm_list:list  = variable.search_program(station_id, find_list, time.today_now, time.days_ago, var_parts.tmp_dir, var_parts.storage_path)

  return pgm_list


def siingle_match(pgm_list, optional_arument:parse.parse_arg):

  if   len(pgm_list) == 0:
    print("⚠️ Program is Not Found !!")
    exit()

  elif len(pgm_list) == 1:
    if not optional_arument.dl_flag:
      print(pgm_list)
      print("✅ You can download it by adding '-dl' flag")
      exit()

  elif len(pgm_list) >= 2:
    if not optional_arument.fftt:
      for iii in pgm_list:
        srx = {
          'station_id': iii['station_id'],
          'day':        iii['date'],
          'time':       f"{iii['ft'][8:10]}:{iii['ft'][10:12]}-{iii['to'][8:10]}:{iii['to'][10:12]}",
          'title':      iii['title']
        }
        print(srx)
      print(f"📢 Result {len(pgm_list)} Programs")
      exit()

    elif len(optional_arument.fftt) != 14:
      exit("There is an error in the '-ft' option")

    elif len(optional_arument.fftt) == 14:
      hogefuga_list = []
      for rrr in pgm_list:
        if rrr['ft'] == optional_arument.fftt:
          hogefuga_list.append(rrr)
          break
      pgm_list = hogefuga_list
      print(pgm_list)
      print("✅ You can download it by adding '-dl' flag")


def ddwwnn(pgm_list, fst:download.fastforward, ooo:auth.oth):
  for dl_dict in pgm_list:
    fst.dl(ooo.xrat, dl_dict)
    fst.enc(dl_dict)
    result_1 = run(fst.ffmpeg_dl)
    result_2 = run(fst.ffmpeg_enc)
    # print(fst.ffmpeg_dl)

    if result_1.returncode == 0:
      remove(f"{dl_dict['tmp']}/{dl_dict['title']}_{dl_dict['date']}.m4a")

    utils.ntfy(result_2, f"{dl_dict['title']}_{dl_dict['date']}.mp3")


