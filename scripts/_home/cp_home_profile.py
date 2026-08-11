#!/usr/bin/env python3


import subprocess
from pathlib import Path


def git_toplevel(script_dir):
    return [ "git", "-C", script_dir, "rev-parse", "--show-toplevel" ]

def bbb(temp_path, user_profile):
    return [ "cp", "-f", "-b", "--suffix=_`date +%Y%m%d_%H%M`",  f"{temp_path}/sample{user_profile}",  Path.home() / user_profile ]

def sss(user_profile):
    return [ "source", Path.home() / user_profile ]

def main():

    SCRIPT_DIR   = Path(__file__).parent
    GIT_TOPLEVEL = Path(subprocess.run(git_toplevel(SCRIPT_DIR), capture_output=True, text= True).stdout.strip())
    FHS_ROOT_DIR = Path("root/home")
    USER_PROFILE = ".profile"

    TEMP_PATH = GIT_TOPLEVEL / FHS_ROOT_DIR

    print(bbb(TEMP_PATH, USER_PROFILE))
    print(sss(USER_PROFILE))

if __name__ == '__main__':
    main()