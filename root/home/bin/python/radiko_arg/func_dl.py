
def ffmpeg(authtoken, station_id, time_ft, time_to, path, filename):
  download = [
    "ffmpeg",
      "-loglevel", "warning",
      "-n",
      # "-fflags", "+discardcorrupt",
      "-headers", f"X-Radiko-Authtoken: {authtoken}",
      "-i", f"https://radiko.jp/v2/api/ts/playlist.m3u8?station_id={station_id}&l=15&ft={time_ft}&to={time_to}",
      "-codec", "copy",
      # "-vn",
      # "-bsf:a", "aac_adtstoasc",
      # "-movflags", "faststart",
    f"{path}/{filename}.m4a"
  ]
  return download


def encode(tmp, path, filename, img):
  encode = [
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
  return encode

