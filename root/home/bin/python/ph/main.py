import func
from sys import argv, exit
from subprocess import run
from mytool import ctrl_string, ctrl_path

def main():
  ctrl_string.Ctrl_Arg.check_arg(argv[1])
  variable = func.gen_var()
  lp = ctrl_path.Storage("@ph")

  if variable.parts.path == "/view_video.php":
    variable.ytdlp(str(lp.storage_dir), argv[1])

  elif variable.parts.path.startswith(("/model", "/pornstar")):
    variable.ytdlp(str(lp.storage_dir) + variable.parts.path, argv[1] + "/videos/upload")

  else:
    print("Invailed Argment!")
    exit()

  run(variable.method)

