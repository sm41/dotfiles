
from datetime import date, timedelta
from locale   import setlocale, LC_TIME


def dow_yesterday(day_int:int):
  setlocale(LC_TIME, 'ja_JP.UTF-8')

  d_today      = date.today()
  d_yesterday  = d_today - timedelta( days = day_int )
  y_dow_str:str = d_yesterday.strftime('%a')
  return y_dow_str


def out_get_dow(deploy_yaml_list, target_key, find_value):

  dow_list:list = []

  for iii in deploy_yaml_list:
    for pltfrm, prpty in iii.items():
      for genre, param in prpty.items():
        if genre == 'config':
          continue
        for cnfg, lstky in param.items():
          if cnfg == "header":
            continue
          for dwanchr in lstky['plan']:
            if dwanchr[target_key] == find_value:
              hypr = {**prpty['config'], 'header':param['header'], **lstky}
              dow_list.append(hypr)
  return dow_list


def out_fix_dow(dict_list:list, y_dow_str:str):

  fix_dow_list:list = []

  for input_dict in dict_list:
    for qqq in input_dict["plan"]:
      if qqq["dow"] == y_dow_str:
        ygyg = {
          "platform": input_dict["platform"],
          "child_dir":input_dict["child_dir"],
          "header":   input_dict["header"],
          "link":     input_dict["url"],
          "anchor":   qqq["anchor"]
          }
        fix_dow_list.append(ygyg)
  return fix_dow_list