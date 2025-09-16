from bs4     import BeautifulSoup
from yaml    import safe_load
from urllib  import request
# from pathlib import Path
from mytool import check_any

class gen_obj:
  # @staticmethod
  # def load_all_file(*path_parts):
  #   filename = Path(*path_parts)
  #   with filename.open(mode='r') as f:
  #     y_data = list(load_all(f, Loader=SafeLoader))
  #   return y_data

  @staticmethod
  def data2soup(url, type):
    get_xml = request.urlopen(url)
    check_any.check_any.check_status_code(get_xml)
    soup = BeautifulSoup(get_xml, type)
    return soup


class yaml_tool:
  @staticmethod
  def yaml_safe_load(path):
    with open(path, mode='r') as f:
      y_data = safe_load(f)
    return y_data