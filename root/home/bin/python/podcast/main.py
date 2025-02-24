
from subprocess import run
from os  import getenv, path
from sys import argv
import func, func_util, func_none

func_util.check_arg()
argment_str = argv[1]

tmp_dir   = "/tmp"
yaml_file = "ppp.yaml"
download_dir   = getenv("CLIENT_NETWORK_STORAGE_misc")
state_file_dir = getenv("XDG_STATE_HOME")
storage_dir = path.join(download_dir, "@podcast")



def main():

  y_dow        = func.dow_yesterday(1)
  loaded_yaml  = func_util.load_yaml(state_file_dir, yaml_file)

  if argment_str == "dow":
    today_list = func_none.get_today_list(loaded_yaml, y_dow)
  else:
    today_list = func_none.yui(loaded_yaml, argment_str)
  # print(today_list)


  for ttt in today_list:

    uuu = ttt['url']
    sss = ttt['plan']['anchor']

    soup     = func.makesoup(uuu)
    qqq      = func.getconf(soup, sss)
    download = func_none.dl(qqq, tmp_dir)
    result   = run(download)

    func_util.rnm(tmp_dir, storage_dir, qqq['name'])
    func_util.ntfy(result,)


if __name__ == "__main__":
  main()