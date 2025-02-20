
from datetime import date, timedelta
from locale   import setlocale, LC_TIME, LC_ALL
from pathlib  import Path
from yaml import load, FullLoader
from sys import argv


def check_arg():
  if(len(argv) <= 1):
    print('You need args!')
    exit()


def dow_yesterday(day_int:int):
  setlocale(LC_TIME, 'ja_JP.UTF-8')

  d_today      = date.today()
  d_yesterday  = d_today - timedelta( days = day_int )
  y_dow_str:str = d_yesterday.strftime('%a')
  return y_dow_str


def load_yaml(state_file_dir, yaml_file):
  filename = Path(state_file_dir, 'python', yaml_file)
  with filename.open(mode='r') as f:
    y_data = load(f, Loader=FullLoader)
  return y_data


def get_today_list(y_data, y_dow_str):

  eee = []

  for platform, mmm in y_data.items():
    for cntnt, zzz in mmm.items():
      for ppp in zzz['plan']:
        if ppp['dow'] == y_dow_str:
          kkk = {
            **zzz,
            "plan": ppp
          }
          eee.append(kkk)
  return eee


def yui(y_data, args):

  eee = []

  for platform, mmm in y_data.items():
    for cntnt, zzz in mmm.items():
      if cntnt == args:
        kkk = {
          **zzz,
          "plan": zzz['plan'][0]
        }
        eee.append(kkk)
  return eee
