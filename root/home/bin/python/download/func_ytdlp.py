import __main__
import os
import sys


# MNT_ENV_VAR = "CLIENT_LOCAL_STORAGE"
MNT_ENV_VAR = "CLIENT_LOCAL_STORAGE"
PODCAST_DIR = "/@podcast"
TVER_DIR    = "/@tver"

MNT_PATH = os.getenv(MNT_ENV_VAR)

# print(MNT_PATH + PODCAST_DIR)

# if MNT_PATH is None:
#     print(type(MNT_PATH))
#     print(f"\"{MNT_ENV_VAR}\" is not define")
#     sys.exit()
# else:
#     if os.path.isdir(MNT_PATH):
#         print(MNT_PATH)
#         print(f"\"{MNT_PATH}\" is ok")
#     else:
#         print(MNT_PATH)
#         print(f"\"{MNT_PATH}\" is not exist PATH")
#         sys.exit()



def apple_podcast(target_url):
    cmd_ytdlp = [
        "yt-dlp",
        "--paths",  MNT_PATH + PODCAST_DIR,
        "--output", "[Podcast]_%(series)s_%(upload_date>%Y-%m-%d)s_%(title)s.%(ext)s",
        target_url
    ]
    return cmd_ytdlp


def megaphone_fm(target_url):
    cmd_ytdlp = [
        "yt-dlp",
        "--paths",  MNT_PATH + PODCAST_DIR,
        "--output", "[Podcast]_" + __main__.soup[0] + "_" + __main__.soup[1] + ".%(ext)s",
        target_url
    ]
    return cmd_ytdlp


def tver(target_url):
    cmd_ytdlp = [
        "yt-dlp",
        "--embed-subs",
        "--paths",  MNT_PATH + TVER_DIR,
        "--output", "[%(webpage_url_domain)s]_%(series)s_%(episode)s.%(ext)s",
        target_url
    ]
    return cmd_ytdlp
