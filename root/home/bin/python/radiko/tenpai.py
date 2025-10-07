from os import remove
from re import compile, IGNORECASE
from sys import exit
from pathlib import Path
from subprocess import run
from mytool import ctrl_string as cs, scraping, notify
import auth, parse, download, variable


def arg2soup(series_list):
  soup_dish = []

  for buiyon in series_list:
    url         = buiyon['url']
    search_term = buiyon['title']

    qqq  = scraping.Scrp()
    qqq.get_response(url).simple("xml")

    find_all_list = qqq.soup.find_all("title", text=compile(search_term, flags=IGNORECASE))
    soup_dish.append(find_all_list)
  return soup_dish


def search_program(station_id, find_lists, time:variable.Time, var_parts:variable.Set_Variable):
  program_list = []

  for find_list in find_lists:
    for keyword in find_list:
      prog_detail = keyword.parent
      if   time.n_days_ago >  prog_detail.attrs['to'] >  time.today_now:
        continue
      elif time.n_days_ago <= prog_detail.attrs['to'] <= time.today_now:
        ddd = {
          "station_id":  station_id,
          "ft":          prog_detail.attrs['ft'],
          "to":          prog_detail.attrs['to'],
          "date":     f"{prog_detail.attrs['ft'][0:4]}-{prog_detail.attrs['ft'][4:6]}-{prog_detail.attrs['ft'][6:8]}",
          "start":       prog_detail.attrs['ftl'],
          "end":         prog_detail.attrs['tol'],
          "img":         prog_detail.img.string,
          'tmp':         var_parts.tmp_dir,
          'storage':     var_parts.storage_dir,
          "title":       cs.File_Tool.zen2han(prog_detail.title.string),
        }
        program_list.append(ddd)

  return program_list


def single_match(pgm_list, optional_arument:parse.Parse_Arg):

  if   len(pgm_list) == 0:
    print("⚠️ Program is Not Found !!")
    exit()

  elif len(pgm_list) == 1:
    if not optional_arument.dl_flag:
      cs.line_up_dict(pgm_list[0])
      print("✅ You can download it by adding '-dl' flag")
      exit()
    else:
      return pgm_list

  elif len(pgm_list) >= 2:
    if not optional_arument.fftt:
      print('+---'*32)

      day_one = ''
      day_two = ''

      for pgm_status in pgm_list:
        srx = {
          'ft' :        pgm_status['ft'],
          'station_id': pgm_status['station_id'],
          'day':        pgm_status['date'],
          'time':    f"{pgm_status['start'][0:2]}:{pgm_status['start'][2:4]}-{pgm_status['end'][0:2]}:{pgm_status['end'][2:4]}",
          'title':      pgm_status['title']
        }
        day_one = srx['day']

        if day_one != day_two:
          day_two = day_one
          print('■■■■'*36)


        print(srx)
      print('+---'*32)
      print(f"📢 Result {len(pgm_list)} Programs")
      exit()

    elif len(optional_arument.fftt) != 14:
      print("⚠️ Please specify the exact 'from time' with '-ft' option (e.g. YYYYMMDDhhmmss(20xx1231235959))")
      exit()

    elif len(optional_arument.fftt) == 14:
      hogefuga_list = []
      for rrr in pgm_list:
        if rrr['ft'] == optional_arument.fftt:
          hogefuga_list.append(rrr)
          break
      pgm_list = hogefuga_list
      single_match(pgm_list, optional_arument)
      return pgm_list


def ddwwnn(pgm_list):
  xrat = auth.iinntt()

  for dl_dict in pgm_list:
    fst = download.Fast_Forward(dl_dict)

    fst.download_by_ffmpeg(xrat)
    fst.select_audio_format(fst.ffmpeg_dl[-1], "aac")
    fst.select_container_format(fst.ffmpeg_af[-1], "mp4")

    result_dl = run(fst.ffmpeg_dl)
    result_af = run(fst.ffmpeg_af)
    result_cf = run(fst.ffmpeg_cf)

    if result_dl.returncode == 0:
      remove(Path(fst.ffmpeg_dl[-1]))
    if result_af.returncode == 0:
      remove(Path(fst.ffmpeg_af[-1]))

    notify.ntfy(result_cf, Path(fst.ffmpeg_cf[-1]).name)

