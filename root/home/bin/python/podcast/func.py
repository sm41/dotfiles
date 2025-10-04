from sys import argv
from mytool import ctrl_string, ctrl_path, ctrl_date


class Set_Variable:
  def __init__(self):
    lp = ctrl_path.Storage("@podcast")
    ld = ctrl_path.Local_Data("podcast_new.yaml")

    self.arg         = argv[1]
    self.tmp_dir     = lp.tmp_dir
    self.storage_dir = lp.storage_dir
    self.loaded_yaml = ctrl_path.Yaml_Tool.yaml_safe_load(ld.local_data_path)


class Set_Metadata:
  def __init__(self, soup):

    JJJ = ctrl_string.Ctrl_File()
    LLL = ctrl_date.Ctrl_Date()

    root_obj = soup.find("channel")
    item_obj = soup.find("item")

    self.series  = JJJ.zen2han(root_obj.title.string)
    self.episode = JJJ.zen2han(item_obj.title.string)
    self.date    = LLL.change_format(item_obj.pubDate.string, "%a, %d %b %Y %H:%M:%S %z", "%Y-%m-%d").formatted_date
    self.img     = root_obj.image.url.string.split('?')[0]
    self.url     = item_obj.enclosure.attrs['url'].split('?')[0]
    self.ext     = JJJ.get_ext(self.url)
    self.name    = JJJ.byte_count(f"[Podcast]_{self.series}_{self.date}_{self.episode}")


class Check:
  def __init__(self):
    self.reserve_list: list[dict] = []

  def check_today_list(self, y_data:dict, y_dow_str):
    for value in y_data.values():
      if y_dow_str in value.get('dow', []):
        self.reserve_list.append({**value})

  def check_series_name(self, y_data:dict, args):
    for key, value in y_data.items():
      if key == args:
        self.reserve_list.append({**value})

