import func_main
import os


MNT_ENV_VAR = "CLIENT_LOCAL_STORAGE"
PODCAST_DIR = "/@podcast"
TVER_DIR    = "/@tver"

MNT_PATH = os.getenv(MNT_ENV_VAR)

def apple_podcast(target_url):
  cmd_ytdlp = [
    "yt-dlp",
    "--paths",  MNT_PATH + PODCAST_DIR,
    "--output", "[Podcast]_%(series)s_%(upload_date>%Y-%m-%d)s_%(title)s.%(ext)s",
    target_url
  ]
  return cmd_ytdlp


def megaphone_fm(target_url):
  cmd_ytdlp = [
    "yt-dlp",
    "--paths",  MNT_PATH + PODCAST_DIR,
    "--output", "[Podcast]_" + func_main.soup[0] + "_" + func_main.soup[1] + ".%(ext)s",
    target_url
  ]
  return cmd_ytdlp


def tver(target_url):
  cmd_ytdlp = [
    "yt-dlp",
    "--embed-subs",
    "--paths",  MNT_PATH + TVER_DIR,
    "--output", "[%(webpage_url_domain)s]_%(series)s_%(episode)s.%(ext)s",
    target_url
  ]
  return cmd_ytdlp



def ooo(target_url, platform):

  if   platform == "apple_podcast":
    return apple_podcast(target_url)

  elif platform == "megaphone_fm":
    return megaphone_fm(target_url)

  elif platform == "tver":
    return tver(target_url)

