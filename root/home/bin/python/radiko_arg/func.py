#!/usr/bin/python3

import urllib.request
from datetime import datetime, timedelta
from argparse import ArgumentParser
from plyer  import notification
from bs4    import BeautifulSoup
from re  import compile, IGNORECASE
from sys import exit
# from locale   import setlocale, LC_TIME


def check_ststus_code(subject):
  if subject.getcode() != 200:
    print(f"Ststus Code is {subject.getcode()} !!")
    exit()


def analyse_argment(s_dict:dict):
  parser = ArgumentParser()

  parser.add_argument('-s',  help='station_id', required=True,  type=str.upper, choices=s_dict.keys())
  parser.add_argument('-t',  help='title',      required=True,  type=str)
  parser.add_argument('-ft', help='ft',         required=False, type=str)
  parser.add_argument('-dl', help='download',   required=False, action='store_true')

  optional_args = parser.parse_args()
  return optional_args


def now_time(day_int:int):
  get_now = datetime.now()
  get_past = get_now - timedelta( days = day_int )

  today_now:str = get_now.strftime('%Y%m%d%H%M')+'00'
  days_ago:str = get_past.strftime('%Y%m%d%H%M')+'00'

  return today_now, days_ago


def search_program(search_term, url, today_now, days_ago, fftt):
  get_xml = urllib.request.urlopen(url)
  check_ststus_code(get_xml)
  soup = BeautifulSoup(get_xml, "xml")
  keyword_list = soup.find_all("title", text=compile(search_term, flags=IGNORECASE))

  program_list = []

  for keyword in keyword_list:
    prog_detail = keyword.parent
    if   days_ago >  prog_detail.attrs['to'] >  today_now:
      continue
    elif days_ago <= prog_detail.attrs['to'] <= today_now:
      ddd = {
        "ft":       prog_detail.attrs['ft'],
        "to":       prog_detail.attrs['to'],
        "time":     f"{prog_detail.attrs['ft'][0:4]}-{prog_detail.attrs['ft'][4:6]}-{prog_detail.attrs['ft'][6:8]}-{prog_detail.attrs['ft'][8:12]}",
        "title":    prog_detail.title.string,
        "img":      prog_detail.img.string,
      }
      program_list.append(ddd)


  if fftt is None:
    return program_list

  elif len(fftt) != 14:
    print("There is an error in the '-ft' option")
    exit()

  elif len(fftt) == 14:
    hogefuga_list = []
    for rrr in program_list:
      if rrr['ft'] == fftt:
        hogefuga_list.append(rrr)
    return hogefuga_list


def branch(program_list, download_flag):

  if   len(program_list) > 1:
    if download_flag == True:
      notification.notify(title = "⚠️ failed",  message = "upper")
    elif download_flag == False:
      for vvv in program_list:
        print(vvv)
      print(f"Result {len(program_list)} Programs")
    exit()

  elif len(program_list) == 1:
    if download_flag == True:
      return program_list[0]['ft'], program_list[0]['to'], f"{program_list[0]['title']}_{program_list[0]['time']}", program_list[0]['img']
    elif download_flag == False:
      print(program_list)
      print("You can download it by adding '-dl' flag")
    exit()

  elif len(program_list) == 0:
    if download_flag == True:
      notification.notify(title = "⚠️ failed",  message = "upper")
    elif download_flag == False:
      print("Program is Not Found !!")
    exit()

