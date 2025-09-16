
from sys import exit
from pathlib import Path
from subprocess import run
from mytool  import check_any, ctrl_path, gen_obj, notify
import func


def main():

  check_any.check_any.check_arg()
  variable = func.gen_var()
  branch   = func.check_arg()
  time     = func.time(1)

  if variable.arg == "dow":
    branch.today_list(variable.loaded_yaml, time.n_days_ago_dow)
  else:
    branch.series_name(variable.loaded_yaml, variable.arg)

  if not branch.reserve_list:
    print("No matching podcast found.")
    exit()

  for ttt in branch.reserve_list:
    soup   = gen_obj.gen_obj.data2soup(ttt['url'], "xml")
    source = func.gen_tag(soup)

    # print(source.episode)
    # continue

    download = func.dl(source, variable.tmp_dir)
    result   = run(download)
    ctrl_path.ctrl_path.rnm_path(Path(variable.tmp_dir, source.name + source.ext), Path(variable.storage_dir, source.name + source.ext))
    notify.ntfy(result, f"{source.series}\n{source.episode}")
