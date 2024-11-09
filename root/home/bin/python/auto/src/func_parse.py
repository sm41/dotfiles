
import func_main
import re

def apple_podcast(bouillon, cssslct):
  ROW_SERIES   = bouillon.select_one(cssslct["series"]).get_text()
  ROW_EPISODE  = bouillon.select_one(cssslct["episode"]).get_text()
  ROW_LINK     = bouillon.select_one(cssslct["link"]).attrs['href']

  return ROW_SERIES, ROW_EPISODE, ROW_LINK


def tver(bouillon, cssslct):
  ROW_SERIES   = bouillon.select_one(cssslct["series"]).get_text()
  ROW_EPISODE  = bouillon.select_one(cssslct["episode"]).get_text()
  ROW_LINK     = bouillon.select_one(cssslct["link"]).attrs['href']
  ROW_LINK_MOD = "https://tver.jp" + ROW_LINK

  return ROW_SERIES, ROW_EPISODE, ROW_LINK_MOD


def megaphone_fm(FFF, cssslct):
  bouillon = FFF.find("title", string=re.compile(func_main.SET_MEMBER["anchor"])).parent

  ROW_SERIES   =      FFF.select_one(cssslct["series"]).get_text()
  ROW_EPISODE  = bouillon.select_one(cssslct["episode"]).get_text()
  ROW_LINK     = bouillon.select_one(cssslct["link"]).attrs['url']

  return ROW_SERIES, ROW_EPISODE, ROW_LINK


def radiko(soup, cssslct):
  bouillon = soup.find(string=re.compile(func_main.SET_MEMBER["title"])).parent.parent

  ROW_SERIES   = bouillon.select_one(cssslct["series"]).get_text()
  ROW_EPISODE  = bouillon.select_one(cssslct["episode"]).get_text()
  ROW_LINK     = bouillon.select_one(cssslct["link"]).attrs['url']

  return ROW_SERIES, ROW_EPISODE, ROW_LINK



def ppp(platform, material, mmm):
  if platform == "apple_podcast":
    return apple_podcast(material, mmm)

  elif platform == "tver":
    return tver(material, mmm)

  elif platform == "megaphone_fm":
    return megaphone_fm(material, mmm)

  elif platform == "radiko":
    return radiko(material, mmm)