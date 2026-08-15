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


def mmm(eee):

    required_env = search_text(eee, r"\$\{([^}]+)\}")
    check_var = {}

    for env in required_env:
        if os.getenv(env):
            check_var[env] = True
        else:
            check_var[env] = False

    if check_var:
        for k,v in check_var.items():
            print(f"{k} : {v}")
    else:
        print("check_var is empty")
        sys.exit()

    if all(check_var.values()):
        print("all ok")

        # template  = TEMPLATE_PATH.read_text()
        # generated = os.path.expandvars(template)
        # GENERATE_PATH.write_text(generated)
        # GENERATE_PATH.chmod(0o600)

        # subprocess.run([ "chmod" "600" f"{GENERATE_PATH}" ])
        # subprocess.run([ "nmcli" "connection" "reload" ])
        # subprocess.run([ "systemctl" "restart" "NetworkManager" ])
    else:
        print("any ng")
        sys.exit()

    return check_var


def main():

    SCRIPT_DIR    = Path(__file__).parent
    GIT_TOPLEVEL  = Path(subprocess.run(git_toplevel(SCRIPT_DIR), capture_output=True, text= True).stdout.strip())
    # FHS_ROOT_DIR  = "root"
    TARGET_DIR    = "etc/NetworkManager/system-connections"

    GENERATE_FILENAME = "network_interface.nmconnection"
    TEMPLATE_FILENAME = "template." + GENERATE_FILENAME

    TEMPLATE_FILENAME = "template.network_interface.nmconnection"
    # GENERATE_FILENAME = f"{NETWORK_INTERFACE}.nmconnection"

    TEMPLATE_PATH = GIT_TOPLEVEL / "root" / TARGET_DIR / TEMPLATE_FILENAME
    GENERATE_PATH = Path("/" + TARGET_DIR) / GENERATE_FILENAME

    if TEMPLATE_PATH.exists():
        print("File is exist")
        print(TEMPLATE_PATH)
        print(GENERATE_PATH)
    else:
        print("No such file")
        sys.exit()

    print(mmm(TEMPLATE_PATH))







if __name__ == '__main__':
    main()