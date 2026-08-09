#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path


def main():

    if sys.argv == 2:
        pass


    # print(Path.cwd())

    for aaa in sys.stdin:

        AAA = Path(aaa.rstrip()).absolute()

        if not AAA.exists():
            print("file is nothing")
            sys.exit()

        # print(AAA)


        LLL = AAA.parent / AAA.name
        RRR = AAA.parent / AAA.with_stem("alpha")


        subprocess.run([ "mv",  f"{AAA.parent / AAA.name}",  f"{AAA.parent / AAA.with_stem("alpha")}" ])




















if __name__ == '__main__':
    main()