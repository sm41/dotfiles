
import re

def apple_podcast(bouillon):
  series   = bouillon.find(class_="headings__title svelte-mr6v6m").get_text()
  episode  = bouillon.find(class_="episode-details__title-text").get_text()
  link     = bouillon.select_one("li.svelte-8rlk6b:nth-child(1) > div:nth-child(1) > a:nth-child(1)").attrs['href']

  return series, episode, link


def test_apple(beautiful, anchor):

  pin_target = beautiful.find(class_="episode-details__title-text", text=re.compile(anchor))
  pin_parent = pin_target.find_parent(class_="svelte-8rlk6b")

  series   = beautiful.find(class_="headings__title svelte-mr6v6m").get_text()
  episode  = pin_parent.find(class_="episode-details__title-text").get_text()
  link     = pin_parent.find(class_="link-action svelte-1wtdvjb").attrs['href']

  return series, episode, link


def tver(bouillon):
  series   = bouillon.find(class_="series-main_title__cOS46").get_text()
  episode  = bouillon.find(class_="episode-row_title__6W7Ar").get_text()
  link     = bouillon.find(class_="episode-row_container___2msI").attrs['href']
  link_mod = "https://tver.jp" + link

  return series, episode, link_mod


def megaphone_fm(FFF, cssslct):
  bouillon = FFF.find("title", string=re.compile(cssslct["anchor"])).parent

  series   =      FFF.select_one("rss > channel > title").get_text()
  episode  = bouillon.select_one("item > title").get_text()
  link     = bouillon.select_one("enclosure").attrs['url']

  return series, episode, link


# def apple_podcast(bouillon, cssslct):
#   series   = bouillon.select_one(cssslct["series"]).get_text()
#   episode  = bouillon.select_one(cssslct["episode"]).get_text()
#   link     = bouillon.select_one(cssslct["link"]).attrs['href']

#   return series, episode, link


# def tver(bouillon, cssslct):
#   series   = bouillon.select_one(cssslct["series"]).get_text()
#   episode  = bouillon.select_one(cssslct["episode"]).get_text()
#   link     = bouillon.select_one(cssslct["link"]).attrs['href']
#   link_mod = "https://tver.jp" + link

#   return series, episode, link_mod


# def radiko(soup, cssslct):
#   bouillon = soup.find(string=re.compile(cssslct["title"])).parent.parent

#   series   = bouillon.select_one(cssslct["series"]).get_text()
#   episode  = bouillon.select_one(cssslct["episode"]).get_text()
#   link     = bouillon.select_one(cssslct["link"]).attrs['url']

#   return series, episode, link



def ppp(platform, material, anchor):
  if   platform == "apple_podcast":
    if anchor == None:
      return apple_podcast(material)
    else:
      return test_apple(material, anchor)
  elif platform == "tver":
    return tver(material)
  # elif platform == "megaphone_fm":
  #   return megaphone_fm(material, selector)
  # elif platform == "radiko":
  #   return radiko(material, selector)