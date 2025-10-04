
class anlys:
  def __init__(self):
    self.result_list = []

  def find_key_dict(self, data, target_key):
    if isinstance(data, dict):
      for key, value in data.items():
        if key.startswith("_"):
          continue
        if key == target_key:
          self.result_list.append(value)
          return self.result_list

  def find_key_value_list(self, data, target_key):
    if isinstance(data, dict):
      for key, value in data.items():
        if key.startswith("_"):
          continue
        for dow_item in value['dow']:
          if dow_item == target_key:
            self.result_list.append(value)
