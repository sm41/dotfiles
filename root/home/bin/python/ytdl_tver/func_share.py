
from subprocess import run
from pathlib    import Path
from sys  import argv, exit
from yaml import load, FullLoader


def check_arg():
  if(len(argv) <= 1):
    print('You need args!')
    exit()


def anlys_path(*path_parts):
  down_dir = Path(*path_parts)
  down_dir.mkdir(parents=True, exist_ok=True)
  return down_dir


def load_yaml(*path_parts):
  filename = Path(*path_parts)
  with filename.open(mode='r') as f:
    y_data = load(f, Loader=FullLoader)
  return y_data


def get_yaml_data(loaded_yaml):

  for domain, prpty in loaded_yaml.items():
    for cnfg, series in prpty.items():
      if cnfg == 'config':
        return series


def get_ntfy_meta(url):

  get_meta_method:list = [
    "yt-dlp",
      "--print", "series",
      "--print", "episode",
      "--print", "original_url",
      url
    ]
  meta = run(get_meta_method, capture_output=True, text=True).stdout.strip()
  [ series, episode, url ] = meta.splitlines()
  return [ series, episode, url ]


