
import urllib.parse
from sys import argv
from os  import getenv
from mytool import abc

class gen_var:
  def __init__(self):
    self.arg            = argv[1]
    self.download_dir   = getenv("CLIENT_NETWORK_STORAGE_misc")
    self.storage_dir    = abc.ctrl_path.anlys_path(self.download_dir, "@ph")
    self.parts          = urllib.parse.urlparse(self.arg)


def ytdlp(paths, url):
  method = [
    "yt-dlp",
      "--trim-filenames", "245",
      "--paths",  paths,
      "--output", f"[%(upload_date>%Y-%m-%d)s]_[%(id)s]_%(title)s.%(ext)s",
    url
  ]
  return method
