from sys import exit
import variable


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
    start      = variable.time.convert_time_hhmm_no_colon(dl_dict['start'])

    self.ffmpeg_dl = [
      "ffmpeg",
        "-loglevel", "warning",
        "-n",
        "-headers", f"X-Radiko-Authtoken: {authtoken}",
        "-i", f"https://radiko.jp/v2/api/ts/playlist.m3u8?station_id={station_id}&l=15&ft={time_ft}&to={time_to}",
        "-codec", "copy",
      f"{tmp}/{title}_{date}_{start}.m4a"
    ]


  def select_audio_format(self, source_audio, enc_dict:dict, audio_format:str):
    tmp    = enc_dict['tmp']
    title  = enc_dict['title']
    date   = enc_dict['date']
    start  = variable.time.convert_time_hhmm_no_colon(enc_dict['start'])

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
      f"{tmp}/{title}_{date}_{start}.{audio_format}"
    ]


  def select_container_format(self, source_audio, enc_dict:dict, container_format:str):
    storage  = enc_dict['storage']
    img      = enc_dict['img']
    title    = enc_dict['title']
    date     = enc_dict['date']
    start    = variable.time.convert_time_hhmm_no_colon(enc_dict['start'])

    if container_format == "mp4" or container_format == "mkv":
      pass
    else:
      exit()

    self.ffmpeg_cf = [
      "ffmpeg",
        "-loglevel", "warning",
        "-n",
        "-i",  source_audio,
        "-i",  f"{img}",
        "-map", "0",
        "-map", "1",
        "-c:a", "copy",
        "-c:v", "mjpeg",
        "-disposition:v:0", "attached_pic",
      f"{storage}/{title}_{date}_{start}.{container_format}"
    ]

