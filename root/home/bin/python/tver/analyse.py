
class anlys:
  def __init__(self):
    self.result_list = []

  # def find_key_dict(self, data, target_key):
  #   if isinstance(data, dict):
  #     for key, value in data.items():
  #       if key.startswith("_"):
  #         continue
  #       if key == target_key:
  #         self.result_list.append(value)
  #         return self.result_list
  #       result = self.find_key_dict(value, target_key)
  #       if result is not None:
  #         return result


  def find_key_dict(self, data, target_key):
    if isinstance(data, dict):
      for key, value in data.items():
        if key.startswith("_"):
          continue
        if key == target_key:
          self.result_list.append(value)
          return self.result_list
        # result = self.find_key_dict(value, target_key)
        # if result is not None:
          # return result


  # def find_key_value_list(self, data, target_key):
  #   if isinstance(data, dict):
  #     for key1, value1 in data.items():
  #       if key1.startswith("_"):
  #         continue
  #       if "dow" not in value1:
  #         self.find_key_value_list(value1, target_key)
  #       else:
  #         for dow_item in value1['dow']:
  #           if dow_item == target_key:
  #             self.result_list.append(value1)
  #             # break  # 同じtitleのデータが複数回追加されないようにする


  def find_key_value_list(self, data, target_key):
    if isinstance(data, dict):
      for key, value in data.items():
        if key.startswith("_"):
          continue
        for dow_item in value['dow']:
          if dow_item == target_key:
            self.result_list.append(value)
