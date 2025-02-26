
from yaml import load, FullLoader
from sys  import argv
from pathlib  import Path
from plyer    import notification
import shutil


def check_arg():
  if(len(argv) <= 1):
    print('You need args!')
    exit()


def load_yaml(*path_parts):
  filename = Path(*path_parts)
  with filename.open(mode='r') as f:
    y_data = load(f, Loader=FullLoader)
  return y_data


def anlys_path(*path_parts):
  down_dir = Path(*path_parts)
  down_dir.mkdir(parents=True, exist_ok=True)
  return down_dir


def rnm(tmp_dir, storage, filename):
  oldpath = Path(tmp_dir, filename)
  newpath = Path(storage, filename)
  shutil.move(oldpath, newpath)


def ntfy(result, upper, lower):
  if result.returncode == 0:
    notification.notify(title = "✅ Success", message = f"{upper}\n{lower}")
  else:
    notification.notify(title = "⚠️ failed", message = f"{upper}\n{lower}")


