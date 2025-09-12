from os import remove
from re import compile, IGNORECASE
from subprocess import run
from mytool import utils
from sys import exit
import parse, download
from pathlib import Path


def arg2soup(series_list):
  soup_dish = []
  for buiyon in series_list:
    url         = buiyon['url']
    search_term = buiyon['title']

    soup          = utils.Gen_Obj.data2soup(url, "xml")
    find_all_list = soup.find_all("title", text=compile(search_term, flags=IGNORECASE))
    soup_dish.append(find_all_list)
  return soup_dish


def single_match(pgm_list, optional_arument:parse.parse_arg):

  if   len(pgm_list) == 0:
    print("⚠️ Program is Not Found !!")
    exit()

  elif len(pgm_list) == 1:
    if not optional_arument.dl_flag:
      print(pgm_list)
      print("✅ You can download it by adding '-dl' flag")
      exit()
    else:
      return pgm_list

  elif len(pgm_list) >= 2:
    if not optional_arument.fftt:
      for pgm_status in pgm_list:
        srx = {
          'ft' :        pgm_status['ft'],
          'station_id': pgm_status['station_id'],
          'day':        pgm_status['date'],
          'time':       f"{pgm_status['ft'][8:10]}:{pgm_status['ft'][10:12]}-{pgm_status['to'][8:10]}:{pgm_status['to'][10:12]}",
          'title':      pgm_status['title']
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
      single_match(pgm_list, optional_arument)
      return pgm_list


def ddwwnn(pgm_list, fst:download.fastforward, xrat):
  for dl_dict in pgm_list:
    fst.dl(xrat, dl_dict)
    fst.select_audio_format(fst.ffmpeg_dl[-1], dl_dict, "aac")
    fst.select_container_format(fst.ffmpeg_af[-1], dl_dict, "mkv")
    fst.enc(dl_dict)

    result_dl = run(fst.ffmpeg_dl)
    result_af = run(fst.ffmpeg_af)
    result_cf = run(fst.ffmpeg_cf)

    if result_dl.returncode == 0:
      remove(Path(fst.ffmpeg_dl[-1]))
    if result_af.returncode == 0:
      remove(Path(fst.ffmpeg_af[-1]))

    utils.ntfy(result_cf, Path(fst.ffmpeg_cf[-1]).name)


