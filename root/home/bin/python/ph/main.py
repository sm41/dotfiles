
import func
from subprocess import run
from mytool import abc
from sys import exit

def main():
  abc.Check_Any.check_arg()
  variable = func.GenVar()

  if variable.parts.path == "/view_video.php":
    variable.ytdlp(str(variable.storage_dir), variable.arg)

  elif variable.parts.path.startswith(("/model", "/pornstar")):
    variable.ytdlp(str(variable.storage_dir) + variable.parts.path, variable.arg + "/videos/upload")

  else:
    exit("Invailed Argment!")

  run(variable.method)

