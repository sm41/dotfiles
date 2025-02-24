
from yaml import load, FullLoader
from sys  import argv
from pathlib  import Path
from plyer    import notification
import shutil


def rnm(tmp_dir, storage, filename):
  oldpath = Path(tmp_dir, filename)
  newpath = Path(storage, filename)
  shutil.move(oldpath, newpath)


def ntfy(result, upper:str, lower:str):
  if result.returncode == 0:
    notification.notify(title = "✅ Success", message = f"{upper}\n{lower}")
  else:
    notification.notify(title = "⚠️ failed", message = f"{upper}\n{lower}")


def check_arg():
  if(len(argv) <= 1):
    print('You need args!')
    exit()


def load_yaml(state_file_dir, yaml_file):
  filename = Path(state_file_dir, 'python', yaml_file)
  with filename.open(mode='r') as f:
    y_data = load(f, Loader=FullLoader)
  return y_data
