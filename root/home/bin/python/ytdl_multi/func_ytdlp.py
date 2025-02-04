from pathlib import Path


def sshhrr(paths, id, ext, link):
  cmd_ytdlp = [
    "yt-dlp",
      "--embed-subs",
      "--paths",  paths,
      "--output", f"{id}.{ext}",
    link
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


def vvv(yaml_data_dict, ntfy_meta_dict, paths, id, ext):

  if   yaml_data_dict["platform"] == "apple_podcast" or "tver" or "ph_view" or None:
    return sshhrr(paths, id, ext, ntfy_meta_dict['link'])

  # elif yaml_data_dict["platform"] == "ph_cat":
  #   ctgry = yaml_data_dict['path_tuple'][1]
  #   actor = yaml_data_dict['path_tuple'][2]

  #   kmkm = paths.joinpath(ctgry, actor)
  #   kmkm.mkdir(parents=True, exist_ok=True)

  #   archive_dir = Path(state_file_dir_str, "yt-dlp", "ph", ctgry, actor)
  #   archive_dir.touch(exist_ok=True)

  #   return ph_cat(ntfy_meta_dict["link"], str(kmkm), str(archive_dir))

  # elif yaml_data_dict["platform"] == None:
  #   return none(paths, ntfy_meta_dict['link'])