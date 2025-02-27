
from datetime import datetime, date, timedelta
from locale import setlocale, LC_TIME, LC_ALL
from bs4 import BeautifulSoup
from re  import match, sub, compile
from mytool import abc


def change_format(episode_date):
  setlocale(LC_TIME, (None,None))

  format_str_tz = "%a, %d %b %Y %H:%M:%S %z"
  dt_tz = datetime.strptime(episode_date, format_str_tz)
  yyy = dt_tz.strftime("%Y-%m-%d")
  return yyy


def get_searchitem(rrr, search_term):

  if search_term is None:
    search_term = ".+"

  for iii in rrr:
    if match(search_term, iii.title.string):
      target_item = iii
      break

  return target_item


def getconf(soup:BeautifulSoup, search_term):
  root_obj     = soup.find("channel")
  series_title = root_obj.title.string
  series_img   = root_obj.image.url.string.split('?')[0]

  target_obj  = soup.find_all("item", limit=50)
  target_item = get_searchitem(target_obj, search_term)
  episode_title = target_item.title.string
  episode_date  = target_item.pubDate.string
  episode_url   = target_item.enclosure.attrs['url'].split('?')[0]

  ddd = change_format(episode_date)
  sss = abc.zen2han(series_title)
  eee = abc.zen2han(episode_title)

  filename = f"[Podcast]_{sss}_{ddd}_{eee}.mp3"

  qqq = {
    "series_title": sss,
    "episode_title": eee,
    "img": series_img,
    "url": episode_url,
    "name": filename
  }

  return qqq

