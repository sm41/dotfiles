
from pathlib  import Path
from plyer    import notification
import shutil


def dl(qqq, tmp_dir):

  url = qqq['url']
  img = qqq['img']
  filename = qqq['name']

  download = [
    "ffmpeg",
      "-loglevel", "warning",
      "-i",   url,
      "-i",   img,
      "-map", "0:a",
      "-map", "1:v",
      "-metadata:s:v", "title='Album cover'",
      "-metadata:s:v", "comment='Cover (Front)'",
      "-codec", "copy",
    f"{tmp_dir}/{filename}"
  ]

  return download


def rnm(tmp_dir, storage, filename):
  oldpath = Path(tmp_dir, filename)
  newpath = Path(storage, filename)
  shutil.move(oldpath, newpath)


def ntfy(result, upper:str, lower:str):
  if result.returncode == 0:
    notification.notify(title = "✅ Success", message = f"{upper}\n{lower}")
  else:
    notification.notify(title = "⚠️ failed", message = f"{upper}\n{lower}")