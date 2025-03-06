
from pathlib    import Path
from subprocess import run
from mytool import abc


# class direct_link:
#   def __init__(self):
#     pass

#   def get_base_yaml(self, loaded_yaml):
#     self.ghq = loaded_yaml['tver']['config']

#   def get_ntfy_meta(self, url):
#     __get_metadata:list = [
#       "yt-dlp",
#         "--print", "series",
#         "--print", "episode",
#         "--print", "original_url",
#         url
#       ]
#     __meta = run(__get_metadata, capture_output=True, text=True).stdout.strip()
#     self.series, self.episode, self.url = __meta.splitlines()


class test:
  def __init__(self):
    self.__pre_series =  "series"
    self.__pre_episode = "episode"
    self.__pre_url     = "original_url"
    self.__pre_filname = "filename"
    self.__pre_id      = "id"

  def get_base_yaml(self, loaded_yaml):
    self.ghq = loaded_yaml['tver']['config']

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
        "--print",  self.__pre_id,
      url
    ]
    __ddd = run(__cmd_ytdlp, capture_output=True, text=True).stdout.strip()
    self.series, self.episode, self.url, __ppp, self.id = __ddd.splitlines()
    self.paths, self.output = Path(__ppp).parent, abc.zen2han(Path(__ppp).name)


# class oda:
#   def __init__(self):
#     pass

#   def get_path_and_filename(self, yaml_config, url, down_dir):
#     __header = yaml_config['header']
#     __cmd_ytdlp = [
#       "yt-dlp",
#         "--paths",  f"home:{down_dir}",
#         "--output", f"{__header}",
#         "--print",  "filename",
#         "--print",  "id",
#       url
#     ]
#     __ddd = run(__cmd_ytdlp, capture_output=True, text=True).stdout.strip()
#     __ppp, self.id = __ddd.splitlines()
#     self.paths, self.output = Path(__ppp).parent, abc.zen2han(Path(__ppp).name)


#   def ytdlp(self, paths, id, link):
#     self.method = [
#       "yt-dlp",
#         "--embed-subs",
#         "--paths",  str(paths),
#         "--output", f"{id}.mp4",
#       link
#     ]


def ytdlp(paths, id, link):
  method = [
    "yt-dlp",
      "--embed-subs",
      "--paths",  str(paths),
      "--output", f"{id}.mp4",
    link
  ]
  return method


# def bbb(series, episode, url, storage_path, yaml_config):
#   gfv = oda()
#   gfv.get_path_and_filename(yaml_config, url, storage_path)
#   gfv.ytdlp(gfv.paths, gfv.id, url)
#   result = run(gfv.method)
#   abc.rnm(gfv.paths, f"{gfv.id}.mp4", gfv.paths, gfv.output)
#   abc.ntfy(result, series, episode)
#   # print(gfv.method)



def ccc(series, episode, url, id, paths, output):
  method = ytdlp(paths, id, url)
  print(method)
  # result = run(method)
  # abc.rnm(paths, f"{id}.mp4", paths, output)
  # abc.ntfy(result, series, episode)
  # print(gfv.method)

