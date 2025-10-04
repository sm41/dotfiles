from pathlib import Path
from sys     import exit
import unicodedata

class Ctrl_Arg:
  @staticmethod
  def check_arg(data):
    if len(data) <= 1:
      exit('Length is incorrect')


class Ctrl_File:
  @staticmethod
  def byte_count(input, limit=240):
    length = len(str(input).encode('utf-8'))

    if length < limit:
      return input

    if length > limit:
      ttt = input[:-1]
      result = Ctrl_File.byte_count(ttt, limit) # 再帰呼び出しの結果を返す

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


def line_up_dict(some_dict:dict):

  max_key   = max(some_dict.keys(),   key=lambda k: get_display_width(str(k)))
  max_value = max(some_dict.values(), key=lambda v: get_display_width(str(v)))

  k_byte_length = get_display_width(str(max_key))
  v_byte_length = get_display_width(str(max_value))

  print("+" + ("-"*(k_byte_length + 2)) + "+" + ("-"*(v_byte_length + 2)) + "+")

  for key, value in some_dict.items():
    print(f"| {str(key).ljust(k_byte_length)} | {value}")

  print("+" + ("-"*(k_byte_length + 2)) + "+" + ("-"*(v_byte_length + 2)) + "+")


def get_display_width(text):
  width = 0
  for ch in text:
    eaw = unicodedata.east_asian_width(ch)
    if eaw in ('F', 'W'):
      width += 2
    else:
      width += 1
  return width