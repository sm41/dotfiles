#!/usr/bin/env python3

import os
import subprocess
from pathlib import Path


def rrr(SCRIPT_DIR):
    return [ "git", "-C", SCRIPT_DIR, "rev-parse", "--show-toplevel" ]

def bbb(hoge, fuga):
    return [ "ln", "-s", "-f", hoge, fuga ]


def main():

    SCRIPT_DIR   = Path(__file__).parent
    GIT_TOPLEVEL = Path(subprocess.run(rrr(SCRIPT_DIR), capture_output=True, text= True).stdout.strip())
    ROOT_FHS_DIR = Path("root/home")
    ORIGIN_DIR   = Path(".mozilla/firefox")

    TARGET_PATH      = Path.home() / ORIGIN_DIR
    TARGET_DIRECTORY = [ jjj for jjj in TARGET_PATH.glob('*.default-release') ]

    if len(TARGET_DIRECTORY) == 1:
        vvv = TARGET_PATH / TARGET_DIRECTORY[0].name

    FX_REPOSITORY = GIT_TOPLEVEL / ROOT_FHS_DIR / ORIGIN_DIR
    PROFILE_DIR   = [ iii for iii in FX_REPOSITORY.rglob('*default-release/**/*') ]

    for u in PROFILE_DIR:
        if u.is_file():
            q = vvv / u.relative_to(FX_REPOSITORY / "default-release")
            if not q.parent.exists():
                q.parent.mkdir()
            print(f"{u}   --->   {q}")


if __name__ == '__main__':
    main()

