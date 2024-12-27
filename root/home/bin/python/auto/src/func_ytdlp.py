
# import func_main
import os

def apple_podcast(target_url, download_dir):
  cmd_ytdlp = [
    "yt-dlp",
    "--paths",  f"home:{download_dir}",
    "--output", "[Podcast]_%(series)s_%(upload_date>%Y-%m-%d)s_%(title)s.%(ext)s",
    target_url
  ]
  return cmd_ytdlp


def megaphone_fm(target_url, download_dir):
  cmd_ytdlp = [
    "yt-dlp",
    "--paths",  f"home:{download_dir}",
    "--output", "[Podcast]_" + func_main.soup[0] + "_" + func_main.soup[1] + ".%(ext)s",
    target_url
  ]
  return cmd_ytdlp


def tver(target_url, download_dir):
  cmd_ytdlp = [
    "yt-dlp",
    "--embed-subs",
    "--paths",  f"home:{download_dir}",
    "--output", "[%(webpage_url_domain)s]_%(series)s_%(episode)s.%(ext)s",
    target_url
  ]
  return cmd_ytdlp

def check_dir(dirname):
  if os.path.isdir(dirname):
    pass
  else:
    os.makedirs(dirname)


def rrr(target_url, platform, storage_path):

  mnt_path = os.getenv(storage_path)

  if   platform == "apple_podcast":
    eee = os.path.join(mnt_path, "test", "@podcast")
    check_dir(eee)
    return apple_podcast(target_url, eee)

  elif platform == "megaphone_fm":
    eee = os.path.join(mnt_path, "test", "@podcast")
    check_dir(eee)
    return megaphone_fm(target_url, eee)

  elif platform == "tver":
    eee = os.path.join(mnt_path, "test", "@tver")
    check_dir(eee)
    return tver(target_url, eee)

