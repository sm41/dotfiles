
from plyer    import notification
import array_element
import func_parse, func_scrape, func_ytdlp

import subprocess
import datetime
import locale
import sys

def get_tuple(module_set, target_key, find_value):

  dict_tuple = []

  for ooo in module_set:
    tuple_var = getattr(ooo, "tuple_dict")

    for var_dict in tuple_var:
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




def main(vvvv):

  for input_dict in vvvv:

    set_platform = input_dict["platform"]
    set_scraper  = input_dict["scraper"]
    # SET_MEMBER   = input_dict

    set_selector = get_tuple([ array_element ], "var", set_platform)[0]
    material = func_scrape.hhh(set_scraper, input_dict["url"])
    series, episode, link = func_parse.ppp(set_platform, material, set_selector)

    # print(series, episode, link)
    # continue
    # sys.exit()

    method = func_ytdlp.ooo(link, set_platform)
    result = subprocess.run(method)

    if result.returncode == 0:
      notification.notify(
        title = "✅ Success",
        message = f"{series}\n{episode}"
      )
    else:
      notification.notify(
        title = "⚠️ failed",
        message = f"{series}\n{episode}"
      )

