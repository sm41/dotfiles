
from os  import getenv
from mytool import ctrl_path
from pathlib import Path

class storage:
  def __init__(self, target_dir):
    self.tmp_dir     = "/tmp"
    __download_dir   = getenv("CLIENT_NETWORK_STORAGE_misc")
    self.storage_dir = ctrl_path.ctrl_path.mkdir_path(__download_dir, target_dir)


class local_data:
  def __init__(self, target_file):
    __local_data_dir  = getenv("XDG_CONFIG_HOME")
    self.local_data_path = Path(__local_data_dir, "script_python", target_file)

  # def yaml_path(self, yaml_filename):
  #   self.yaml_path_name = Path(self.local_data_dir, yaml_filename)
