#!/usr/bin/env python3


import subprocess
from pathlib  import Path
from datetime import datetime

# 現在日時を指定のフォーマットで取得
current_time = datetime.now().strftime('%Y%m%d_%H%M')

def git_toplevel(script_dir):
    return [ "git", "-C", script_dir, "rev-parse", "--show-toplevel" ]

def bbb(temp_path, user_profile):
    return [ "cp", "-f", "-b", f"--suffix=_{current_time}",  f"{temp_path}/sample{user_profile}",  Path.home() / user_profile ]

def sss(user_profile):
    return [ "source", Path.home() / user_profile ]

def main():

    SCRIPT_DIR   = Path(__file__).parent
    GIT_TOPLEVEL = Path(subprocess.run(git_toplevel(SCRIPT_DIR), capture_output=True, text= True).stdout.strip())
    FHS_ROOT_DIR = Path("root/home")
    USER_PROFILE = ".profile"

    TEMP_PATH = GIT_TOPLEVEL / FHS_ROOT_DIR

    subprocess.run(bbb(TEMP_PATH, USER_PROFILE))
    subprocess.run(sss(USER_PROFILE))

if __name__ == '__main__':
    main()