#!/usr/bin/env python3

from pathlib import Path
import re
import subprocess
import sys
import unicodedata

def encode(before_path, after_path):
    return [
        "ffmpeg",
            "-nostdin",
            "-loglevel", "warning",
            "-i", before_path,
        after_path
    ]


def sanitize_filename(name):

    if type(name) != type(str):
        name = str(name)

    # Windows禁止文字
    # WINDOWS_FORBIDDEN = r'[\\/:*?"<>|]'

    # 全角 → 半角変換テーブル
    Z2H_TABLE = str.maketrans(
        # 全角英数字
        '０１２３４５６７８９'
        'ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ'
        'ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ'
        # 全角記号（よく使うもの）
        # '＃（）［］｛｝＜＞＠％＆＋＝！？．，'
        '＃（）［］｛｝＜＞＠％＆＋＝．，'
        ,
        # 対応する半角
        '0123456789'
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        'abcdefghijklmnopqrstuvwxyz'
        # '#()[]{}<>@%&+=!?.,'
        '#()[]{}<>@%&+=.,'
    )


    # 1. Unicode正規化
    name = unicodedata.normalize("NFC", name)

    # 2. 全角英数字・記号 → 半角
    name = name.translate(Z2H_TABLE)

    # 3. スペース（全角・半角） → _
    name = re.sub(r'[ 　]', '_', name)

    # 4. Windows禁止文字 → _
    # name = re.sub(WINDOWS_FORBIDDEN, '_', name)

    # 5. 連続 _ を1つに
    name = re.sub(r'_+', '_', name)

    # 6. 末尾のドット・空白を削除（Windows対策）
    name = name.rstrip('. ')

    return Path(name)


def main():
    old_ext  = "png"
    new_ext  = "jpg"
    hogefuga = "_[encoded]"

    standard_path = Path(sys.argv[1]).resolve()

    if standard_path.exists():

        if standard_path.is_dir():

            before_parent = standard_path
            after_parent  = sanitize_filename(standard_path.with_name(standard_path.name + hogefuga))

            for target_path in sorted(standard_path.rglob(f"*.{old_ext}")):

                child = target_path.relative_to(standard_path)

                if str(child).startswith("."):
                    continue

                if target_path.is_dir():
                    continue

                after_child = sanitize_filename(child.parent)
                after_name  = sanitize_filename(child.name)

                before_path = before_parent / child.parent / child.name
                after_path  = after_parent  / after_child  / after_name.with_suffix(f".{new_ext}")

                if not after_path.parent.exists():
                    after_path.parent.mkdir(parents=True)

                subprocess.run(encode(before_path, after_path))


        elif standard_path.is_file():

            before_parent = standard_path.parent
            # after_parent  = standard_path.parent.with_name(standard_path.parent.name + "_hogefuga")
            before_name   = standard_path.name
            after_name    = sanitize_filename(standard_path.with_suffix(".pdf").name)

            before_path = before_parent / before_name
            after_path  = before_parent / after_name

            subprocess.run(encode(before_path, after_path))


    else:
        print("NG")


if __name__ == '__main__':
    main()