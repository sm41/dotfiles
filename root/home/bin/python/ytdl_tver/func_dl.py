
from pathlib    import Path
from subprocess import run
from mytool import abc


def mix(value):
  key_data   = [ "upper", "lower", "url" ]
  value_data = value
  ulu_dict   = dict(zip(key_data, value_data))
  return ulu_dict


def get_path_and_filename(yaml_config:dict, sel_dict:dict, down_dir:str):

  header = yaml_config['header']
  link   = sel_dict['url']

  cmd_ytdlp = [
    "yt-dlp",
      "--paths",  f"home:{down_dir}",
      "--output", f"{header}",
      "--print",  "filename",
      "--print",  "id",
    link
  ]
  ddd = run(cmd_ytdlp, capture_output=True, text=True).stdout.strip()
  ppp, id = ddd.splitlines()
  paths, output = Path(ppp).parent,   abc.zen2han(Path(ppp).name)

  return paths, output, id


def ytdlp(paths, id, link):
  cmd_ytdlp = [
    "yt-dlp",
      "--embed-subs",
      "--paths",  str(paths),
      "--output", f"{id}.mp4",
    link
  ]
  return cmd_ytdlp


def bbb(seu_list, storage_path, yaml_config):
  ulu_dict          = mix(seu_list)
  paths, output, id = get_path_and_filename(yaml_config, ulu_dict, storage_path)
  method            = ytdlp(paths, id, ulu_dict['url'])
  # result            = run(method)
  # abc.rnm(paths, f"{id}.mp4", paths, output)
  # abc.ntfy(result, ulu_dict["upper"], ulu_dict["lower"])
  print(method)

