from sys import argv, exit
from mytool import ctrl_string, scraping, ctrl_date
import func


def main():
  ctrl_string.ctrl_arg.check_arg(argv[1])
  variable = func.gen_var()
  tag_tag  = func.gen_tag()

  if variable.arg.startswith("https://tver.jp/episodes/"):
    tag_tag.get_base_yaml(variable.loaded_yaml)
    tag_tag.integrate(variable.arg, variable.storage_dir, tag_tag.config)
    func.ccc(tag_tag, None, None)

  elif not variable.arg.startswith("https://tver.jp/episodes/"):
    anlys = func.anlys()
    time  = ctrl_date.ctrl_date().yesterday(1)
    time.quarte(time.n_days_ago_date.month)

    if   variable.arg == "dow":
      anlys.find_key_value_list(variable.loaded_yaml, time.n_days_ago_dow)
    elif variable.arg != "dow":
      anlys.find_key_dict(variable.loaded_yaml, variable.arg)

    if not anlys.result_list:
      print("Not Found")
      exit(0)

    for bmw in anlys.result_list:
      scraper = scraping.scrp().check_status_code(bmw["url"])
      scraper.make2soup().simple("html.parser")

      # print(scraper.soup)
      # exit()

      scraper.tver(scraper.soup)
      tag_tag.integrate(scraper.url, variable.storage_dir, bmw)
      func.ccc(tag_tag, time.n_days_ago_date.year, time.quarte_date)

  else:
    exit("Invailed Argment!")

