from pathlib  import Path
import shutil



class ctrl_path:
  @staticmethod
  def rnm_path(bfr_path, aftr_path):
    oldpath = Path(bfr_path)
    newpath = Path(aftr_path)
    shutil.move(oldpath, newpath)

  @staticmethod
  def anlys_path(*path_parts):
    down_dir = Path(*path_parts)
    down_dir.mkdir(parents=True, exist_ok=True)
    return down_dir
