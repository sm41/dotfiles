import shutil
from os      import getenv
from yaml    import safe_load
from pathlib import Path


class Storage:
  def __init__(self, target_dir):
    self.tmp_dir     = "/tmp"
    download_dir     = getenv("CLIENT_NETWORK_STORAGE_misc")
    self.storage_dir = Ctrl_Path.mkdir_path(download_dir, target_dir)


class Local_Data:
  def __init__(self, target_file):
    local_data_dir       = getenv("XDG_CONFIG_HOME")
    self.local_data_path = Path(local_data_dir, "script_python", target_file)


class Ctrl_Path:
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


class Yaml_Tool:
  @staticmethod
  def yaml_safe_load(path):
    with open(path, mode='r') as f:
      y_data = safe_load(f)
    return y_data