
from os import getenv, remove
from re import compile, IGNORECASE
from plyer import notification
from subprocess import run
import func, func_auth, func_dl
from mytool import abc


#JP+都道府県コード ex) 北海道 => JP1    沖縄 => JP47
#国土交通省 https://nlftp.mlit.go.jp/ksj/gml/codelist/PrefCd.html
#Area ID: JP8   https://radiko.jp/v3/station/list/JP8.xml
#
#https://radiko.jp/v3/program/station/date/20301231/TBS.xml
#https://radiko.jp/v3/program/station/weekly/TBS.xml


def main():

  chkarg   = func.check_arg()
  valiable = func.gen_var()
  time     = func.time(7)
  fff      = func_dl.fastforward()



  soup = abc.makesoup(url)
  find_list = soup.find_all("title", text=compile(chkarg.search_term, flags=IGNORECASE))
  program_list = func.search_program(find_list, time.today_now, time.days_ago, chkarg.fftt)
  time_ft, time_to, filename, img = func.branch(program_list, chkarg.dl_flag)

  # authtoken = func_auth.auth(auth1_url, auth2_url, authkey)
  ooo = func_auth.oth(auth1_url, auth2_url, authkey)

  fff.dl(ooo.xat, chkarg.station_id, time_ft, time_to, valiable.tmp_dir, filename)
  result_1  = run(fff.download)

  fff.enc(valiable.tmp_dir, valiable.storage_path, filename, img)
  result_2  = run(fff.encode)
  # print(fff.download)


  if result_1.returncode == 0:
    remove(f"{valiable.tmp_dir}/{filename}.m4a"),
  else:
    pass

  if result_2.returncode == 0:
    notification.notify(title = "✅ Success", message = f"{filename}.mp3"),
  else:
    notification.notify(title = "⚠️ failed",  message = f"{filename}.mp3")


if __name__ == "__main__":
  main()
