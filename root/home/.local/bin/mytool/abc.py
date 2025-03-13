import shutil
from datetime import datetime, date, timedelta
from pathlib  import Path
from locale import setlocale, LC_TIME, LC_ALL
from urllib import request
from yaml import load, FullLoader
from bs4  import BeautifulSoup
from sys  import argv, exit
from plyer import notification


class check_any:
  def __init__(self):
    pass

  @staticmethod
  def check_arg():
    if len(argv) <= 1:
      exit('You need args!')

  @staticmethod
  def check_status_code(subject):
    if subject.getcode() != 200:
      print(f"Status Code is {subject.getcode()} !!")
      exit()


class ctrl_file:
  def __init__(self):
    pass

  def byte_count(input, limit=245):
    length = len(str(input).encode('utf-8'))

    if length < limit:
        return input

    if length > limit:
        ttt = input[:-1]
        result = ctrl_file.byte_count(ttt, limit) # 再帰呼び出しの結果を返す

        if len(result.encode('utf-8')) < limit:
            return result + "[@]"
        return result

  def zen2han(input):
    z_digit = '＃（）： 　／１２３４５６７８９０ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ'
    h_digit = '#():__-1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    z2h_digit = str.maketrans(z_digit, h_digit)
    output    = input.translate(z2h_digit)
    return output

  def get_basename(input):
    return Path(input).stem

  def get_ext(input):
    return Path(input).suffix


class ctrl_path:
  def __init__(self):
    pass

  @staticmethod
  def rnm(bfr_path, aftr_path):
    oldpath = Path(bfr_path)
    newpath = Path(aftr_path)
    shutil.move(oldpath, newpath)

  @staticmethod
  def anlys_path(*path_parts):
    down_dir = Path(*path_parts)
    down_dir.mkdir(parents=True, exist_ok=True)
    return down_dir


def dow_yesterday(day_int:int):
  setlocale(LC_TIME, 'ja_JP.UTF-8')

  d_today      = date.today()
  d_yesterday  = d_today - timedelta( days = day_int )
  y_dow_str = d_yesterday.strftime('%a')
  return y_dow_str


def load_yaml(*path_parts):
  filename = Path(*path_parts)
  with filename.open(mode='r') as f:
    y_data = load(f, Loader=FullLoader)
  return y_data


def xml2soup(url):
  get_xml = request.urlopen(url)
  check_any.check_status_code(get_xml)
  soup = BeautifulSoup(get_xml, "xml")
  return soup


def ntfy(result, text):
  if result.returncode == 0:
    notification.notify(title = "✅ Success", message = text)
  else:
    notification.notify(title = "⚠️ failed", message = text)

