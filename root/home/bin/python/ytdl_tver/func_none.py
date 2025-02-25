

def out_get_dow(deploy_yaml:list, find_value):

  dow_list:list = []

  for pltfrm, prpty in deploy_yaml.items():
    for genre, param in prpty.items():
      if genre == 'config':
        continue
      for cntnts, series in param.items():
        if cntnts != "contents":
          continue
        for title, spec in series.items():
          for hoge in spec['dow']:
            if hoge == find_value:
              hypr = {
                **spec,
                'header': param['header'],
                }
              dow_list.append(hypr)
  return dow_list


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
              **spec,
              'header': param['header'],
              }
            hogefuga.append(hypr)
  return hogefuga
