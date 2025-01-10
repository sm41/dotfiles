# import os
from pathlib import Path

def apple_podcast(url, download_dir):
  cmd_ytdlp = [
    "yt-dlp",
    "--paths",  f"home:{download_dir}",
    "--output", "[Podcast]_%(series)s_%(upload_date>%Y-%m-%d)s_%(title)s.%(ext)s",
    url
  ]
  return cmd_ytdlp


def tver(url, download_dir):
  cmd_ytdlp = [
    "yt-dlp",
    "--embed-subs",
    "--paths",  f"home:{download_dir}",
    "--output", "[%(webpage_url_domain)s]_%(series)s_%(episode)s.%(ext)s",
    url
  ]
  return cmd_ytdlp


def ph_view(url, download_dir):
  cmd_ytdlp = [
    "yt-dlp",
    "--paths",  f"home:{download_dir}",
    "--output", "[%(upload_date>%Y-%m-%d)s]_[%(id)s]_%(title)s.%(ext)s",
    url
  ]
  return cmd_ytdlp


def ph_cat(url, download_dir, archive_dir):
  cmd_ytdlp = [
    "yt-dlp",
    "--download-archive",    archive_dir,
    "--paths",               f"home:{download_dir}",
    "--output",              "[%(upload_date>%Y-%m-%d)s]_[%(id)s]_%(title)s.%(ext)s",
    url
  ]
  return cmd_ytdlp


def none(url, download_dir):
  cmd_ytdlp = [
    "yt-dlp",
    "--embed-subs",
    "--paths",  f"home:{download_dir}",
    url
  ]
  return cmd_ytdlp


def check_dir(dirname:Path):
  if dirname.is_dir():
    pass
  else:
    dirname.mkdir()



# ppp = Path("hogefuga", "piyopiyo")
# ppp.mkdir(parents=True, exist_ok=True)
# print(type(ppp))
# hhh = Path(ppp, 'uuu.txt')
# hhh.touch(exist_ok=True)


def vvv(yaml_data_dict:dict, ntfy_meta_dict:dict, storage_path:str, state_file_dir_str:str):

  down_dir = Path(storage_path, "test", yaml_data_dict["child_dir"])
  down_dir.mkdir(parents=True, exist_ok=True)

  if   yaml_data_dict["platform"] == "apple_podcast":
    return apple_podcast(ntfy_meta_dict["link"], down_dir)

  elif yaml_data_dict["platform"] == "tver":
    return tver(ntfy_meta_dict["link"], down_dir)

  elif yaml_data_dict["platform"] == "ph_view":
    return ph_view(ntfy_meta_dict["link"], down_dir)

  elif yaml_data_dict["platform"] == "ph_cat":
    ctgry, actor = yaml_data_dict['path_tuple'][1], yaml_data_dict['path_tuple'][2]

    kmkm = down_dir.joinpath(ctgry, actor)
    kmkm.mkdir(parents=True, exist_ok=True)
    archive_dir = Path(state_file_dir_str, "yt-dlp", "ph", ctgry, actor)
    archive_dir.touch(exist_ok=True)

    return ph_cat(ntfy_meta_dict["link"], str(kmkm), str(archive_dir))

  elif yaml_data_dict["platform"] == None:
    return none(ntfy_meta_dict["link"], down_dir)