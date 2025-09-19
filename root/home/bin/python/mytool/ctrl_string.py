from pathlib import Path
from sys     import exit


class ctrl_arg:
  @staticmethod
  def check_arg(data):
    if len(data) <= 1:
      exit('Length is incorrect')


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
