#!/usr/bin/env python3

import subprocess
from pathlib import Path

def rrr(SCRIPT_DIR):
    return [ "git", "-C", SCRIPT_DIR, "rev-parse", "--show-toplevel" ]

def bbb(hoge, fuga):
    return [ "ln", "-s", "-f", hoge, fuga ]


def main():

    ignore_path = [
        "systemd/user"
    ]

    SCRIPT_PATH  = Path(__file__)
    SCRIPT_DIR   = SCRIPT_PATH.parent
    GIT_TOPLEVEL = Path(subprocess.run(rrr(SCRIPT_DIR), capture_output=True, text= True).stdout.strip())

    ROOT_FHS_DIR = Path("root/home")
    XDG_DIR      = Path(".config")

    CONFIG_REPOSITORY = GIT_TOPLEVEL / ROOT_FHS_DIR / XDG_DIR

    for DOT_CONFIG in sorted(CONFIG_REPOSITORY.rglob('*')):

        if DOT_CONFIG.is_dir():
            continue

        LOCAL_BIN = Path.home() / DOT_CONFIG.relative_to(GIT_TOPLEVEL / ROOT_FHS_DIR)

        for aaa in ignore_path:
            if str(CONFIG_REPOSITORY / aaa) in str(DOT_CONFIG):
                continue
            else:
                if not LOCAL_BIN.parent.exists():
                    LOCAL_BIN.parent.mkdir(parents=True, exist_ok=True)

                result = subprocess.run(bbb(DOT_CONFIG, LOCAL_BIN))

                if result.returncode == 0:
                    print(f"✅  {DOT_CONFIG}  --->   {LOCAL_BIN}")
                else:
                    print(f"🚫  {DOT_CONFIG}  --->   {LOCAL_BIN}")


            # if DOT_CONFIG.match('systemd/user/*'):
            #     continue
            # else:
            #     print(bbb(DOT_CONFIG, LOCAL_BIN))


if __name__ == '__main__':
    main()

