import func
from subprocess import run
from sys import exit
from mytool import check_any

def main():
  check_any.check_any.check_arg()
  variable = func.Gen_Var()

  if variable.parts.path == "/view_video.php":
    variable.ytdlp(str(variable.storage_dir), variable.arg)

  elif variable.parts.path.startswith(("/model", "/pornstar")):
    variable.ytdlp(str(variable.storage_dir) + variable.parts.path, variable.arg + "/videos/upload")

  else:
    print("Invailed Argment!")
    exit()

  run(variable.method)

