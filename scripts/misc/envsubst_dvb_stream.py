#!/usr/bin/env python3

import os
import re
import subprocess
import sys
from pathlib import Path

def git_toplevel(script_dir):
    return [ "git", "-C", script_dir, "rev-parse", "--show-toplevel" ]

def search_text(file_path, pattern):
    text    = Path(file_path).read_text(encoding="utf-8")
    matches = re.findall(pattern, text)
    return list(dict.fromkeys(matches))

def main():

    SCRIPT_DIR        = Path(__file__).parent
    GIT_TOPLEVEL      = Path(subprocess.run(git_toplevel(SCRIPT_DIR), capture_output=True, text= True).stdout.strip())
    FHS_ROOT_DIR      = Path("root/home")

    GENERATE_FILENAME = "dvb_stram.m3u"
    TEMPLATE_FILENAME = GENERATE_FILENAME + ".template"

    TEMPLATE_PATH     = Path.home() / TEMPLATE_FILENAME
    GENERATE_PATH     = Path.home() / GENERATE_FILENAME

    # TEMPLATE_PATH = GIT_TOPLEVEL / FHS_ROOT_DIR / TEMPLATE_FILENAME
    # GENERATE_PATH = Path.home() / "XDG_USER_DIRS/Desktop" / GENERATE_FILENAME

    if TEMPLATE_PATH.exists():
        print("File is exist")
        print(TEMPLATE_PATH)
        print(GENERATE_PATH)
    else:
        print("No such file")
        sys.exit()

    sys.exit()

    required_env = search_text(TEMPLATE_PATH, r"\$\{([^}]+)\}")
    check_var = {}

    for env in required_env:
        if os.getenv(env):
            check_var[env] = True
        else:
            check_var[env] = False

    if check_var:
        print(check_var)
    else:
        print("check_var is empty")
        sys.exit()

    if all(check_var.values()):
        print("all ok")

        template  = TEMPLATE_PATH.read_text()
        generated = os.path.expandvars(template)
        GENERATE_PATH.write_text(generated)

    else:
        print("check_var is empty")
        sys.exit()

if __name__ == '__main__':
    main()