
from subprocess import run
from pathlib    import Path
from sys  import argv, exit
from yaml import load, FullLoader


def check_arg():
  if(len(argv) <= 1):
    print('You need args!')
    exit()


def anlys_path(download_path):
  down_dir = Path(download_path, "@tver")
  down_dir.mkdir(parents=True, exist_ok=True)
  return down_dir


def load_yaml(yaml_file, state_file_dir):
  filename = Path(state_file_dir, 'python', yaml_file)
  with filename.open(mode='r') as f:
    y_data = load(f, Loader=FullLoader)
  return y_data


def get_yaml_data(loaded_yaml):

  for domain, prpty in loaded_yaml.items():
    for cnfg, series in prpty.items():
      if cnfg == 'config':
        return series


def get_ntfy_meta(url:str, meta_tag:dict):

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


