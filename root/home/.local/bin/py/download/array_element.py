

class selenium:
    pass
    apple_podcast = {
        "series":   ".headings__title",
        "episode":  "li.svelte-8rlk6b:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(1) > div:nth-child(2) > h3:nth-child(1) > div:nth-child(1)",
        "link":     "li.svelte-8rlk6b:nth-child(1) > div:nth-child(1) > a:nth-child(1)",
    }
    tver = {
        "series":   ".series-main_title__qi7zw",
        "episode":  "div.episode-row_host__nSdWB:nth-child(1) > a:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)",
        "link":     "div.episode-row_host__nSdWB:nth-child(1) > a:nth-child(1)",
    }

class xml:
    pass
    megaphone_fm = {
        "series":   "rss > channel > title",
        "episode":  "item > title",
        "link":     "enclosure",
    }
    # radiko = {
    #     "series":   "radiko > stations > station > progs > prog > title",
    #     "episode":  "radiko > stations > station > progs > prog > title",
    #     "link":     "radiko > stations > station > progs > prog > ts_in_ng",
    # }
