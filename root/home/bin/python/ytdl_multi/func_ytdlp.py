from pathlib import Path
import os


def sshhrr(paths, id, ext, link):
  cmd_ytdlp = [
    "yt-dlp",
      "--embed-subs",
      "--paths",  paths,
      "--output", f"{id}.{ext}",
    link
  ]
  return cmd_ytdlp


def ph_cat(archive_dir, paths, output, link):
  cmd_ytdlp = [
    "yt-dlp",
      "--download-archive",   archive_dir,
      "--paths",              paths,
      "--output",             output,
    link
  ]
  return cmd_ytdlp


def vvv(yaml_data_dict, ntfy_meta_dict, paths, output, id, ext):

  if   yaml_data_dict["platform"] == "apple_podcast" or "tver" or "ph_view":
    return sshhrr(paths, id, ext, ntfy_meta_dict['link'])

  # elif yaml_data_dict["platform"] == ("ph_cat"):
    # ctgry = yaml_data_dict['path_tuple'][1]
    # actor = yaml_data_dict['path_tuple'][2]

    # kmkm = Path(paths)
    # lll = Path(*yaml_data_dict['path_tuple'])
    # aaa = kmkm.joinpath(Path(*yaml_data_dict['path_tuple']))
    # kmkm.mkdir(parents=True, exist_ok=True)
    # print(kmkm)

    # archive_dir = Path(state_file_dir_str, "yt-dlp", "ph", ctgry, actor)
    # archive_dir.touch(exist_ok=True)
    # return yaml_data_dict["platform"]
    # return ph_cat(str(kmkm), str(kmkm), output, ntfy_meta_dict['link'])
