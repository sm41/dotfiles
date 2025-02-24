

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