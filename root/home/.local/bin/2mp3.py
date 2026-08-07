#!/usr/bin/env python3

import sys
from pathlib import Path


def ooo(input_file, bitrate, basename):

    return [
        "ffmpeg",
            "-i", input_file,
            "-map", "0:a",
            "-map", "0:v:0",
            "-c:a", "libmp3lame",
            "-b:a", bitrate,
            "-disposition:1", "attached_pic",
            "-id3v2_version", "3",
            "-metadata:s:v",  "title='Album cover'",
            "-metadata:s:v",  "comment='Cover (front)'",
        f"{basename}.mp3"
    ]


def main():

    input_file = sys.argv[1]
    file_path  = Path(input_file).absolute()

    if not file_path.exists():
        print("Argument is invailed")
        sys.exit()

    directory = file_path.parent
    basename  = file_path.stem
    ext       = file_path.suffix
    bitrate   = 48

    bbb = directory / basename

    # print(file_path)
    # print(directory)
    # print(basename)
    # print(ext)


    ddd = ooo(input_file, bitrate, bbb)
    print(ddd)


if __name__ == '__main__':
    main()

