#!/usr/bin/env python3

import sys
import subprocess
from pathlib import Path


def encode(input_file, bitrate, output_file):

    return [
        "ffmpeg",
            "-loglevel", "error",
            "-i", input_file,
            "-map", "0:a",
            "-map", "0:v:0",
            "-c:a", "libmp3lame",
            "-b:a", str(bitrate),
            "-disposition:1", "attached_pic",
            "-id3v2_version", "3",
            "-metadata:s:v",  "title='Album cover'",
            "-metadata:s:v",  "comment='Cover (front)'",
        f"{output_file}.mp3"
    ]


def main():

    if len(sys.argv) != 2:
        print("Argument is Less")
        sys.exit()

    INPUT_FILE  = Path(sys.argv[1]).absolute()

    if not INPUT_FILE.is_file():
        print("Argument is invailed")
        sys.exit()

    BITRATE     = 48
    OUTPUT_FILE = INPUT_FILE.parent / INPUT_FILE.stem

    result = subprocess.run(encode(INPUT_FILE, BITRATE, OUTPUT_FILE))

    if result.returncode == 0:
        print()
    else:
        print()

if __name__ == '__main__':
    main()
