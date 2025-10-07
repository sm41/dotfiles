from sys import argv, exit
from mytool import ctrl_string as cs, ctrl_date as cd, scraping
import func, analyse, download


def main():
  cs.Argument.check_arg(argv[1])
  fsv   = func.Set_Variable()
  flud  = func.Line_Up_Contents()
  time  = cd.Date()
  time.yesterday(1).quarte(time.n_days_ago_date.month)

  if argv[1].startswith("https://tver.jp/episodes/"):
    cis = func.Check_Include_Series()

    cis.check_series_id(argv[1], fsv.loaded_yaml)
    flud.set_tmp_dict(argv[1], fsv.storage_dir, cis.header).append_contents()

  elif not argv[1].startswith("https://tver.jp/episodes/"):
    anlys = analyse.Anlys_Argument()

    if   argv[1] == "dow":
      anlys.find_key_value_list(fsv.loaded_yaml, time.n_days_ago_dow)
    elif argv[1] != "dow":
      anlys.find_key_dict(fsv.loaded_yaml, argv[1])

    if not anlys.result_list:
      print("Not Found")
      exit()

    for bmw in anlys.result_list:
      scraper  = scraping.Scrp()
      hohoniku = scraping.Channel()

      scraper.get_response(bmw["url"]).make2soup().simple("html.parser")
      hohoniku.tver(scraper.soup)
      flud.set_tmp_dict(scraper.url, fsv.storage_dir, bmw['header']).append_contents()

  download.kkk(flud, time)