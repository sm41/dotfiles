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

    srx = str.maketrans(
        "/",
        "／"
    )


    name = name.translate(srx)

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

    if len(sys.argv) != 2:
        print("argv is")
        sys.exit()

    old_ext  = ".png"
    new_ext  = ".jpg"
    hogefuga = "_[encoded]"

    STANDARD_PATH = Path(sys.argv[1]).resolve()

    if not STANDARD_PATH.exists():
        print("NG")
        sys.exit()

    if STANDARD_PATH.is_dir():
        ORIGINAL_GRAND_DIRECTORY  = STANDARD_PATH.parents[0]
        ORIGINAL_PARENT_DIRECTORY = STANDARD_PATH.name
        REPLACED_PARENT_DIRECTORY = str(sanitize_filename(ORIGINAL_PARENT_DIRECTORY)) + hogefuga

        for target_path in sorted(STANDARD_PATH.rglob(f"*{old_ext}")):

            if target_path.is_dir():
                continue

            child = target_path.relative_to(STANDARD_PATH)

            if str(child).startswith("."):
                continue

            after_parent = sanitize_filename(child.parent)
            after_name   = sanitize_filename(child.name)
            before_path  = ORIGINAL_GRAND_DIRECTORY / ORIGINAL_PARENT_DIRECTORY / child.parent / child.name
            after_path   = ORIGINAL_GRAND_DIRECTORY / REPLACED_PARENT_DIRECTORY / after_parent / after_name.with_suffix(new_ext)

            if not after_path.parent.exists():
                after_path.parent.mkdir(parents=True)

            subprocess.run(encode(before_path, after_path))

    elif STANDARD_PATH.is_file():
        before_parent = STANDARD_PATH.parent
        # after_parent  = STANDARD_PATH.parent.with_name(STANDARD_PATH.parent.name + "_hogefuga")
        before_name   = STANDARD_PATH.name
        after_name    = sanitize_filename(STANDARD_PATH.with_suffix(".pdf").name)
        before_path   = before_parent / before_name
        after_path    = before_parent / after_name

        subprocess.run(encode(before_path, after_path))


if __name__ == '__main__':
    main()