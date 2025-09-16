import func
from sys import exit
from subprocess import run
from mytool import check_any, local_path

def main():
  check_any.check_any.check_arg()
  variable = func.gen_var()
  lp = local_path.storage("@ph")

  if variable.parts.path == "/view_video.php":
    variable.ytdlp(str(lp.storage_dir), variable.arg)

  elif variable.parts.path.startswith(("/model", "/pornstar")):
    variable.ytdlp(str(lp.storage_dir) + variable.parts.path, variable.arg + "/videos/upload")

  else:
    print("Invailed Argment!")
    exit()

  run(variable.method)

