
from subprocess import run
from pathlib    import Path
from sys  import argv, exit
from yaml import load, FullLoader


def check_arg():
  if(len(argv) <= 1):
    print('You need args!')
    exit()


def load_yaml(yaml_file, state_file_dir:str):
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
      "--print", meta_tag['meta_list'][0],
      "--print", meta_tag['meta_list'][1],
      "--print", meta_tag['meta_list'][2],
      url
    ]
  meta = run(get_meta_method, capture_output=True, text=True).stdout.strip()
  [ series, episode, link ] = meta.splitlines()
  return [ series, episode, link ]


