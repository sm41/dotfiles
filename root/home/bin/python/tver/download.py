from subprocess import run, CompletedProcess
from pathlib  import Path
from mytool import ctrl_date as cd, ctrl_path as cp, ctrl_string as cs, notify
import func


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


class Set_Metadata:
  def get_metadata(self, url, down_dir, header):
    cmd_ytdlp = [
      "yt-dlp",
        "--paths",  f"home:{down_dir}",
        "--output", f"{header}",
        "--print",  "series",
        "--print",  "episode",
        "--print",  "original_url",
        "--print",  "filename",
        "--print",  "ext",
        "--print",  "id",
      url
    ]
    ddd: CompletedProcess = run(cmd_ytdlp, capture_output=True, text=True).stdout.strip()
    rxw = ddd.splitlines()
    self.series, self.episode, self.url, filename, self.ext, self.id = rxw[:6]
    self.dirname  = Path(filename).parent
    self.basename = cs.File_Tool.zen2han(Path(filename).stem)


def kkk(flfl:func.Line_Up_Contents, time:cd.Date):
  today_dl_lists  = []

  for kkk in flfl.contents_list:
    jsondata = Set_Metadata()
    jsondata.get_metadata(kkk['url'], kkk['down_dir'], kkk['header'])

    today_dl_lists.append(jsondata)
    cs.line_up_dict(jsondata.__dict__)


  for dl_parts in today_dl_lists:
    dl_parts:Set_Metadata

    method = ytdlp(dl_parts.dirname, dl_parts.id, dl_parts.ext, dl_parts.url)
    result = run(method)
    dl_parts.basename = insert_quoter(dl_parts.basename, time.n_days_ago_date.year, time.quarte_date)
    dl_parts.basename = cs.File_Tool.byte_count(dl_parts.basename, 245)
    cp.Path_Tool.rnm_path(Path(dl_parts.dirname, f"{dl_parts.id}.{dl_parts.ext}"), Path(dl_parts.dirname, f"{dl_parts.basename}.{dl_parts.ext}"))
    notify.ntfy(result, f"{dl_parts.series}\n{dl_parts.episode}")