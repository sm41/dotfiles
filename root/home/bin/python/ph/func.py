from sys import argv
from urllib import parse


class gen_var:
  def __init__(self):
    self.arg    = argv[1]
    self.parts  = parse.urlparse(self.arg)


  def ytdlp(self, paths, url):
    self.method = [
      "yt-dlp",
        "--trim-filenames", "240",
        "--paths",  paths,
        "--output", f"[%(upload_date>%Y-%m-%d)s]_[%(id)s]_%(title)s.%(ext)s",
      url
    ]
