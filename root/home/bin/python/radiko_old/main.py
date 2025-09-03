
from os import remove
from re import compile, IGNORECASE
from subprocess import run
import func, func_auth
from mytool import utils
from sys import argv
import __main__


#JP+都道府県コード ex) 北海道 => JP1    沖縄 => JP47
#国土交通省 https://nlftp.mlit.go.jp/ksj/gml/codelist/PrefCd.html
#Area ID: JP8   https://radiko.jp/v3/station/list/JP8.xml
#
#https://radiko.jp/v3/program/station/date/20301231/TBS.xml
#https://radiko.jp/v3/program/station/weekly/TBS.xml


def main():

  setarg   = func.Set_Arg()
  valiable = func.Gen_Var(setarg.station_id)
  time     = func.Time(7)
  fff      = func.Fastforward()
  ooo      = func_auth.Oth()
  vbn      = func.Wsx()

  soup = utils.Gen_Obj.data2soup(valiable.url, "xml")
  find_list = soup.find_all("title", text=compile(setarg.search_term, flags=IGNORECASE))

  vbn.search_program(find_list, time.today_now, time.days_ago, setarg.fftt)
  vbn.branch(vbn.program_list, setarg.dl_flag)

  fff.dl(ooo.xrat, setarg.station_id, vbn.time_ft, vbn.time_to, valiable.tmp_dir, vbn.filename)
  fff.enc(valiable.tmp_dir, valiable.storage_path, vbn.filename, vbn.img)

  result_1 = run(fff.download)
  result_2 = run(fff.encode)
  # print(fff.download)

  if result_1.returncode == 0:
    remove(f"{valiable.tmp_dir}/{vbn.filename}.m4a")

  utils.ntfy(result_2, f"{vbn.filename}.mp3")

