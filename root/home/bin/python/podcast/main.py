
from subprocess import run
from pathlib import Path
from mytool  import utils
import func


def main():

  utils.Check_Any.check_arg()
  variable = func.Gen_Var()
  branch   = func.Check_Arg(variable.root_string)
  before   = utils.Ctrl_Date(1)

  if variable.arg == "dow":
    branch.today_list(variable.loaded_yaml, before.y_dow)
  else:
    branch.series_name(variable.loaded_yaml, variable.arg)

  for ttt in branch.reserve_list:
    soup   = utils.Gen_Obj.data2soup(ttt['url'], "xml")
    source = func.Gen_Tag(soup)

    download = func.dl(source.url, source.img, source.name, source.ext, variable.tmp_dir)
    result   = run(download)
    utils.Ctrl_Path.rnm_path(Path(variable.tmp_dir, source.name + source.ext), Path(variable.storage_dir, source.name + source.ext))
    utils.ntfy(result, f"{source.series}\n{source.episode}")
