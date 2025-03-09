
from sys import exit
import func_dl, func
from mytool import abc


def main():
  abc.check_arg()
  variable = func.gen_var()
  scraper  = func.scrp()
  testes   = func_dl.test()


  if variable.arg.startswith("https://tver.jp/episodes/"):
    testes.get_base_yaml(variable.loaded_yaml)
    testes.integrate(variable.arg, variable.storage_path, testes.config)
    func_dl.ccc(testes.series, testes.episode, testes.url, testes.id, testes.paths, testes.output)

  elif not variable.arg.startswith("https://tver.jp/episodes/"):
    if   variable.arg == "dow":
      y_dow    = abc.dow_yesterday(1)
      fix_list = func.find_key_value_list(variable.loaded_yaml, y_dow)
    elif variable.arg != "dow":
      fix_list = func.find_key_dict(variable.loaded_yaml, variable.arg)

    # print(fix_list)

    for bmw in fix_list:
      scraper.selenium(bmw["url"])
      scraper.tver(scraper.soup)
      testes.integrate(scraper.url, variable.storage_path, bmw)
      func_dl.ccc(testes.series, testes.episode, testes.url, testes.id, testes.paths, testes.output)

  else:
    exit("Invailed Argment!")

if __name__ == "__main__":
  main()