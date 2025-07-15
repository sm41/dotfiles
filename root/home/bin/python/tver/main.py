
from sys import exit
from mytool import utils
import func


def main():
  utils.Check_Any.check_arg()
  variable = func.Gen_Var()
  tag_tag  = func.Gen_Tag()

  if variable.arg.startswith("https://tver.jp/episodes/"):
    tag_tag.get_base_yaml(variable.loaded_yaml)
    tag_tag.integrate(variable.arg, variable.storage_path, tag_tag.config)
    func.ccc(tag_tag.series, tag_tag.episode, tag_tag.url, tag_tag.ext, tag_tag.id, tag_tag.paths, tag_tag.output, None, None)

  elif not variable.arg.startswith("https://tver.jp/episodes/"):
    scraper = func.Scrp()
    anlys   = func.Anlys()
    before  = utils.Ctrl_Date(1)

    if   variable.arg == "dow":
      anlys.find_key_value_list(variable.loaded_yaml, before.y_dow)
    elif variable.arg != "dow":
      anlys.find_key_dict(variable.loaded_yaml, variable.arg)

    for bmw in anlys.result_list:
      scraper.selenium(bmw["url"])
      scraper.tver(scraper.soup)
      tag_tag.integrate(scraper.url, variable.storage_path, bmw)
      func.ccc(tag_tag.series, tag_tag.episode, tag_tag.url, tag_tag.ext, tag_tag.id, tag_tag.paths, tag_tag.output, before.d_yesterday.year, before.q_date)

  else:
    exit("Invailed Argment!")

