#!/usr/bin/env python3


import subprocess
from pathlib import Path


def git_toplevel(script_dir):
    return [ "git", "-C", script_dir, "rev-parse", "--show-toplevel" ]

def make_symlink(hoge, fuga):
    return [ "ln", "-s", "-f", hoge, fuga ]


def main():

    ignore_list = [
        "systemd/user"
    ]

    SCRIPT_DIR   = Path(__file__).parent
    GIT_TOPLEVEL = Path(subprocess.run(git_toplevel(SCRIPT_DIR), capture_output=True, text= True).stdout.strip())
    FHS_ROOT_DIR = Path("root/home")
    XDG_DIR      = Path(".config")

    CONFIG_REPOSITORY = GIT_TOPLEVEL / FHS_ROOT_DIR / XDG_DIR

    for DOT_CONFIG in sorted(CONFIG_REPOSITORY.rglob('*')):

        if DOT_CONFIG.is_dir():
            continue

        LOCAL_BIN = Path.home() / DOT_CONFIG.relative_to(GIT_TOPLEVEL / FHS_ROOT_DIR)

        for ignore_path in ignore_list:
            if str(CONFIG_REPOSITORY / ignore_path) in str(DOT_CONFIG):
                print(f"🚫  {DOT_CONFIG}")
                continue
            else:
                if not LOCAL_BIN.parent.exists():
                    LOCAL_BIN.parent.mkdir(parents=True, exist_ok=True)

                result = subprocess.run(make_symlink(DOT_CONFIG, LOCAL_BIN))

                if result.returncode == 0:
                    print(f"✅  {DOT_CONFIG}  --->   {LOCAL_BIN}")
                else:
                    print(f"🚫  {DOT_CONFIG}  --->   {LOCAL_BIN}")


            # if DOT_CONFIG.match('systemd/user/*'):
            #     continue
            # else:
            #     print(make_symlink(DOT_CONFIG, LOCAL_BIN))


if __name__ == '__main__':
    main()

