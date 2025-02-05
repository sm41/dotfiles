
from yaml import load, FullLoader
from func_ytdlp  import vvv
from subprocess import run
# from pathlib  import Path
from plyer    import notification
from sys import argv, exit
from os  import path, rename, makedirs


def check_arg():
  if(len(argv) <= 1):
    print('You need args!')
    exit()


# def anlys(yaml_files_list:list, state_file_dir_str:str):

#   deploy_yaml_list:list = []
#   ddd = Path(state_file_dir_str)

#   for picked_yaml_file in yaml_files_list:
#     filename = ddd.joinpath('python', picked_yaml_file)
#     with filename.open(mode='r') as f:
#       y_data = load(f, Loader=FullLoader)
#       deploy_yaml_list.append(y_data)
#   return deploy_yaml_list

def anlys(yaml_files_list:list, state_file_dir_str:str):

  deploy_yaml_list:list = []

  for picked_yaml_file in yaml_files_list:
    filename = path.join(state_file_dir_str, 'python', picked_yaml_file)
    with open(filename, mode='r') as f:
      y_data = load(f, Loader=FullLoader)
      deploy_yaml_list.append(y_data)
  return deploy_yaml_list


# def anlys_path(download_path, yaml_data_dict):
#   down_dir = Path(download_path, yaml_data_dict["child_dir"])
#   down_dir.mkdir(parents=True, exist_ok=True)
#   return down_dir


def anlys_path(download_path, yaml_data_dict):
  down_dir = path.join(download_path, yaml_data_dict["child_dir"])
  makedirs(down_dir, exist_ok=True)
  return down_dir


def mix(series:str, episode:str, link:str):
  key_data   = [ "upper", "lower", "link" ]
  value_data = [ series, episode, link ]
  mix_dict   = dict(zip(key_data, value_data))
  return mix_dict


def ntfy(result, upper:str, lower:str):
  if result.returncode == 0:
    notification.notify(title = "✅ Success", message = f"{upper}\n{lower}")
  else:
    notification.notify(title = "⚠️ failed", message = f"{upper}\n{lower}")


def get_path_and_filename(yaml_data_dict:dict, ntfy_meta_dict:dict, down_dir:str):

  if ('playlist' in yaml_data_dict) and (yaml_data_dict['playlist'] == True):
    paths  = down_dir
    output = yaml_data_dict['header']
    id     = None
    ext    = None

  elif ('playlist' not in yaml_data_dict) or (yaml_data_dict['playlist'] == False):
    header = yaml_data_dict['header']
    link   = ntfy_meta_dict['link']

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
    paths, output = path.split(ppp)

  return paths, output, id, ext


def rnm(paths, output, id, ext):
  oldpath = path.join(paths, f"{id}.{ext}")
  newpath = path.join(paths, output)
  rename(oldpath, newpath)


def bbb(series, episode, link, download_path_str, yaml_data_dict):
  ntfy_meta_dict         = mix(series, episode, link)
  down_dir               = anlys_path(download_path_str, yaml_data_dict)
  paths, output, id, ext = get_path_and_filename(yaml_data_dict, ntfy_meta_dict, down_dir)
  method                 = vvv(yaml_data_dict, ntfy_meta_dict, paths, output, id, ext)
  result                 = run(method)
  rnm(paths, output, id, ext)
  ntfy(result, ntfy_meta_dict["upper"], ntfy_meta_dict["lower"])
  # print(method)