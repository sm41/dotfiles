
import urllib.parse
from sys import argv
from os  import getenv
from mytool import utils


class Gen_Var:
  def __init__(self):
    self.arg          = argv[1]
    __download_dir    = getenv("CLIENT_NETWORK_STORAGE_misc")
    self.storage_dir  = utils.Ctrl_Path.anlys_path(__download_dir, "@ph")
    self.parts        = urllib.parse.urlparse(self.arg)


  def ytdlp(self, paths, url):
    self.method = [
      "yt-dlp",
        "--trim-filenames", "240",
        "--paths",  paths,
        "--output", f"[%(upload_date>%Y-%m-%d)s]_[%(id)s]_%(title)s.%(ext)s",
      url
    ]
