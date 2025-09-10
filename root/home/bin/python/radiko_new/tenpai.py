from os import remove
from re import compile, IGNORECASE
from subprocess import run
from mytool import utils
from sys import exit
import parse, download


def arg2soup(series_list):
  soup_dish = []
  for buiyon in series_list:
    url         = buiyon['url']
    search_term = buiyon['title']
    # station_id  = buiyon['station_id']

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
      for iii in pgm_list:
        srx = {
          'ft' :        iii['ft'],
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
      single_match(pgm_list, optional_arument)
      return pgm_list


def ddwwnn(pgm_list, fst:download.fastforward, xrat):
  for dl_dict in pgm_list:
    fst.dl(xrat, dl_dict)
    fst.enc(dl_dict)
    result_1 = run(fst.ffmpeg_dl)
    result_2 = run(fst.ffmpeg_enc)

    if result_1.returncode == 0:
        remove(f"{dl_dict['tmp']}/{dl_dict['title']}_{dl_dict['date']}.m4a")

    utils.ntfy(result_2, f"{dl_dict['title']}_{dl_dict['date']}.mp3")


