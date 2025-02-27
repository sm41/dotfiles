
from os  import getenv
from sys import argv, exit
import func_share, func_dl, func_scrape, func_none
from mytool import abc


abc.check_arg()
argment_str = argv[1]

download_path  = getenv("CLIENT_NETWORK_STORAGE_misc")
state_file_dir = getenv("XDG_STATE_HOME")

def main():

  storage_path = abc.anlys_path(download_path, "@tver")
  loaded_yaml  = abc.load_yaml(state_file_dir, "python", "vvv.yaml")

  if argment_str.startswith("https://tver.jp/episodes/"):
    yaml_config = func_share.get_yaml_data(loaded_yaml)
    seu_list    = func_share.get_ntfy_meta(argment_str)
    func_dl.bbb(seu_list, storage_path, yaml_config)
  elif not argment_str.startswith("https://tver.jp/episodes/"):
    if   argment_str == "dow":
      y_dow     = abc.dow_yesterday(1)
      fix_list  = func_none.out_get_dow(loaded_yaml, y_dow)
    elif argment_str != "dow":
      fix_list  = func_none.www(loaded_yaml, argment_str)
    # print(fix_list)

    for yaml_config in fix_list:
      material = func_scrape.selenium(yaml_config["url"])
      url      = func_scrape.tver(material)
      seu_list = func_share.get_ntfy_meta(url)
      func_dl.bbb(seu_list, storage_path, yaml_config)
  else:
    exit("Invailed Argment!")

if __name__ == "__main__":
  main()