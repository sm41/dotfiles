#!/usr/bin/python3

import func_dow, func_url, func_share
from func_ytdlp import vvv
from subprocess import run
from os  import getenv
from sys import argv

func_share.check_arg()
argment_str:str  = argv[1]

state_file_dir_str:str = getenv("XDG_STATE_HOME")
download_path_str:str  = getenv("CLIENT_NETWORK_STORAGE_misc")

def main():
  if argment_str.startswith("https://"):
    yaml_files_list:list  = [ 'uuu.yaml' ]
    anlys_yaml_list:list  = func_share.anlys(yaml_files_list, state_file_dir_str)

    yaml_data_dict:dict   = func_url.out_yaml_data(argment_str, anlys_yaml_list)
    series, episode, link = func_url.out_ntfy_meta(argment_str, yaml_data_dict)
    ntfy_meta_dict:dict   = func_share.mix(series, episode, link)
    method                = vvv(yaml_data_dict, ntfy_meta_dict, download_path_str, state_file_dir_str)
    result                = run(method)
    func_share.ntfy(result, ntfy_meta_dict["upper"], ntfy_meta_dict["lower"])
    # print(method)

  elif not argment_str.startswith("https://"):
    yaml_files_list:list = [ 'audio.yaml', 'video.yaml' ]
    anlys_yaml_list:list = func_share.anlys(yaml_files_list, state_file_dir_str)

    if   argment_str == "dow":
      y_dow_str:str      = func_dow.dow_yesterday(1)
      get_dow_list:list  = func_dow.out_get_dow(anlys_yaml_list, "dow", y_dow_str)
      fix_dow_list:list  = func_dow.out_fix_dow(get_dow_list, y_dow_str)
    elif argment_str != "dow":
      fix_dow_list:list  = func_dow.www(anlys_yaml_list, argment_str)

    func_dow.looping(fix_dow_list, download_path_str, state_file_dir_str)
    # print(fix_dow_list)

  else:
    print("Invailed Argment!")

if __name__ == "__main__":
  main()