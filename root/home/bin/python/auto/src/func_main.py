
from plyer    import notification
import func_parse, func_scrape, func_ytdlp

import subprocess
import datetime
import locale
import sys
import os
import yaml


def tgtg(y_path, y_d_set):

  uuu = []

  for y_file in y_d_set:
    filename = os.path.join(y_path, 'python', y_file)
    with open(filename, mode='r') as f:
      y_data = yaml.load(f, Loader=yaml.FullLoader)
      uuu.append(y_data)
  return uuu


def alt_dow(uuu, target_key, find_value):

  dow_tuple = []

  for iii in uuu:
    for pltfrm, prpty in iii.items():
      for cntnts, siries in prpty['contents'].items():
        for dwanchr in siries['plan']:
          if dwanchr[target_key] == find_value:
            pppp = {**prpty['config'], **siries}
            dow_tuple.append(pppp)
  return dow_tuple


def alt_arg(uuu, target_key, find_value):

  arg_tuple = []

  for iii in uuu:
    for pltfrm, prpty in iii.items():
      for cntnts, siries in prpty['contents'].items():
        if cntnts == find_value:
          pppp = {**prpty['config'], **siries, 'yyyy':cntnts}
          arg_tuple.append(pppp)
  return arg_tuple


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


def sub(vvvv, y_dow_symbol):

  for input_dict in vvvv:

    set_platform = input_dict["platform"]
    set_scraper  = input_dict["scraper"]

    for qqq in input_dict["plan"]:
      if qqq["dow"] == y_dow_symbol:
        set_anchor = qqq["anchor"]
      elif "yyyy" in input_dict:
        set_anchor = None

    material = func_scrape.hhh(set_scraper, input_dict["url"])
    series, episode, link = func_parse.ppp(set_platform, material, set_anchor)

    print(series, episode, link)
    continue
    sys.exit()

    method = func_ytdlp.rrr(link, set_platform)
    result = subprocess.run(method)

    ntfy(result, series, episode)