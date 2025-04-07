
from sys import exit
from mytool import abc
import func


def main():
  abc.check_any.check_arg()
  variable = func.gen_var()
  testes   = func.test()
  scraper  = func.scrp()
  anlys    = func.anlys()

  if variable.arg.startswith("https://tver.jp/episodes/"):
    testes.get_base_yaml(variable.loaded_yaml)
    testes.integrate(variable.arg, variable.storage_path, testes.config)
    func.ccc(testes.series, testes.episode, testes.url, testes.ext, testes.id, testes.paths, testes.output)

  elif not variable.arg.startswith("https://tver.jp/episodes/"):
    if   variable.arg == "dow":
      anlys.find_key_value_list(variable.loaded_yaml, variable.y_dow)
    elif variable.arg != "dow":
      anlys.find_key_dict(variable.loaded_yaml, variable.arg)

    for bmw in anlys.result_list:
      scraper.selenium(bmw["url"])
      scraper.tver(scraper.soup)
      testes.integrate(scraper.url, variable.storage_path, bmw)
      func.ccc(testes.series, testes.episode, testes.url, testes.ext, testes.id, testes.paths, testes.output)

  else:
    exit("Invailed Argment!")

# if __name__ == "__main__":
#   main()