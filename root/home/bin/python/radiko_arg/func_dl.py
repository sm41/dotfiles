
class fastforward:
  def __init__(self):
    pass

  def dl(self, authtoken, station_id, time_ft, time_to, path, filename):
    self.download = [
      "ffmpeg",
        "-loglevel", "warning",
        "-n",
        "-headers", f"X-Radiko-Authtoken: {authtoken}",
        "-i", f"https://radiko.jp/v2/api/ts/playlist.m3u8?station_id={station_id}&l=15&ft={time_ft}&to={time_to}",
        "-codec", "copy",
      f"{path}/{filename}.m4a"
    ]

  def enc(self, tmp, path, filename, img):
    self.encode = [
      "ffmpeg",
        "-loglevel", "warning",
        "-n",
        "-i",  f"{tmp}/{filename}.m4a",
        "-i",  f"{img}",
        "-map", "0",
        "-map", "1",
        "-metadata:s:v", "title='Album cover'",
        "-metadata:s:v", "comment='Cover (Front)'",
        "-b:a", "48k",
      f"{path}/{filename}.mp3"
    ]