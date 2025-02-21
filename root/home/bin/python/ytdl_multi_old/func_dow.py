
from func_parse  import ppp
from func_scrape import selenium
import func_share

from datetime import date, timedelta
from locale   import setlocale, LC_TIME


def dow_yesterday(day_int:int):
  setlocale(LC_TIME, 'ja_JP.UTF-8')

  d_today      = date.today()
  d_yesterday  = d_today - timedelta( days = day_int )
  y_dow_str:str = d_yesterday.strftime('%a')
  return y_dow_str


def out_get_dow(deploy_yaml_list:list, target_key, find_value):

  dow_list:list = []

  for select_yaml in deploy_yaml_list:
    for pltfrm, prpty in select_yaml.items():
      for genre, param in prpty.items():
        if genre == 'config':
          continue
        for cntnts, series in param.items():
          if cntnts != "contents":
            continue
          for title, spec in series.items():
            for hoge in spec['plan']:
              if hoge[target_key] == find_value:
                hypr = {**prpty['config'], 'header':param['header'], **spec}
                dow_list.append(hypr)
  return dow_list


def out_fix_dow(dict_list:list, y_dow_str:str):

  fix_dow_list:list = []

  for input_dict in dict_list:
    for qqq in input_dict["plan"]:
      if qqq["dow"] == y_dow_str:
        ygyg = {
          "child_dir":input_dict["child_dir"],
          "platform": input_dict["platform"],
          "header":   input_dict["header"],
          "link":     input_dict["url"],
          "anchor":   qqq["anchor"]
          }
        fix_dow_list.append(ygyg)
  return fix_dow_list


def www(deploy_yaml_list:list, keyword:str):

  hogefuga = []

  for select_yaml in deploy_yaml_list:
    for pltfrm, prpty in select_yaml.items():
      for genre, param in prpty.items():
        if genre == 'config':
          continue
        for cntnts, series in param.items():
          if cntnts != "contents":
            continue
          for title, spec in series.items():
            if title == keyword:
              hypr = {**prpty['config'], 'header':param['header'], 'link':spec['url'], 'anchor':spec['plan'][0]['anchor']}
              hogefuga.append(hypr)
  return hogefuga


def looping(fix_dow_list:list, download_path_str:str, state_file_dir_str:str):

  for yaml_data_dict in fix_dow_list:
    material = selenium(yaml_data_dict["link"])
    series, episode, link  = ppp(material, yaml_data_dict["platform"], yaml_data_dict["anchor"])

    func_share.bbb(series, episode, link, download_path_str, yaml_data_dict)
    # print(method)