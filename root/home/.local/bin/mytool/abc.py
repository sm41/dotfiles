import shutil
from datetime import datetime, date, timedelta
from pathlib  import Path
from locale import setlocale, LC_TIME, LC_ALL
from urllib import request
from yaml import load, FullLoader
from bs4  import BeautifulSoup
from sys  import argv, exit
from plyer import notification
from dataclasses import dataclass, InitVar, field


@dataclass
class check_any:
  @staticmethod
  def check_arg():
    if len(argv) <= 1:
      exit('You need args!')

  @staticmethod
  def check_status_code(subject):
    if subject.getcode() != 200:
      print(f"Status Code is {subject.getcode()} !!")
      exit()


@dataclass
class ctrl_file:
  @staticmethod
  def byte_count(input, limit=240):
    length = len(str(input).encode('utf-8'))

    if length < limit:
        return input

    if length > limit:
      ttt = input[:-1]
      result = ctrl_file.byte_count(ttt, limit) # 再帰呼び出しの結果を返す

      if len(result.encode('utf-8')) < limit:
        return result + "[…]"
      return result

  @staticmethod
  def zen2han(input):
    z_digit = '＃（）： 　／１２３４５６７８９０ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ'
    h_digit = '#():__-1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    z2h_digit = str.maketrans(z_digit, h_digit)
    output    = input.translate(z2h_digit)
    return output

  @staticmethod
  def get_basename(input):
    return Path(input).stem

  @staticmethod
  def get_ext(input):
    return Path(input).suffix


@dataclass
class ctrl_path:
  @staticmethod
  def rnm_path(bfr_path, aftr_path):
    oldpath = Path(bfr_path)
    newpath = Path(aftr_path)
    shutil.move(oldpath, newpath)

  @staticmethod
  def anlys_path(*path_parts):
    down_dir = Path(*path_parts)
    down_dir.mkdir(parents=True, exist_ok=True)
    return down_dir


@dataclass
class gen_obj:
  @staticmethod
  def load_file(*path_parts):
    filename = Path(*path_parts)
    with filename.open(mode='r') as f:
      y_data = load(f, Loader=FullLoader)
    return y_data

  @staticmethod
  def data2soup(url, type):
    get_xml = request.urlopen(url)
    check_any.check_status_code(get_xml)
    soup = BeautifulSoup(get_xml, type)
    return soup


def dow_yesterday(day_int:int):
  setlocale(LC_TIME, 'ja_JP.UTF-8')

  d_today     = date.today()
  d_yesterday = d_today - timedelta( days = day_int )
  y_dow_str   = d_yesterday.strftime('%a')
  return y_dow_str


@dataclass
class ctrl_date:
  day_int: InitVar[int]

  def __post_init__(self, day_int:int):
    setlocale(LC_TIME, 'ja_JP.UTF-8')
    self.d_today     = date.today()
    self.d_yesterday = self.d_today - timedelta( days = day_int )
    self.y_dow       = self.d_yesterday.strftime('%a')
    self.q_date      = (self.d_yesterday.month - 1) // 3 + 1


def ntfy(result, text):
  if result.returncode == 0:
    notification.notify(title = "✅ Success", message = text)
  else:
    notification.notify(title = "⚠️ failed", message = text)

