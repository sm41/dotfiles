from argparse import ArgumentParser
# from plyer  import notification
# from sys import exit
from mytool import utils


class set_arg:
  s_dict = {
    "TBS":     "TBSラジオ",
    "QRR":     "文化放送",
    "LFR":     "ニッポン放送",
    "RN1":     "ラジオNIKKEI第1",
    "RN2":     "ラジオNIKKEI第2",
    "INT":     "interfm",
    "FMT":     "tokyo fm",
    "FMJ":     "j-wave",
    "IBS":     "LuckyFM 茨城放送",
    "JORF":    "ラジオ日本",
    "BAYFM78": "bayfm",
    "NACK5":   "nack5",
    "YFM":     "fm yokohama",
    "JOAK":    "NHKラジオ第1（東京）",
    "JOAK-FM": "NHK-FM（東京）",
  }

  def __init__(self):
    __parser = ArgumentParser()
    __parser.add_argument('-s',   help='station_id',  required=True,   type=str.upper, choices = self.s_dict.keys())
    __parser.add_argument('-t',   help='title',       required=True,   type=str)
    __parser.add_argument('-ft',  help='ft',          required=False,  type=str)
    __parser.add_argument('-dl',  help='download',    required=False,  action='store_true')

    __opt_args       = __parser.parse_args()
    self.station_id  = __opt_args.s.upper()
    self.search_term = __opt_args.t
    self.fftt        = __opt_args.ft
    self.dl_flag     = __opt_args.dl
    self.url         = f"https://radiko.jp/v3/program/station/weekly/{self.station_id}.xml"


class icpo:
  program_list = []

  def search_program(self, station_id, find_list, today_now, days_ago, tmp, storage):

    for keyword in find_list:
      prog_detail = keyword.parent
      if   days_ago >  prog_detail.attrs['to'] >  today_now:
        continue
      elif days_ago <= prog_detail.attrs['to'] <= today_now:
        ddd = {
          "station_id":  station_id,
          "ft":          prog_detail.attrs['ft'],
          "to":          prog_detail.attrs['to'],
          "date":     f"{prog_detail.attrs['ft'][0:4]}-{prog_detail.attrs['ft'][4:6]}-{prog_detail.attrs['ft'][6:8]}",
          "img":      prog_detail.img.string,
          'tmp':      tmp,
          'storage':  storage,
          "title":    utils.Ctrl_File.zen2han(prog_detail.title.string),
        }
        self.program_list.append(ddd)


  # def branch(self, program_list, dl_flag):

  #   if len(program_list) == 1:
  #     if dl_flag:
  #       self.time_ft  = program_list[0]['ft']
  #       self.time_to  = program_list[0]['to']
  #       self.filename = f"{program_list[0]['title']}_{program_list[0]['time']}"
  #       self.img      = program_list[0]['img']
  #     else:
  #       print(program_list)
  #       print("✅ You can download it by adding '-dl' flag")
  #       exit()
  #   else:
  #     if dl_flag:
  #       notification.notify(title = "⚠️ failed",  message = "Not One")
  #     elif program_list:
  #       for vvv in program_list:
  #         print(vvv)
  #       print(f"📢 Result {len(program_list)} Programs")
  #     else:
  #       print("⚠️ Program is Not Found !!")
  #     exit()

