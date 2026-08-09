#!/usr/bin/env python3

import os
import subprocess
from pathlib import Path

def rrr(SCRIPT_DIR):
    return [ "git", "-C", SCRIPT_DIR, "rev-parse", "--show-toplevel" ]

def main():

    TEMPLATE_PATH = Path(Path.home() / "template.dvb_stram.m3u")
    GENERATE_PATH = Path(Path.home() / "test.m3u")

    SCRIPT_PATH  = Path(__file__)
    SCRIPT_DIR   = SCRIPT_PATH.parent
    GIT_TOPLEVEL = Path(subprocess.run(rrr(SCRIPT_DIR), capture_output=True, text= True).stdout.strip())

    ROOT_FHS_DIR = Path("root/home")
    XDG_DIR      = Path(".local/bin")
    FILENAME     = "dvb_stram.m3u"

    # TEMPLATE_PATH = GIT_TOPLEVEL / ROOT_FHS_DIR / f"template.{FILENAME}"
    # GENERATE_PATH = Path.home() / "XDG_USER_DIRS/Desktop" / FILENAME

    print(TEMPLATE_PATH)
    print(GENERATE_PATH)

    # template = TEMPLATE_PATH.read_text()
    # generated = os.path.expandvars(template)

    # GENERATE_PATH.write_text(generated)


if __name__ == '__main__':
    main()