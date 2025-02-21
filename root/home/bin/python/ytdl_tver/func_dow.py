
from datetime import date, timedelta
from locale   import setlocale, LC_TIME
import func_dl, func_scrape, func_share


def dow_yesterday(day_int:int):
  setlocale(LC_TIME, 'ja_JP.UTF-8')

  d_today      = date.today()
  d_yesterday  = d_today - timedelta( days = day_int )
  y_dow_str:str = d_yesterday.strftime('%a')
  return y_dow_str


def out_get_dow(deploy_yaml:list, target_key, find_value):

  dow_list:list = []

  for pltfrm, prpty in deploy_yaml.items():
    for genre, param in prpty.items():
      if genre == 'config':
        continue
      for cntnts, series in param.items():
        if cntnts != "contents":
          continue
        for title, spec in series.items():
          for hoge in spec['plan']:
            if hoge[target_key] == find_value:
              hypr = {
                **prpty['config'],
                **spec,
                'header': param['header'],
                }
              dow_list.append(hypr)
  return dow_list


def out_fix_dow(dict_list:list, y_dow_str:str):

  fix_dow_list:list = []

  for input_dict in dict_list:
    for qqq in input_dict["plan"]:
      if qqq["dow"] == y_dow_str:
        ygyg = {
          **input_dict,
          "anchor":    qqq["anchor"]
          }
        fix_dow_list.append(ygyg)
  return fix_dow_list


def www(deploy_yaml:list, keyword:str):

  hogefuga = []

  for pltfrm, prpty in deploy_yaml.items():
    for genre, param in prpty.items():
      if param == 'config':
        continue
      for cntnts, series in param.items():
        if cntnts != "contents":
          continue
        for title, spec in series.items():
          if title == keyword:
            hypr = {
              **prpty['config'],
              **spec,
              'header': param['header'],
              'anchor': spec['plan'][0]['anchor']
              }
            hogefuga.append(hypr)
  return hogefuga


def looping(fix_dow_list:list, download_path:str):

  for yaml_config in fix_dow_list:
    material = func_scrape.selenium(yaml_config["url"])
    url = func_scrape.tver(material)
    sel_list = func_share.get_ntfy_meta(url, yaml_config)

    func_dl.bbb(sel_list, download_path, yaml_config)
    # print(kkk)