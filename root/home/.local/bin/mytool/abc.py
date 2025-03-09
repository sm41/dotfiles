import shutil
from datetime import datetime, date, timedelta
from pathlib  import Path
from locale import setlocale, LC_TIME, LC_ALL
from urllib import request
from yaml import load, FullLoader
from bs4  import BeautifulSoup
from sys  import argv, exit
from plyer import notification


def check_arg():
  if(len(argv) <= 1):
    exit('You need args!')


def check_status_code(subject):  # スペルミスを修正
  if subject.getcode() != 200:
    print(f"Status Code is {subject.getcode()} !!")  # スペルミスを修正
    exit()


def dow_yesterday(day_int:int):
  setlocale(LC_TIME, 'ja_JP.UTF-8')

  d_today      = date.today()
  d_yesterday  = d_today - timedelta( days = day_int )
  y_dow_str = d_yesterday.strftime('%a')
  return y_dow_str


def zen2han(input):
  z_digit = '＃（）： 　／１２３４５６７８９０ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ'
  h_digit = '#():__-1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

  z2h_digit = str.maketrans(z_digit, h_digit)
  iop = input.translate(z2h_digit)
  return iop


def load_yaml(*path_parts):
  filename = Path(*path_parts)
  with filename.open(mode='r') as f:
    y_data = load(f, Loader=FullLoader)
  return y_data


def makesoup(url):
  get_xml = request.urlopen(url)
  check_status_code(get_xml)  # スペルミスを修正
  soup = BeautifulSoup(get_xml, "xml")
  return soup


def ntfy(result, upper, lower):
  if result.returncode == 0:
    notification.notify(title = "✅ Success", message = f"{upper}\n{lower}")
  else:
    notification.notify(title = "⚠️ failed", message = f"{upper}\n{lower}")


def rnm(bfr_dir, bfr_name, aftr_dir, aftr_name):
  oldpath = Path(bfr_dir, bfr_name)
  newpath = Path(aftr_dir, aftr_name)
  shutil.move(oldpath, newpath)


def anlys_path(*path_parts):
  down_dir = Path(*path_parts)
  down_dir.mkdir(parents=True, exist_ok=True)
  return down_dir