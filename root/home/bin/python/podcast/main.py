
from subprocess import run
from os  import getenv, path
from sys import argv
import func, func_none
from mytool import abc


abc.check_arg()
argment_str = argv[1]

tmp_dir   = "/tmp"
download_dir   = getenv("CLIENT_NETWORK_STORAGE_misc")
state_file_dir = getenv("XDG_STATE_HOME")
storage_dir = abc.anlys_path(download_dir, "@podcast")


def main():

  y_dow        = abc.dow_yesterday(1)
  loaded_yaml  = abc.load_yaml(state_file_dir, "python", "ppp.yaml")

  if argment_str == "dow":
    today_list = func_none.get_today_list(loaded_yaml, y_dow)
  else:
    today_list = func_none.yui(loaded_yaml, argment_str)
  # print(today_list)


  for ttt in today_list:

    uuu = ttt['url']
    sss = ttt['plan']['anchor']

    soup     = abc.makesoup(uuu)
    qqq      = func.getconf(soup, sss)
    download = func_none.dl(qqq, tmp_dir)
    print(download)
    # result   = run(download)
    # abc.rnm(tmp_dir, qqq['name'], storage_dir, qqq['name'])
    # abc.ntfy(result, qqq['series_title'], qqq['episode_title'])


if __name__ == "__main__":
  main()