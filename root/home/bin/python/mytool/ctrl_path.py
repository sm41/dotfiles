import shutil
from os  import getenv
from pathlib import Path


class storage:
  def __init__(self, target_dir):
    self.tmp_dir     = "/tmp"
    __download_dir   = getenv("CLIENT_NETWORK_STORAGE_misc")
    self.storage_dir = ctrl_path.mkdir_path(__download_dir, target_dir)


class local_data:
  def __init__(self, target_file):
    __local_data_dir     = getenv("XDG_CONFIG_HOME")
    self.local_data_path = Path(__local_data_dir, "script_python", target_file)

  # def yaml_path(self, yaml_filename):
  #   self.yaml_path_name = Path(self.local_data_dir, yaml_filename)


class ctrl_path:
  @staticmethod
  def rnm_path(bfr_path, aftr_path):
    oldpath = Path(bfr_path)
    newpath = Path(aftr_path)
    shutil.move(oldpath, newpath)

  @staticmethod
  def mkdir_path(*path_parts):
    down_dir = Path(*path_parts)
    down_dir.mkdir(parents=True, exist_ok=True)
    return down_dir
