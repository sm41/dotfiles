
from datetime import datetime
from locale import setlocale, LC_TIME, LC_ALL
from urllib import request
from bs4  import BeautifulSoup
from re   import match



def change_format(episode_date):
  setlocale(LC_TIME, (None,None))

  format_str_tz = "%a, %d %b %Y %H:%M:%S %z"
  dt_tz = datetime.strptime(episode_date, format_str_tz)
  yyy = dt_tz.strftime("%Y-%m-%d")
  return yyy


def makesoup(url):
  get_xml = request.urlopen(url)
  # check_ststus_code(get_xml)
  soup = BeautifulSoup(get_xml, "xml")
  return soup


def get_searchterms(rrr, search_term):

  if search_term is None:
    search_term = ".+"

  for iii in rrr:
    if match(search_term, iii.title.string):
      target_item = iii
      break

  return target_item


def getconf(soup, search_term):
  root_obj = soup.find("channel")

  series_title = root_obj.title.string
  series_img   = root_obj.image.url.string.split('?')[0]

  rrr = soup.find_all("item", limit=50)
  target_item = get_searchterms(rrr, search_term)

  episode_title = target_item.title.string
  episode_date  = target_item.pubDate.string
  episode_url   = target_item.enclosure.attrs['url'].split('?')[0]
  ddd = change_format(episode_date)

  filename = f"[Podcast]_{series_title}_{ddd}_{episode_title}.mp3"

  qqq = {
    "img": series_img,
    "url": episode_url,
    "name": filename
  }

  return qqq

