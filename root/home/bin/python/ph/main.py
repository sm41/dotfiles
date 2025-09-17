import func
from sys import argv, exit
from subprocess import run
from mytool import ctrl_string, ctrl_path

def main():
  ctrl_string.ctrl_arg.check_arg(argv[1])
  variable = func.gen_var()
  lp = ctrl_path.storage("@ph")

  if variable.parts.path == "/view_video.php":
    variable.ytdlp(str(lp.storage_dir), variable.arg)

  elif variable.parts.path.startswith(("/model", "/pornstar")):
    variable.ytdlp(str(lp.storage_dir) + variable.parts.path, variable.arg + "/videos/upload")

  else:
    print("Invailed Argment!")
    exit()

  run(variable.method)

