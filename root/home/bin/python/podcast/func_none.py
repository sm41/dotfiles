

def get_today_list(y_data, y_dow_str):

  eee = []

  for platform, mmm in y_data.items():
    for cntnt, zzz in mmm.items():
      for ppp in zzz['plan']:
        if ppp['dow'] == y_dow_str:
          kkk = {
            **zzz,
            "plan": ppp
          }
          eee.append(kkk)
  return eee


def yui(y_data, args):

  eee = []

  for platform, mmm in y_data.items():
    for cntnt, zzz in mmm.items():
      if cntnt == args:
        kkk = {
          **zzz,
          "plan": zzz['plan'][0]
        }
        eee.append(kkk)
  return eee


def dl(qqq, tmp_dir):

  url = qqq['url']
  img = qqq['img']
  filename = qqq['name']

  download = [
    "ffmpeg",
      "-loglevel", "warning",
      "-i",   url,
      "-i",   img,
      "-map", "0:a",
      "-map", "1:v",
      "-metadata:s:v", "title='Album cover'",
      "-metadata:s:v", "comment='Cover (Front)'",
      "-codec", "copy",
    f"{tmp_dir}/{filename}"
  ]

  return download






















