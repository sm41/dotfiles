
# from os  import getenv
from sys import argv, exit
import func_dl, func_scrape
from mytool import abc


def main():

  abc.check_arg()
  variable = func_scrape.gen_var()
  scraper  = func_scrape.scrp()
  # dldl     = func_dl.direct_link()
  testes   = func_dl.test()

  if variable.arg.startswith("https://tver.jp/episodes/"):
    testes.get_base_yaml(variable.loaded_yaml)
    # dldl.get_ntfy_meta(variable.arg)
    testes.integrate(variable.arg, variable.storage_path, testes.ghq)
    # func_dl.bbb(dldl.series, dldl.episode, dldl.url, variable.storage_path, dldl.ghq)
    func_dl.ccc(testes.series, testes.episode, testes.url, testes.id, testes.paths, testes.output)
    # print(testes.series, testes.episode, testes.url, testes.paths, testes.output)

  elif not variable.arg.startswith("https://tver.jp/episodes/"):
    if   variable.arg == "dow":
      y_dow     = abc.dow_yesterday(1)
      fix_list  = func_scrape.out_get_dow(variable.loaded_yaml, y_dow)
    elif variable.arg != "dow":
      fix_list  = func_scrape.www2(variable.loaded_yaml, variable.arg)

    for bmw in fix_list:
      scraper.selenium(bmw["url"])
      scraper.tver(scraper.soup)
      # dldl.get_ntfy_meta(scraper.url)
      testes.integrate(scraper.url, variable.storage_path, bmw)
      # func_dl.bbb(dldl.series, dldl.episode, dldl.url, variable.storage_path, bmw)
      func_dl.ccc(testes.series, testes.episode, testes.url, testes.id, testes.paths, testes.output)

  else:
    exit("Invailed Argment!")

if __name__ == "__main__":
  main()