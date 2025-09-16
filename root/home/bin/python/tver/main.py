from sys import exit
from mytool import check_any, scraping
import func


def main():
  check_any.check_any.check_arg()
  variable = func.Gen_Var()
  tag_tag  = func.Gen_Tag()

  if variable.arg.startswith("https://tver.jp/episodes/"):
    tag_tag.get_base_yaml(variable.loaded_yaml)
    tag_tag.integrate(variable.arg, variable.storage_dir, tag_tag.config)
    func.ccc(tag_tag, None, None)

  elif not variable.arg.startswith("https://tver.jp/episodes/"):
    scraper = scraping.selenium()
    anlys   = func.Anlys()
    time    = func.time(1)

    if   variable.arg == "dow":
      anlys.find_key_value_list(variable.loaded_yaml, time.date.n_days_ago_dow)
    elif variable.arg != "dow":
      anlys.find_key_dict(variable.loaded_yaml, variable.arg)

    if not anlys.result_list:
      print("Not Found")
      exit(0)

    for bmw in anlys.result_list:
      scraper.make_soup(bmw["url"])
      # fuga = scraping.hoge(bmw["url"])
      # fuga.make2soup().simple(fuga.response, "html.parser")

      # print(fuga.soup)
      # exit()

      scraper.tver(scraper.soup)
      tag_tag.integrate(scraper.url, variable.storage_dir, bmw)
      func.ccc(tag_tag, time.date.n_days_ago_date.year, time.date.quarte_date)

  else:
    exit("Invailed Argment!")

