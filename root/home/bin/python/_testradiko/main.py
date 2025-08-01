
from os import remove
from re import compile, IGNORECASE
from subprocess import run
import func, func_auth, func_dow
from mytool import abc
from sys import argv
import __main__
from dataclasses import dataclass, field, InitVar


#JP+都道府県コード ex) 北海道 => JP1    沖縄 => JP47
#国土交通省 https://nlftp.mlit.go.jp/ksj/gml/codelist/PrefCd.html
#Area ID: JP8   https://radiko.jp/v3/station/list/JP8.xml
#
#https://radiko.jp/v3/program/station/date/20301231/TBS.xml
#https://radiko.jp/v3/program/station/weekly/TBS.xml


@dataclass
class arg():
  def __post_init__(self):
    self.setarg   = func.set_arg()
    self.valiable = func.gen_var(self.setarg.station_id)
    self.time     = func.time(7)
    self.vbn      = func.wsx()

    soup = abc.gen_obj.data2soup(self.valiable.url, "xml")
    find_list = soup.find_all("title", text=compile(self.setarg.search_term, flags=IGNORECASE))

    self.vbn.search_program(find_list, self.time.today_now, self.time.days_ago, self.setarg.fftt)
    self.vbn.branch(self.vbn.program_list, self.setarg.dl_flag)


@dataclass
class analyse:
  def __post_init__(self):
    self.variable = func_dow.gen_var()
    self.argment  = func_dow.check_arg()

  def dow(self):
    dy = abc.dow_yesterday(1)
    self.argment.today_list(self.variable.loaded_yaml, dy)
    self.today_list = self.argment.reserve_list

  def phrase(self):
    self.argment.series_name(self.variable.loaded_yaml, argv[1])
    self.today_list = self.argment.reserve_list


@dataclass
class download:
  def __post_init__(self):
    self.fff = func.fastforward()
    self.ooo = func_auth.oth()

  def dl(self, argclass:arg):
    self.fff.dl(self.ooo.xrat, argclass.setarg.station_id, argclass.vbn.time_ft, argclass.vbn.time_to, argclass.valiable.tmp_dir, argclass.vbn.filename)
    self.fff.enc(argclass.valiable.tmp_dir, argclass.valiable.storage_path, argclass.vbn.filename, argclass.vbn.img)

    result_1 = run(self.fff.download)
    result_2 = run(self.fff.encode)
    # print(self.fff.download)

    if result_1.returncode == 0:
      remove(f"{argclass.valiable.tmp_dir}/{argclass.vbn.filename}.m4a")

    abc.ntfy(result_2, f"{argclass.vbn.filename}.mp3")


def main():

  if       argv[1].startswith("-"):
    iop = arg()
    dldl = download()
    dldl.dl(iop)
  elif not argv[1].startswith("-"):
    jkl = analyse()

    if   argv[1] == "dow":
      jkl.dow()
    elif argv[1] != "dow":
      jkl.phrase()

    cvb = func_dow.convert_d2l(jkl.today_list)

    for ggg in cvb:
      run(ggg)

