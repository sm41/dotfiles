#!/usr/bin/python3

from os  import getenv
from sys import argv
import func_dow, func_share, func_dl, func_scrape

func_share.check_arg()
argment_str = argv[1]

download_path  = getenv("CLIENT_NETWORK_STORAGE_misc")
state_file_dir = getenv("XDG_STATE_HOME")
yaml_file = 'vvv.yaml'


def main():

  loaded_yaml = func_share.load_yaml(yaml_file, state_file_dir)

  if argment_str.startswith("https://tver.jp/episodes/"):

    yaml_config = func_share.get_yaml_data(loaded_yaml)
    sel_list    = func_share.get_ntfy_meta(argment_str, yaml_config)

    func_dl.bbb(sel_list, download_path, yaml_config)
    # print(sel_list)

  elif not argment_str.startswith("https://tver.jp/episodes/"):

    if   argment_str == "dow":
      y_dow     = func_dow.dow_yesterday(1)
      dow_list  = func_dow.out_get_dow(loaded_yaml, "dow", y_dow)
      fix_list  = func_dow.out_fix_dow(dow_list, y_dow)
    elif argment_str != "dow":
      fix_list  = func_dow.www(loaded_yaml, argment_str)

    for yaml_config in fix_list:
      material = func_scrape.selenium(yaml_config["url"])
      url      = func_scrape.tver(material)
      sel_list = func_share.get_ntfy_meta(url, yaml_config)
      func_dl.bbb(sel_list, download_path, yaml_config)

  else:
    print("Invailed Argment!")

if __name__ == "__main__":
  main()