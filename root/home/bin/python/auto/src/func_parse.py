
import re

def apple_podcast(bouillon, anchor):

  if   anchor is None:
    pin_parent = bouillon.find(class_ = re.compile("section--episode"))
  elif anchor is not None:
    pin_target = bouillon.find(class_ = "episode-details__title-text", text = re.compile(anchor))
    pin_parent = pin_target.find_parent("li", class_ = re.compile("svelte"))

  series   =   bouillon.find(class_ = re.compile("headings__title")).get_text()
  episode  = pin_parent.find(class_ = re.compile("episode-details__title-text")).get_text()
  link     = pin_parent.find(class_ = re.compile("link-action")).attrs['href']

  return series, episode, link


def tver(bouillon):
  series   = bouillon.find(class_ = re.compile("series-main_title")).get_text()
  episode  = bouillon.find(class_ = re.compile("episode-row_title")).get_text()
  link     = bouillon.find(class_ = re.compile("episode-row_container")).attrs['href']
  link_mod = "https://tver.jp" + link

  return series, episode, link_mod


def megaphone_fm(FFF, cssslct):
  bouillon = FFF.find("title", string=re.compile(cssslct["anchor"])).parent

  series   =      FFF.select_one("rss > channel > title").get_text()
  episode  = bouillon.select_one("item > title").get_text()
  link     = bouillon.select_one("enclosure").attrs['url']

  return series, episode, link


def ppp(platform, material, anchor):

  if   platform == "apple_podcast":
    return apple_podcast(material, anchor)

  elif platform == "tver":
    return tver(material)

  # elif platform == "megaphone_fm":
  #   return megaphone_fm(material, selector)

  # elif platform == "radiko":
  #   return radiko(material, selector)