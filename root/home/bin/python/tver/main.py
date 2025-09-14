
from sys import exit
from mytool import check_any, ctrl_date
import func


def main():
  check_any.check_any.check_arg()
  variable = func.Gen_Var()
  tag_tag  = func.Gen_Tag()

  if variable.arg.startswith("https://tver.jp/episodes/"):
    tag_tag.get_base_yaml(variable.loaded_yaml)
    tag_tag.integrate(variable.arg, variable.storage_path, tag_tag.config)
    func.ccc(tag_tag, None, None)

  elif not variable.arg.startswith("https://tver.jp/episodes/"):
    scraper = func.Scrp()
    anlys   = func.Anlys()
    before  = ctrl_date.ctrl_date(1)

    if   variable.arg == "dow":
      anlys.find_key_value_list(variable.loaded_yaml, before.y_dow)
    elif variable.arg != "dow":
      anlys.find_key_dict(variable.loaded_yaml, variable.arg)

    if not anlys.result_list:
      print("Not Found")
      exit(0)

    for bmw in anlys.result_list:
      scraper.selenium(bmw["url"])
      scraper.tver(scraper.soup)
      tag_tag.integrate(scraper.url, variable.storage_path, bmw)
      func.ccc(tag_tag, before.d_yesterday.year, before.q_date)

  else:
    exit("Invailed Argment!")

