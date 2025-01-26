from pathlib import Path


def sshhrr(dict, dict2, download_dir):
  cmd_ytdlp = [
    "yt-dlp",
    "--embed-subs",
    "--paths",  f"home:{download_dir}",
    "--output", f"{dict2['header']}",
    dict['link']
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


def none(dict, download_dir):
  cmd_ytdlp = [
    "yt-dlp",
    "--embed-subs",
    "--paths",  f"home:{download_dir}",
    dict['link']
  ]
  return cmd_ytdlp


def vvv(yaml_data_dict:dict, ntfy_meta_dict:dict, storage_path:str, state_file_dir_str:str):

  down_dir = Path(storage_path, "test", yaml_data_dict["child_dir"])
  down_dir.mkdir(parents=True, exist_ok=True)

  if   yaml_data_dict["platform"] == "apple_podcast" or "tver" or "ph_view":
    return sshhrr(ntfy_meta_dict, yaml_data_dict, down_dir)

  elif yaml_data_dict["platform"] == "ph_cat":
    ctgry = yaml_data_dict['path_tuple'][1]
    actor = yaml_data_dict['path_tuple'][2]

    kmkm = down_dir.joinpath(ctgry, actor)
    kmkm.mkdir(parents=True, exist_ok=True)

    archive_dir = Path(state_file_dir_str, "yt-dlp", "ph", ctgry, actor)
    archive_dir.touch(exist_ok=True)

    return ph_cat(ntfy_meta_dict["link"], str(kmkm), str(archive_dir))

  elif yaml_data_dict["platform"] == None:
    return none(ntfy_meta_dict, down_dir)