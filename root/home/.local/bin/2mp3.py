#!/usr/bin/env python3

import sys
import subprocess
from pathlib import Path


def encode(input_file, bitrate, output_file):

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
        f"{output_file}.mp3"
    ]


def main():

    if not len(sys.argv) == 2:
        print("Argument is Less")
        sys.exit()

    INPUT_FILE  = Path(sys.argv[1]).absolute()

    if not INPUT_FILE.exists():
        print("Argument is invailed")
        sys.exit()

    DIRECTORY = INPUT_FILE.parent
    BASENAME  = INPUT_FILE.stem
    ext       = INPUT_FILE.suffix
    BITRATE   = 48

    OUTPUT_FILE = DIRECTORY / BASENAME

    ddd = encode(INPUT_FILE, BITRATE, OUTPUT_FILE)
    print(ddd)


if __name__ == '__main__':
    main()

