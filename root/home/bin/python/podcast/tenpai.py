from pathlib import Path
from subprocess import run
from mytool import ctrl_string, ctrl_path, scraping, notify
import func


def dl(source:func.gen_tag, tmp_dir):
  download = [
    "ffmpeg",
      "-loglevel", "warning",
      "-i",   source.url,
      "-i",   source.img,
      "-map", "0:a",
      "-map", "1:v",
      "-metadata:s:v", "title='Album cover'",
      "-metadata:s:v", "comment='Cover (Front)'",
      "-codec", "copy",
    f"{tmp_dir}/{source.name}{source.ext}"
  ]
  return download


def ddwwnn(branch:func.check_arg, variable:func.gen_var):

  for ttt in branch.reserve_list:
    qqq    = scraping.scrp()
    soup   = qqq.get_response(ttt['url']).simple("xml").soup
    source = func.gen_tag(soup)

    ctrl_string.line_up_dict(source.__dict__)

    download = dl(source, variable.tmp_dir)
    result   = run(download)
    ctrl_path.ctrl_path.rnm_path(Path(variable.tmp_dir, source.name + source.ext), Path(variable.storage_dir, source.name + source.ext))
    notify.ntfy(result, f"{source.series}\n{source.episode}")