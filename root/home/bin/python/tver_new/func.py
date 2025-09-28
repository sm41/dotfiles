from subprocess import run
from mytool import ctrl_path
# import analyse


class gen_var:
  def __init__(self):
    lp = ctrl_path.storage("@tver")
    ld = ctrl_path.local_data("tver_new.yaml")

    self.storage_dir  = lp.storage_dir
    self.loaded_yaml  = ctrl_path.yaml_tool.yaml_safe_load(ld.local_data_path)


class check:
  def check_series_id(self, url, data):
    check_series = [
      "yt-dlp",
        "--print", "series_id",
        url
    ]

    series_id       = run(check_series, capture_output=True, text=True).stdout.strip()
    self.series_url = "https://tver.jp/series/" + series_id
    self.header     = self.get_header(self.series_url, data)

  def get_header(self, url, data):
    for key, value in data.items():
      if key.startswith("_"):
        continue
      if "url" not in value:
        continue
      if value['url'] == url:
        return value['header']

    return data['_http']['header']


class fff_list:
  def __init__(self):
    self.ukuk = []

  def mmkk(self, url, down_dir, header):
    self.fff = {
      "url"      : url,
      "down_dir" : down_dir,
      "header"   : header
    }
    return self

  def llsstt(self):
    self.ukuk.append(self.fff)
    return self