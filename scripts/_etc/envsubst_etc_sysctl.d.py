#!/usr/bin/env python3

import os
import sys
import re
from pathlib import Path
import subprocess

def git_toplevel(script_dir):
    return [ "git", "-C", script_dir, "rev-parse", "--show-toplevel" ]

def search_text(file_path, pattern):
    text    = Path(file_path).read_text(encoding="utf-8")
    matches = re.findall(pattern, text)
    return list(dict.fromkeys(matches))


def main():

    SCRIPT_DIR    = Path(__file__).parent
    GIT_TOPLEVEL  = Path(subprocess.run(git_toplevel(SCRIPT_DIR), capture_output=True, text= True).stdout.strip())
    # FHS_ROOT_DIR  = "root"
    TARGET_DIR    = Path("root/etc/sysctl.d")

    GENERATE_FILENAME = "99_ipv6-privacy.conf"
    TEMPLATE_FILENAME = GENERATE_FILENAME + ".template"

    TEMPLATE_PATH = GIT_TOPLEVEL / TARGET_DIR / TEMPLATE_FILENAME
    GENERATE_PATH = TARGET_DIR.relative_to("root") / GENERATE_FILENAME


    print(TEMPLATE_PATH)
    print(GENERATE_PATH)





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

        # template  = TEMPLATE_PATH.read_text()
        # generated = os.path.expandvars(template)
        # GENERATE_PATH.write_text(generated)

    else:
        print("check_var is empty")
        sys.exit()







if __name__ == '__main__':
    main()