from sys import argv, exit
from mytool import ctrl_string, scraping, ctrl_date
import func, tenpai, analyse, download


def main():
  ctrl_string.ctrl_arg.check_arg(argv[1])
  variable = func.gen_var()
  check_id = func.check()
  flfl     = func.fff_list()
  time     = ctrl_date.ctrl_date()
  time.yesterday(1).quarte(time.n_days_ago_date.month)

  if argv[1].startswith("https://tver.jp/episodes/"):
    check_id.check_series_id(argv[1], variable.loaded_yaml)
    flfl.mmkk(argv[1], variable.storage_dir, check_id.header).llsstt()

  elif not argv[1].startswith("https://tver.jp/episodes/"):
    anlys = analyse.anlys()

    if   argv[1] == "dow":
      anlys.find_key_value_list(variable.loaded_yaml, time.n_days_ago_dow)
    elif argv[1] != "dow":
      anlys.find_key_dict(variable.loaded_yaml, argv[1])

    if not anlys.result_list:
      print("Not Found")
      exit(0)

    for bmw in anlys.result_list:
      scraper  = scraping.scrp()
      hohoniku = scraping.channel()

      scraper.get_response(bmw["url"]).make2soup().simple("html.parser")
      hohoniku.tver(scraper.soup)
      flfl.mmkk(scraper.url, variable.storage_dir, bmw['header']).llsstt()

  inside_list  = []

  for kkk in flfl.ukuk:
    tptp = tenpai.gen_tag()
    tptp.get_metadata(kkk['url'], kkk['down_dir'], kkk['header'])

    inside_list.append(tptp)
    ctrl_string.line_up_dict(tptp.__dict__)

  for ddd in inside_list:
    download.ppp(ddd, time.n_days_ago_date.year, time.quarte_date)