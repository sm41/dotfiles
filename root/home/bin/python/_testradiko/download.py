
class fastforward:
  def __init__(self):
    pass

  def dl(self, authtoken, dl_dict:dict):
    station_id = dl_dict['station_id']
    time_ft    = dl_dict['ft']
    time_to    = dl_dict['to']
    tmp        = dl_dict['tmp']
    title      = dl_dict['title']
    date       = dl_dict['date']

    self.ffmpeg_dl = [
      "ffmpeg",
        "-loglevel", "warning",
        "-n",
        "-headers", f"X-Radiko-Authtoken: {authtoken}",
        "-i", f"https://radiko.jp/v2/api/ts/playlist.m3u8?station_id={station_id}&l=15&ft={time_ft}&to={time_to}",
        "-codec", "copy",
      f"{tmp}/{title}_{date}.m4a"
    ]


  def enc(self, enc_dict:dict):
    storage  = enc_dict['storage']
    img      = enc_dict['img']
    tmp      = enc_dict['tmp']
    title    = enc_dict['title']
    date     = enc_dict['date']

    self.ffmpeg_enc = [
      "ffmpeg",
        "-loglevel", "warning",
        "-n",
        "-i",  f"{tmp}/{title}_{date}.m4a",
        "-i",  f"{img}",
        "-map", "0",
        "-map", "1",
        "-metadata:s:v", "title='Album cover'",
        "-metadata:s:v", "comment='Cover (Front)'",
        "-b:a", "48k",
      f"{storage}/{title}_{date}.mp3"
    ]