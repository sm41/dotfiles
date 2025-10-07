from sys import argv
from urllib import parse


class Set_Variable:
  def __init__(self):
    self.parts  = parse.urlparse(argv[1])


class dl:
  def ytdlp(self, paths, url):
    self.method = [
      "yt-dlp",
        "--trim-filenames", "240",
        "--paths",  paths,
        "--output", f"[%(upload_date>%Y-%m-%d)s]_[%(id)s]_%(title)s.%(ext)s",
      url
    ]
