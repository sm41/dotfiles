import func_parse, func_scrape, func_ytdlp

import datetime
import locale
import subprocess

from urllib.parse import urlparse
from pathlib import Path
from plyer   import notification

import sys
import yaml


def check_arg():
  if(len(sys.argv) <= 1):
    print('You need args!')
    sys.exit()


def anlys(yaml_files_list:list, state_file_dir_str:str):

  deploy_yaml_list:list = []
  ddd = Path(state_file_dir_str)

  for picked_yaml_file in yaml_files_list:
    filename = ddd.joinpath('python', picked_yaml_file)
    with filename.open(mode='r') as f:
      y_data = yaml.load(f, Loader=yaml.FullLoader)
      deploy_yaml_list.append(y_data)
  return deploy_yaml_list


def mix(series, episode, link):
  key_data:list   = [ "upper", "lower", "link" ]
  value_data:list = [ series, episode, link ]
  mix_dict:dict = dict(zip(key_data, value_data))

  return mix_dict


def ntfy(result, upper:str, lower:str):
  if result.returncode == 0:
    notification.notify(title = "✅ Success", message = f"{upper}\n{lower}")
  else:
    notification.notify(title = "⚠️ failed", message = f"{upper}\n{lower}")


def out_yaml_data(url:str, deploy_yaml_list:list):

  url_parsed_tuple = urlparse(url)
  path_directory = Path(url_parsed_tuple.path)

  for vvv in deploy_yaml_list:
    for domain, path in vvv.items():
      if url_parsed_tuple.hostname.endswith(domain):
        for prprty, dict in path.items():
          if 'parts' in str(dict):
            for mmm in dict['parts']:
              if mmm in str(path_directory):
                meta_dict = {
                  "platform":   dict['platform'],
                  "child_dir":  path['child_dir'],
                  "meta_list":  path['meta_list'],
                  "playlist":   dict['playlist'],
                  "path_tuple": path_directory.parts,
                  }
  return meta_dict


def out_ntfy_meta(url:str, meta_tag:dict):

  if meta_tag['playlist']:
    series, episode, link = "hoge", "fuga", url
  else:
    get_meta_method = [
      "yt-dlp",
        "--print", meta_tag['meta_list'][0],
        "--print", meta_tag['meta_list'][1],
        "--print", meta_tag['meta_list'][2],
        url
      ]
    meta = subprocess.run(get_meta_method, capture_output=True, text=True).stdout
    series, episode, link = meta.splitlines()

  return series, episode, link


def dow_yesterday(day_int:int):
  locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')

  d_today      = datetime.date.today()
  d_yesterday  = d_today - datetime.timedelta( days = day_int )
  y_dow_str:str = d_yesterday.strftime('%a')
  return y_dow_str


def out_get_dow(deploy_yaml_list, target_key, find_value):

  dow_list:list = []

  for iii in deploy_yaml_list:
    for pltfrm, prpty in iii.items():
      for cntnts, siries in prpty['contents'].items():
        for dwanchr in siries['plan']:
          if dwanchr[target_key] == find_value:
            pppp = {**prpty['config'], **siries}
            dow_list.append(pppp)
  return dow_list


def out_fix_dow(dict_list:list, y_dow_str:str):

  fix_dow_list:list = []

  for input_dict in dict_list:
    for qqq in input_dict["plan"]:
      if qqq["dow"] == y_dow_str:
        ygyg = {
          "platform": input_dict["platform"],
          "child_dir":input_dict["child_dir"],
          "scraper":  input_dict["scraper"],
          "link":     input_dict["url"],
          "anchor":   qqq["anchor"]
          }
        fix_dow_list.append(ygyg)
  return fix_dow_list


def looping(fix_dow_list, storage_path:str, state_file_dir_str:str):

  for yaml_data_dict in fix_dow_list:
    material = func_scrape.hhh(yaml_data_dict["scraper"], yaml_data_dict["link"])
    series, episode, link = func_parse.ppp(material, yaml_data_dict["platform"], yaml_data_dict["anchor"])

    ntfy_meta_dict = mix(series, episode, link)
    method         = func_ytdlp.vvv(yaml_data_dict, ntfy_meta_dict, storage_path, state_file_dir_str)
    result         = subprocess.run(method)

  return result, ntfy_meta_dict
