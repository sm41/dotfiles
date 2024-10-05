import __main__

MNT     = "/mnt/640G"
PODCAST = "/@podcast"
TVER    = "/@tver"

def apple_podcast(target_url):
    cmd_ytdlp = [
        "yt-dlp",
        "--paths",  MNT + PODCAST,
        "--output", "[Podcast]_%(series)s_%(upload_date>%Y-%m-%d)s_%(title)s.%(ext)s",
        target_url
    ]
    return cmd_ytdlp


def megaphone_fm(target_url):
    cmd_ytdlp = [
        "yt-dlp",
        "--paths",  MNT + PODCAST,
        "--output", "[Podcast]_" + __main__.soup[0] + "_" + __main__.soup[1] + ".%(ext)s",
        target_url
    ]
    return cmd_ytdlp


def tver(target_url):
    cmd_ytdlp = [
        "yt-dlp",
        "--paths",  MNT + TVER,
        "--output", "[%(webpage_url_domain)s]_%(series)s_%(episode)s.%(ext)s",
        target_url
    ]
    return cmd_ytdlp