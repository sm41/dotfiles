import func
from sys import argv, exit
from subprocess import run
from mytool import ctrl_string as cs, ctrl_path as cp

def main():
  cs.Argument.check_arg(argv[1])
  variable = func.Set_Variable()
  ccc      = func.dl()
  lp       = cp.Storage("@ph")

  if variable.parts.path == "/view_video.php":
    ccc.ytdlp(str(lp.storage_dir), argv[1])

  elif variable.parts.path.startswith(("/model", "/pornstar")):
    ccc.ytdlp(str(lp.storage_dir) + variable.parts.path, argv[1] + "/videos/upload")

  else:
    print("Invailed Argment!")
    exit()

  run(ccc.method)

