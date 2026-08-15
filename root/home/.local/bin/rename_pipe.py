#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path


def main():

    if not sys.stdin.isatty():
        print("標準入力（パイプ・リダイレクト）があります。")
        # すべての入力を一括で読み込む
        data = sys.stdin.read()
        print(f"受け取ったデータ:\n{data}")
    else:
        print("標準入力はありません（ターミナルからの直接実行です）。")
        user_input = input("文字を入力してください: ")
        # 対話的に入力を促す

    # print(Path.cwd())

    for aaa in sys.stdin:

        if len(sys.argv) == 1:
            print("argument is 0")



        if len(sys.argv) == 2:
            print("argument is 1")

            AAA = Path(aaa.rstrip()).absolute()

            if not AAA.exists():
                print("file is nothing")
                sys.exit()

            # print(AAA)


            LLL = AAA.parent / AAA.name
            RRR = AAA.parent / AAA.with_stem("alpha")


            print([ "mv",  f"{AAA.parent / AAA.name}",  f"{AAA.parent / AAA.with_stem("alpha")}" ])






if __name__ == '__main__':
    main()

