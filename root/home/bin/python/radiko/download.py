from sys import exit
import variable

class Fast_Forward:
  def __init__(self, dict:dict):
    self.station_id = dict['station_id']
    self.time_ft    = dict['ft']
    self.time_to    = dict['to']
    self.date       = dict['date']
    self.start      = variable.Time.convert_time_hhmm_no_colon(dict['start'])
    self.end        = dict['end']
    self.img        = dict['img']
    self.tmp        = dict['tmp']
    self.storage    = dict['storage']
    self.title      = dict['title']


  def dl(self, authtoken):
    self.ffmpeg_dl = [
      "ffmpeg",
        "-loglevel", "warning",
        "-n",
        "-headers", f"X-Radiko-Authtoken: {authtoken}",
        "-i", f"https://radiko.jp/v2/api/ts/playlist.m3u8?station_id={self.station_id}&l=15&ft={self.time_ft}&to={self.time_to}",
        "-codec", "copy",
      f"{self.tmp}/{self.title}_{self.date}_{self.start}.m4a"
    ]


  def select_audio_format(self, source_audio, audio_format:str):
    if   audio_format == "opus":
      codec = "libopus"
    elif audio_format == "aac":
      codec = "copy"
    else:
      exit()

    self.ffmpeg_af = [
      "ffmpeg",
        "-loglevel", "warning",
        "-n",
        "-i", source_audio,
        "-c", codec,
      f"{self.tmp}/{self.title}_{self.date}_{self.start}.{audio_format}"
    ]


  def select_container_format(self, source_audio, container_format:str):
    if container_format not in [ "mp4", "mkv" ]:
      exit()

    self.ffmpeg_cf = [
      "ffmpeg",
        "-loglevel", "warning",
        "-n",
        "-i",  source_audio,
        "-i",  self.img,
        "-map", "0",
        "-map", "1",
        "-c:a", "copy",
        "-c:v", "mjpeg",
        "-disposition:v:0", "attached_pic",
      f"{self.storage}/{self.title}_{self.date}_{self.start}.{container_format}"
    ]