from sys import argv, exit
from mytool import ctrl_string, scraping, ctrl_date
import func, analyse, download


def main():
  ctrl_string.ctrl_arg.check_arg(argv[1])
  variable = func.gen_var()
  check_id = func.check()
  flfl     = func.line_up_contents()
  time     = ctrl_date.ctrl_date()
  time.yesterday(1).quarte(time.n_days_ago_date.month)

  if argv[1].startswith("https://tver.jp/episodes/"):
    check_id.check_series_id(argv[1], variable.loaded_yaml)
    flfl.set_tmp_dict(argv[1], variable.storage_dir, check_id.header).append_contents()

  elif not argv[1].startswith("https://tver.jp/episodes/"):
    anlys = analyse.anlys()

    if   argv[1] == "dow":
      anlys.find_key_value_list(variable.loaded_yaml, time.n_days_ago_dow)
    elif argv[1] != "dow":
      anlys.find_key_dict(variable.loaded_yaml, argv[1])

    if not anlys.result_list:
      print("Not Found")
      exit()

    for bmw in anlys.result_list:
      scraper  = scraping.scrp()
      hohoniku = scraping.channel()

      scraper.get_response(bmw["url"]).make2soup().simple("html.parser")
      hohoniku.tver(scraper.soup)
      flfl.set_tmp_dict(scraper.url, variable.storage_dir, bmw['header']).append_contents()

  download.kkk(flfl, time)