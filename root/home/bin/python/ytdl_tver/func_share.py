
from subprocess import run
from sys  import argv, exit


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


