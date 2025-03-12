
from pathlib    import Path
from subprocess import run
from mytool import abc


class test:
  def __init__(self):
    self.__pre_series  = "series"
    self.__pre_episode = "episode"
    self.__pre_url     = "original_url"
    self.__pre_filname = "filename"
    self.__pre_ext     = "ext"
    self.__pre_id      = "id"

  def get_base_yaml(self, loaded_yaml):
    self.config = loaded_yaml['tver']['_http']

  def integrate(self, url, down_dir, yaml_config):
    __header = yaml_config['header']
    __cmd_ytdlp = [
      "yt-dlp",
        "--paths",  f"home:{down_dir}",
        "--output", f"{__header}",
        "--print",  self.__pre_series,
        "--print",  self.__pre_episode,
        "--print",  self.__pre_url,
        "--print",  self.__pre_filname,
        "--print",  self.__pre_ext,
        "--print",  self.__pre_id,
      url
    ]
    __ddd = run(__cmd_ytdlp, capture_output=True, text=True).stdout.strip()
    self.series, self.episode, self.url, __ppp, self.ext, self.id = __ddd.splitlines()
    self.paths, self.output = Path(__ppp).parent, abc.ctrl_file.zen2han(Path(__ppp).stem)


def ytdlp(paths, id, ext, link):
  method = [
    "yt-dlp",
      "--embed-subs",
      "--paths",  str(paths),
      "--output", f"{id}.{ext}",
    link
  ]
  return method


def ccc(series, episode, url, ext, id, paths, output):
  method = ytdlp(paths, id, ext, url)
  # print(method)
  result = run(method)
  output = abc.byte_count(output, 245)
  # print(output)
  abc.ctrl_path.rnm(Path(paths, f"{id}.{ext}"), Path(paths, f"{output}.{ext}"))
  abc.ntfy(result, f"{series}\n{episode}")
