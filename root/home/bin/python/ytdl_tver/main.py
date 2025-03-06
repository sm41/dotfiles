
# from os  import getenv
from sys import argv, exit
import func_dl, func_scrape
from mytool import abc


def main():

  abc.check_arg()
  variable = func_scrape.gen_var()
  zxc      = func_scrape.scrp()
  dldl     = func_dl.direct_link()

  if variable.arg.startswith("https://tver.jp/episodes/"):
    dldl.get_base_yaml(variable.loaded_yaml)
    dldl.get_ntfy_meta(variable.arg)
    func_dl.bbb(dldl.series, dldl.episode, dldl.url, variable.storage_path, dldl.ghq)

  elif not variable.arg.startswith("https://tver.jp/episodes/"):
    if   variable.arg == "dow":
      y_dow     = abc.dow_yesterday(1)
      fix_list  = func_scrape.out_get_dow(variable.loaded_yaml, y_dow)
    elif variable.arg != "dow":
      fix_list  = func_scrape.www2(variable.loaded_yaml, variable.arg)

    for bmw in fix_list:
      zxc.selenium(bmw["url"])
      zxc.tver(zxc.soup)
      dldl.get_ntfy_meta(zxc.url)
      func_dl.bbb(dldl.series, dldl.episode, dldl.url,  variable.storage_path, bmw)

  else:
    exit("Invailed Argment!")

if __name__ == "__main__":
  main()