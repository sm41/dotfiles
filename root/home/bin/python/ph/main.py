
import func
from subprocess import run
from sys import exit

def main():
  variable = func.gen_var()

  if variable.parts.path == "/view_video.php":
    method = func.ytdlp(str(variable.storage_dir), variable.arg)
  elif variable.parts.path.startswith(("/model", "/pornstar")):
    method = func.ytdlp(str(variable.storage_dir) + variable.parts.path, variable.arg + "/videos/upload")
  else:
    exit("Invailed Argment!")

  run(method)


if __name__ == "__main__":
  main()