
from pathlib    import Path
from subprocess import run
from plyer  import notification


def mix(value):
  key_data   = [ "upper", "lower", "url" ]
  value_data = value
  ulu_dict   = dict(zip(key_data, value_data))
  return ulu_dict



def anlys_path(download_path, yaml_config):
  down_dir = Path(download_path, yaml_config["child_dir"])
  down_dir.mkdir(parents=True, exist_ok=True)
  return down_dir


def get_path_and_filename(yaml_config:dict, sel_dict:dict, down_dir:str):

  header = yaml_config['header']
  link   = sel_dict['url']

  cmd_ytdlp = [
    "yt-dlp",
      "--paths",  f"home:{down_dir}",
      "--output", f"{header}",
      "--print",  "filename",
      "--print",  "id",
      "--print",  "ext",
    link
  ]
  ddd = run(cmd_ytdlp, capture_output=True, text=True).stdout.strip()
  ppp, id, ext = ddd.splitlines()
  paths, output = Path(ppp).parent, Path(ppp).name

  return paths, output, id, ext



def ytdlp(paths, id, ext, link):
  cmd_ytdlp = [
    "yt-dlp",
      "--embed-subs",
      "--paths",  str(paths),
      "--output", f"{id}.{ext}",
    link
  ]
  return cmd_ytdlp


def rnm(paths, output, id, ext):
  oldpath = Path(paths, f"{id}.{ext}")
  newpath = Path(paths, output)
  oldpath.rename(newpath)


def ntfy(result, upper:str, lower:str):
  if result.returncode == 0:
    notification.notify(title = "✅ Success", message = f"{upper}\n{lower}")
  else:
    notification.notify(title = "⚠️ failed", message = f"{upper}\n{lower}")


def bbb(sel_list, download_path, yaml_config):
  ulu_dict               = mix(sel_list)
  down_dir               = anlys_path(download_path, yaml_config)
  paths, output, id, ext = get_path_and_filename(yaml_config, ulu_dict, down_dir)
  method                 = ytdlp(paths, id, ext, ulu_dict['url'])
  result                 = run(method)
  rnm(paths, output, id, ext)
  ntfy(result, ulu_dict["upper"], ulu_dict["lower"])
  # print(method)

