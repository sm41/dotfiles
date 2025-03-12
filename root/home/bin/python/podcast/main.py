
from subprocess import run
from pathlib  import Path
from mytool import abc
import func


def main():

  abc.check_any.check_arg()
  variable = func.gen_var()
  branch   = func.check_arg()

  y_dow        = abc.dow_yesterday(1)
  loaded_yaml  = abc.load_yaml(variable.state_file_dir, "python", "ppp.yaml")

  if variable.arg == "dow":
    branch.today_list(loaded_yaml, y_dow)
  else:
    branch.series_name(loaded_yaml, variable.arg)

  for ttt in branch.eee:
    uuu = ttt['url']

    soup     = abc.makesoup(uuu)
    source   = func.gen_tag(soup)
    download = func.dl(source.url, source.img, source.name, source.ext, variable.tmp_dir)
    # print(download)
    result   = run(download)
    abc.ctrl_path.rnm(Path(variable.tmp_dir, source.name), Path(variable.storage_dir, source.name))
    abc.ntfy(result, f"{source.series}\n{source.episode}")

if __name__ == "__main__":
  main()