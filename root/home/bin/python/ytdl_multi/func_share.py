
from yaml import load, FullLoader
from pathlib  import Path
from plyer    import notification


def anlys(yaml_files_list:list, state_file_dir_str:str):

  deploy_yaml_list:list = []
  ddd = Path(state_file_dir_str)

  for picked_yaml_file in yaml_files_list:
    filename = ddd.joinpath('python', picked_yaml_file)
    with filename.open(mode='r') as f:
      y_data = load(f, Loader=FullLoader)
      deploy_yaml_list.append(y_data)
  return deploy_yaml_list


def ntfy(result, upper:str, lower:str):
  if result.returncode == 0:
    notification.notify(title = "✅ Success", message = f"{upper}\n{lower}")
  else:
    notification.notify(title = "⚠️ failed", message = f"{upper}\n{lower}")