from subprocess import run
from pathlib  import Path
from mytool import ctrl_path, ctrl_string, notify
import tenpai


def insert_quoter(filename:str, year, q_date):
  if filename.startswith("[ドラマ]"):
    return filename.replace('_', f'_[{year}-Q{q_date}]_', 1)
  else:
    return filename


def ytdlp(paths, id, ext, url):
  method = [
    "yt-dlp",
      "-q",
      "--console-title",
      "--embed-subs",
      "--paths",  str(paths),
      "--output", f"{id}.{ext}",
    url
  ]
  return method


def ppp(hhh:tenpai.gen_tag, year, q_date):
    method = ytdlp(hhh.dirname, hhh.id, hhh.ext, hhh.url)
    result = run(method)
    hhh.basename = insert_quoter(hhh.basename, year, q_date)
    hhh.basename = ctrl_string.ctrl_file.byte_count(hhh.basename, 245)
    ctrl_path.ctrl_path.rnm_path(Path(hhh.dirname, f"{hhh.id}.{hhh.ext}"), Path(hhh.dirname, f"{hhh.basename}.{hhh.ext}"))
    notify.ntfy(result, f"{hhh.series}\n{hhh.episode}")
