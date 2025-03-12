
from os import getenv, remove
from re import compile, IGNORECASE
from plyer import notification
from subprocess import run
import func, func_auth
from mytool import abc


#JP+都道府県コード ex) 北海道 => JP1    沖縄 => JP47
#国土交通省 https://nlftp.mlit.go.jp/ksj/gml/codelist/PrefCd.html
#Area ID: JP8   https://radiko.jp/v3/station/list/JP8.xml
#
#https://radiko.jp/v3/program/station/date/20301231/TBS.xml
#https://radiko.jp/v3/program/station/weekly/TBS.xml


def main():

  setarg   = func.set_arg()
  linker   = func.gen_link(setarg.station_id)
  valiable = func.gen_var()
  time     = func.time(7)
  fff      = func.fastforward()
  ooo      = func_auth.oth(linker.auth1_url, linker.auth2_url, linker.authkey)

  soup = abc.makesoup(linker.url)
  find_list = soup.find_all("title", text=compile(setarg.search_term, flags=IGNORECASE))

  program_list = func.search_program(find_list, time.today_now, time.days_ago, setarg.fftt)
  time_ft, time_to, filename, img = func.branch(program_list, setarg.dl_flag)

  fff.dl(ooo.xrat, setarg.station_id, time_ft, time_to, valiable.tmp_dir, filename)
  result_1  = run(fff.download)

  fff.enc(valiable.tmp_dir, valiable.storage_path, filename, img)
  result_2  = run(fff.encode)
  # print(fff.download)


  if result_1.returncode == 0:
    remove(f"{valiable.tmp_dir}/{filename}.m4a")

  abc.ntfy(result_2, f"{filename}.mp3")


if __name__ == "__main__":
  main()
