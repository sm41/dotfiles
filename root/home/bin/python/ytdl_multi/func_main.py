from func_parse  import ppp
from func_scrape import selenium
from func_ytdlp  import vvv

from subprocess   import run
from sys  import argv, exit


def check_arg():
  if(len(argv) <= 1):
    print('You need args!')
    exit()


def mix(series, episode, link):
  key_data:list   = [ "upper", "lower", "link" ]
  value_data:list = [ series, episode, link ]
  mix_dict:dict = dict(zip(key_data, value_data))

  return mix_dict


def looping(fix_dow_list, storage_path:str, state_file_dir_str:str):

  for yaml_data_dict in fix_dow_list:
    material = selenium(yaml_data_dict["link"])
    series, episode, link = ppp(material, yaml_data_dict["platform"], yaml_data_dict["anchor"])

    ntfy_meta_dict = mix(series, episode, link)
    method         = vvv(yaml_data_dict, ntfy_meta_dict, storage_path, state_file_dir_str)
    result         = run(method)

  return result, ntfy_meta_dict
