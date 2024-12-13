
from plyer    import notification
import func_parse, func_scrape, func_ytdlp

import subprocess
import datetime
import locale
import sys
import os
import json


def json_kit(j_path, j_d_set, target_key, find_value):

  dict_tuple = []

  for j_file in j_d_set:
    filename = os.path.join(j_path, 'python', j_file)
    with open(filename, mode='r') as f:
      j_data = json.load(f)

    for var_dict in j_data:
      if not var_dict[target_key] == find_value:
        continue
      dict_tuple.append(var_dict)

  return dict_tuple


def dow_yesterday(day_int:int):
  locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')

  d_today      = datetime.date.today()
  d_yesterday  = d_today - datetime.timedelta( days = day_int )
  y_dow_symbol = d_yesterday.strftime('%a')

  return y_dow_symbol


def check_arg():
  if(len(sys.argv) <= 1):
    print('You need args!')
    sys.exit()


def ntfy(result, upper, lower):
  if result.returncode == 0:
    notification.notify(
      title = "✅ Success",
      message = f"{upper}\n{lower}"
    )
  else:
    notification.notify(
      title = "⚠️ failed",
      message = f"{upper}\n{lower}"
    )


def main(vvvv, jp):

  for input_dict in vvvv:

    set_platform = input_dict["platform"]
    set_scraper  = input_dict["scraper"]

    if "anchor" in input_dict:
      set_anchor = input_dict["anchor"]
    else:
      set_anchor = None

    material = func_scrape.hhh(set_scraper, input_dict["url"])
    series, episode, link = func_parse.ppp(set_platform, material, set_anchor)

    # print(series, episode, link)
    # continue
    # sys.exit()

    method = func_ytdlp.rrr(link, set_platform)
    result = subprocess.run(method)

    ntfy(result, series, episode)
