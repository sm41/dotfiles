
from subprocess import run
from pathlib  import Path
from mytool import abc
import func


def main():

  abc.check_any.check_arg()
  variable = func.gen_var()
  branch   = func.check_arg()

  if variable.arg == "dow":
    branch.today_list(variable.loaded_yaml, variable.y_dow)
  else:
    branch.series_name(variable.loaded_yaml, variable.arg)

  for ttt in branch.eee:
    uuu  = ttt['url']
    soup = abc.xml2soup(uuu)
    source   = func.gen_tag(soup)
    download = func.dl(source.url, source.img, source.name, source.ext, variable.tmp_dir)
    result   = run(download)
    # print(download)
    abc.ctrl_path.rnm(Path(variable.tmp_dir, source.name + source.ext), Path(variable.storage_dir, source.name + source.ext))
    abc.ntfy(result, f"{source.series}\n{source.episode}")

if __name__ == "__main__":
  main()