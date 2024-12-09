
# import func_main
import os

mnt_path = os.getenv("CLIENT_LOCAL_STORAGE")

def apple_podcast(target_url):
  eee = os.path.join(mnt_path, "@podcast")

  cmd_ytdlp = [
    "yt-dlp",
    "--paths",  eee,
    "--output", "[Podcast]_%(series)s_%(upload_date>%Y-%m-%d)s_%(title)s.%(ext)s",
    target_url
  ]
  return cmd_ytdlp


def megaphone_fm(target_url):
  eee = os.path.join(mnt_path, "@podcast")

  cmd_ytdlp = [
    "yt-dlp",
    "--paths",  eee,
    "--output", "[Podcast]_" + func_main.soup[0] + "_" + func_main.soup[1] + ".%(ext)s",
    target_url
  ]
  return cmd_ytdlp


def tver(target_url):
  eee = os.path.join(mnt_path, "@tver")

  cmd_ytdlp = [
    "yt-dlp",
    "--embed-subs",
    "--paths",  eee,
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

