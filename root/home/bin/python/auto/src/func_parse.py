
import func_main
import re

def apple_podcast(bouillon):
  ROW_SERIES   = bouillon.select_one(func_main.set_selector["series"]).get_text()
  ROW_EPISODE  = bouillon.select_one(func_main.set_selector["episode"]).get_text()
  ROW_LINK     = bouillon.select_one(func_main.set_selector["link"]).attrs['href']

  return ROW_SERIES, ROW_EPISODE, ROW_LINK


def tver(bouillon):
  ROW_SERIES   = bouillon.select_one(func_main.set_selector["series"]).get_text()
  ROW_EPISODE  = bouillon.select_one(func_main.set_selector["episode"]).get_text()
  ROW_LINK     = bouillon.select_one(func_main.set_selector["link"]).attrs['href']
  ROW_LINK_MOD = "https://tver.jp" + ROW_LINK

  return ROW_SERIES, ROW_EPISODE, ROW_LINK_MOD


def megaphone_fm(FFF):
  bouillon = FFF.find("title", string=re.compile(func_main.SET_MEMBER["anchor"])).parent

  ROW_SERIES   =      FFF.select_one(func_main.set_selector["series"]).get_text()
  ROW_EPISODE  = bouillon.select_one(func_main.set_selector["episode"]).get_text()
  ROW_LINK     = bouillon.select_one(func_main.set_selector["link"]).attrs['url']

  return ROW_SERIES, ROW_EPISODE, ROW_LINK


def radiko(soup):
  bouillon = soup.find(string=re.compile(func_main.SET_MEMBER["title"])).parent.parent

  ROW_SERIES   = bouillon.select_one(func_main.set_selector["series"]).get_text()
  ROW_EPISODE  = bouillon.select_one(func_main.set_selector["episode"]).get_text()
  ROW_LINK     = bouillon.select_one(func_main.set_selector["link"]).attrs['url']

  return ROW_SERIES, ROW_EPISODE, ROW_LINK



def ppp(platform, material):
  if platform == "apple_podcast":
    return apple_podcast(material)

  elif platform == "tver":
    return tver(material)

  elif platform == "megaphone_fm":
    return megaphone_fm(material)

  elif platform == "radiko":
    return radiko(material)