
from pathlib    import Path
from subprocess import run
from plyer  import notification


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
  paths, output = Path(ppp).parent, Path(ppp).name

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


def rnm(paths, output, id):
  oldpath = Path(paths, f"{id}.mp4")
  newpath = Path(paths, output)
  oldpath.rename(newpath)


def ntfy(result, upper:str, lower:str):
  if result.returncode == 0:
    notification.notify(title = "✅ Success", message = f"{upper}\n{lower}")
  else:
    notification.notify(title = "⚠️ failed", message = f"{upper}\n{lower}")


def bbb(seu_list, storage_path, yaml_config):
  ulu_dict          = mix(seu_list)
  paths, output, id = get_path_and_filename(yaml_config, ulu_dict, storage_path)
  method            = ytdlp(paths, id, ulu_dict['url'])
  result            = run(method)
  rnm(paths, output, id)
  ntfy(result, ulu_dict["upper"], ulu_dict["lower"])
  # print(method)

