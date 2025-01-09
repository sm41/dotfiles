#!/usr/bin/python3

import func_main, func_ytdlp
from os import getenv
import sys
import subprocess

func_main.check_arg()
argment_str:str  = sys.argv[1]

env_var_str:str = "XDG_STATE_HOME"
state_file_dir_str:str = getenv(env_var_str)

storage_path_str:str = "CLIENT_NETWORK_STORAGE_www"
download_path_str:str = getenv(storage_path_str)

def main():
  if argment_str.startswith("https://"):
    yaml_files_list:list = [ 'uuu.yaml' ]
    anlys_yaml_list:list = func_main.anlys(yaml_files_list, state_file_dir_str)

    yaml_data_dict:dict   = func_main.out_yaml_data(argment_str, anlys_yaml_list)
    series, episode, link = func_main.out_ntfy_meta(argment_str, yaml_data_dict)
    ntfy_meta_dict:dict   = func_main.mix(series, episode, link)
    method                = func_ytdlp.vvv(yaml_data_dict, ntfy_meta_dict, download_path_str, state_file_dir_str)
    result                = subprocess.run(method)
    func_main.ntfy(result, ntfy_meta_dict["upper"], ntfy_meta_dict["lower"])
    # print(method)
  elif argment_str == "dow":
    yaml_files_list:list = [ 'audio.yaml', 'video.yaml' ]
    anlys_yaml_list:list = func_main.anlys(yaml_files_list, state_file_dir_str)

    y_dow_str:str          = func_main.dow_yesterday(1)
    get_dow_list:list      = func_main.out_get_dow(anlys_yaml_list, "dow", y_dow_str)
    fix_dow_list:list      = func_main.out_fix_dow(get_dow_list, y_dow_str)
    result, ntfy_meta_dict = func_main.looping(fix_dow_list, download_path_str)
    func_main.ntfy(result, ntfy_meta_dict["upper"], ntfy_meta_dict["lower"])
    # print(fix_dow_list)
  else:
    print("Invailed Argment!")

if __name__ == "__main__":
  main()