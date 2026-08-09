#!/usr/bin/env python3

import subprocess
from pathlib import Path

def rrr(SCRIPT_DIR):
    return [ "git", "-C", SCRIPT_DIR, "rev-parse", "--show-toplevel" ]

def make_symlink(hoge, fuga):
    return [ "ln", "-s", "-f", hoge, fuga ]


def main():

    SCRIPT_PATH  = Path(__file__)
    SCRIPT_DIR   = SCRIPT_PATH.parent
    GIT_TOPLEVEL = Path(subprocess.run(rrr(SCRIPT_DIR), capture_output=True, text= True).stdout.strip())

    ROOT_FHS_DIR = Path("root/home")
    XDG_DIR      = Path(".local/bin")

    BIN_REPOSITORY = GIT_TOPLEVEL / ROOT_FHS_DIR / XDG_DIR

    for BIN_PATH in sorted(BIN_REPOSITORY.rglob('*')):

        LOCAL_BIN = Path.home() / BIN_PATH.relative_to(GIT_TOPLEVEL / ROOT_FHS_DIR)

        if not LOCAL_BIN.parent.exists():
            LOCAL_BIN.parent.mkdir(parents=True, exist_ok=True)

        result = subprocess.run(make_symlink(BIN_PATH, LOCAL_BIN.parent / LOCAL_BIN.name))

        if result.returncode == 0:
            print(f"✅  {BIN_PATH}  --->   {LOCAL_BIN.parent / LOCAL_BIN.name}")
        else:
            print(f"🚫  {BIN_PATH}  --->   {LOCAL_BIN.parent / LOCAL_BIN.name}")


if __name__ == '__main__':
    main()

