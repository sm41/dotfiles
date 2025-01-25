
from pathlib  import Path
from urllib.parse import urlparse
from subprocess   import run


def out_yaml_data(url:str, deploy_yaml_list:list):

  url_parsed_tuple = urlparse(url)
  path_directory = Path(url_parsed_tuple.path)

  for vvv in deploy_yaml_list:
    for domain, path in vvv.items():
      if url_parsed_tuple.hostname.endswith(domain):
        for prprty, dict in path.items():
          if 'parts' in str(dict):
            for mmm in dict['parts']:
              if mmm in str(path_directory):
                meta_dict = {
                  "platform":   dict['platform'],
                  "child_dir":  path['child_dir'],
                  "meta_list":  path['meta_list'],
                  "playlist":   dict['playlist'],
                  "path_tuple": path_directory.parts,
                  }
  return meta_dict


def out_ntfy_meta(url:str, meta_tag:dict):

  if meta_tag['playlist']:
    series, episode, link = "hoge", "fuga", url
  else:
    get_meta_method = [
      "yt-dlp",
        "--print", meta_tag['meta_list'][0],
        "--print", meta_tag['meta_list'][1],
        "--print", meta_tag['meta_list'][2],
        url
      ]
    meta = run(get_meta_method, capture_output=True, text=True).stdout
    series, episode, link = meta.splitlines()

  return series, episode, link