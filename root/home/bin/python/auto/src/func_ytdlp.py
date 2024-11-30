
import func_main
import os


mnt_env_var = "CLIENT_LOCAL_STORAGE"
podcast_dir = "/@podcast"
tver_dir    = "/@tver"

mnt_path = os.getenv(mnt_env_var)

def apple_podcast(target_url):
  cmd_ytdlp = [
    "yt-dlp",
    "--paths",  mnt_path + podcast_dir,
    "--output", "[Podcast]_%(series)s_%(upload_date>%Y-%m-%d)s_%(title)s.%(ext)s",
    target_url
  ]
  return cmd_ytdlp


def megaphone_fm(target_url):
  cmd_ytdlp = [
    "yt-dlp",
    "--paths",  mnt_path + podcast_dir,
    "--output", "[Podcast]_" + func_main.soup[0] + "_" + func_main.soup[1] + ".%(ext)s",
    target_url
  ]
  return cmd_ytdlp


def tver(target_url):
  cmd_ytdlp = [
    "yt-dlp",
    "--embed-subs",
    "--paths",  mnt_path + tver_dir,
    "--output", "[%(webpage_url_domain)s]_%(series)s_%(episode)s.%(ext)s",
    target_url
  ]
  return cmd_ytdlp



def rrr(target_url, platform):

  if   platform == "apple_podcast":
    return apple_podcast(target_url)

  elif platform == "megaphone_fm":
    return megaphone_fm(target_url)

  elif platform == "tver":
    return tver(target_url)

