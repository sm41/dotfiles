
from subprocess import run
from pathlib import Path
from mytool  import check_any, ctrl_path, ctrl_date, gen_obj, notify
import func
from sys import exit


def main():

  check_any.check_any.check_arg()
  variable = func.Gen_Var()
  branch   = func.Check_Arg()
  before   = ctrl_date.ctrl_date(1)

  if variable.arg == "dow":
    branch.today_list(variable.loaded_yaml, before.y_dow)
  else:
    branch.series_name(variable.loaded_yaml, variable.arg)


  # print(branch.reserve_list)
  # exit()

  for ttt in branch.reserve_list:
    soup   = gen_obj.gen_obj.data2soup(ttt['url'], "xml")
    source = func.Gen_Tag(soup)

    # print(source.episode)
    # continue

    download = func.dl(source, variable.tmp_dir)
    result   = run(download)
    ctrl_path.ctrl_path.rnm_path(Path(variable.tmp_dir, source.name + source.ext), Path(variable.storage_dir, source.name + source.ext))
    notify.ntfy(result, f"{source.series}\n{source.episode}")
