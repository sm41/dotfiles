
from pathlib    import Path
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

