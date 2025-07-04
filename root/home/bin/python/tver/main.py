
from sys import exit
from mytool import abc
import func


def main():
  abc.check_any.check_arg()
  variable = func.gen_var()
  tag_tag  = func.gen_tag()

  if variable.arg.startswith("https://tver.jp/episodes/"):
    tag_tag.get_base_yaml(variable.loaded_yaml)
    tag_tag.integrate(variable.arg, variable.storage_path, tag_tag.config)
    func.ccc(tag_tag.series, tag_tag.episode, tag_tag.url, tag_tag.ext, tag_tag.id, tag_tag.paths, tag_tag.output, None, None)

  elif not variable.arg.startswith("https://tver.jp/episodes/"):
    scraper = func.scrp()
    anlys   = func.anlys()
    before  = abc.ctrl_date(1)

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

