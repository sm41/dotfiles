
from os import getenv, path
from subprocess import run
import func, func_dl, func_util
from sys import argv

func_util.check_arg()
argment_str = argv[1]
tmp_dir = "/tmp"
state_file_dir = getenv("XDG_STATE_HOME")
env_dir = getenv("CLIENT_NETWORK_STORAGE_misc")
storage_dir = path.join(env_dir)
yaml_file = "ppp.yaml"



def main():

  y_dow        = func_util.dow_yesterday(1)
  loaded_yaml  = func_util.load_yaml(state_file_dir, yaml_file)

  if argment_str == "dow":
    today_list = func_util.get_today_list(loaded_yaml, y_dow)
  else:
    today_list = func_util.yui(loaded_yaml, argment_str)


  # print(today_list)

  for ttt in today_list:

    uuu = ttt['url']
    sss = ttt['plan']['anchor']

    soup     = func.makesoup(uuu)
    qqq      = func.getconf(soup, sss)
    download = func_dl.dl(qqq, tmp_dir)
    print(download)

    # run(download)
    # func.rnm(tmp_dir, storage_dir, qqq['name'])

if __name__ == "__main__":
  main()