
from yaml import load, FullLoader
from pathlib  import Path
from plyer    import notification
from sys  import argv, exit


def check_arg():
  if(len(argv) <= 1):
    print('You need args!')
    exit()


def anlys(yaml_files_list:list, state_file_dir_str:str):

  deploy_yaml_list:list = []
  ddd = Path(state_file_dir_str)

  for picked_yaml_file in yaml_files_list:
    filename = ddd.joinpath('python', picked_yaml_file)
    with filename.open(mode='r') as f:
      y_data = load(f, Loader=FullLoader)
      deploy_yaml_list.append(y_data)
  return deploy_yaml_list


def mix(series, episode, link):
  key_data:list   = [ "upper", "lower", "link" ]
  value_data:list = [ series, episode, link ]
  mix_dict:dict = dict(zip(key_data, value_data))

  return mix_dict


def ntfy(result, upper:str, lower:str):
  if result.returncode == 0:
    notification.notify(title = "✅ Success", message = f"{upper}\n{lower}")
  else:
    notification.notify(title = "⚠️ failed", message = f"{upper}\n{lower}")