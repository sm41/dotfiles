
class parse_file:
  reserve_list = []

  def today_list(self, yaml_file, y_dow_str):
    for key, value in yaml_file.items():
      for pln in value['dow']:
        if pln == y_dow_str:
          self.reserve_list.append({**value})

  def series_name(self, yaml_file, args):
    for ttl, cnfg in yaml_file.items():
      if ttl == args:
        self.reserve_list.append({**cnfg})


def yaml2arg(yaml_list:list):
  opt_arg = []
  key_to_option = {
    'station': '-s',
    'title':   '-t',
  }

  for yaml_value in yaml_list:
    aaa = {}
    for key, value in key_to_option.items():
      option = yaml_value.get(key)
      if option:
        aaa[value] = option
    opt_arg.extend([aaa])

  return opt_arg

