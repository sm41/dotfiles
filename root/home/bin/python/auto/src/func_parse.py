
import func_main
import re

def apple_podcast(bouillon, cssslct):
  row_series   = bouillon.select_one(cssslct["series"]).get_text()
  row_episode  = bouillon.select_one(cssslct["episode"]).get_text()
  row_link     = bouillon.select_one(cssslct["link"]).attrs['href']

  return row_series, row_episode, row_link


def tver(bouillon, cssslct):
  row_series   = bouillon.select_one(cssslct["series"]).get_text()
  row_episode  = bouillon.select_one(cssslct["episode"]).get_text()
  row_link     = bouillon.select_one(cssslct["link"]).attrs['href']
  row_link_mod = "https://tver.jp" + row_link

  return row_series, row_episode, row_link_mod


def megaphone_fm(FFF, cssslct):
  bouillon = FFF.find("title", string=re.compile(cssslct["anchor"])).parent

  row_series   =      FFF.select_one(cssslct["series"]).get_text()
  row_episode  = bouillon.select_one(cssslct["episode"]).get_text()
  row_link     = bouillon.select_one(cssslct["link"]).attrs['url']

  return row_series, row_episode, row_link


def radiko(soup, cssslct):
  bouillon = soup.find(string=re.compile(cssslct["title"])).parent.parent

  row_series   = bouillon.select_one(cssslct["series"]).get_text()
  row_episode  = bouillon.select_one(cssslct["episode"]).get_text()
  row_link     = bouillon.select_one(cssslct["link"]).attrs['url']

  return row_series, row_episode, row_link



def ppp(platform, material, selector):
  if   platform == "apple_podcast":
    return apple_podcast(material, selector)

  elif platform == "tver":
    return tver(material, selector)

  elif platform == "megaphone_fm":
    return megaphone_fm(material, selector)

  elif platform == "radiko":
    return radiko(material, selector)