#!/usr/bin/env python3

import subprocess
from pathlib import Path


def rrr(script_dir):
    return [ "git", "-C", script_dir, "rev-parse", "--show-toplevel" ]

def bbb(temp_path, user_profile):
    return [ "cp", "-f", "-b", "--suffix=_`date +%Y%m%d_%H%M`",  f"{temp_path}/sample{user_profile}",  Path.home() / user_profile ]

def sss(user_profile):
    return [ "source", Path.home() / user_profile ]

def main():

    SCRIPT_PATH  = Path(__file__)
    SCRIPT_DIR   = SCRIPT_PATH.parent
    GIT_TOPLEVEL = Path(subprocess.run(rrr(SCRIPT_DIR), capture_output=True, text= True).stdout.strip())

    ROOT_FHS_DIR = Path("root/home")
    USER_PROFILE = Path(".profile")

    TEMP_PATH = GIT_TOPLEVEL / ROOT_FHS_DIR

    print(bbb(TEMP_PATH, USER_PROFILE))
    print(sss(USER_PROFILE))

if __name__ == '__main__':
    main()