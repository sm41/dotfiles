
from subprocess import run
from pathlib import Path
from mytool  import abc
import func


def main():

  abc.check_any.check_arg()
  variable = func.gen_var()
  branch   = func.check_arg(variable.root_string)
  before   = abc.ctrl_date(1)

  if variable.arg == "dow":
    branch.today_list(variable.loaded_yaml, before.y_dow)
  else:
    branch.series_name(variable.loaded_yaml, variable.arg)

  for ttt in branch.reserve_list:
    soup   = abc.gen_obj.data2soup(ttt['url'], "xml")
    source = func.gen_tag(soup)

    download = func.dl(source.url, source.img, source.name, source.ext, variable.tmp_dir)
    result   = run(download)
    abc.ctrl_path.rnm_path(Path(variable.tmp_dir, source.name + source.ext), Path(variable.storage_dir, source.name + source.ext))
    abc.ntfy(result, f"{source.series}\n{source.episode}")
