from re import compile

def apple_podcast(bouillon, anchor):

  if   anchor is None:
    pin_parent = bouillon.find(class_ = compile("section--episode"))
  elif anchor is not None:
    pin_target = bouillon.find(class_ = "episode-details__title-text", text = compile(anchor))
    pin_parent = pin_target.find_parent("li", class_ = compile("svelte"))

  series   =   bouillon.find(class_ = compile("headings__title")).get_text()
  episode  = pin_parent.find(class_ = compile("episode-details__title-text")).get_text()
  link     = pin_parent.find(class_ = compile("link-action")).attrs['href']

  return series, episode, link


def tver(bouillon):

  series   = bouillon.find(class_ = compile("series-main_title")).get_text()
  episode  = bouillon.find(class_ = compile("episode-row_title")).get_text()
  link     = bouillon.find(class_ = compile("episode-row_container")).attrs['href']
  link_mod = "https://tver.jp" + link

  return series, episode, link_mod


def ppp(material, platform, anchor):

  if   platform == "apple_podcast":
    return apple_podcast(material, anchor)

  elif platform == "tver":
    return tver(material)

  # elif platform == "radiko":
  #   return radiko(material, selector)