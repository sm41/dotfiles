#!/usr/bin/python3

from __init__ import *

# check argment
ARGS = sys.argv[1]

# set membars class
for AAA in inspect.getmembers(array_member, inspect.isclass):
    members_class = AAA[1]
    if hasattr(members_class, ARGS):
        SET_MEMBER   = getattr(members_class, ARGS)
        SET_PLATFORM = AAA[0]
        break

# set element class
for BBB in inspect.getmembers(array_element, inspect.isclass):
    element_class = BBB[1]
    if hasattr(element_class, SET_PLATFORM):
        SET_SELECTOR = getattr(element_class, SET_PLATFORM)
        SET_SCRAPER  = BBB[0]
        break

# scrape and parse
material = getattr(func_scrape, SET_SCRAPER)(SET_MEMBER["url"])
soup     = getattr(func_parse, SET_PLATFORM)(material)

SERIES  = soup[0]
EPISODE = soup[1]
LINK    = soup[2]

# # download
method   = getattr(func_ytdlp, SET_PLATFORM)(LINK)
result   = subprocess.run(method)

if result.returncode == 0:
    notification.notify(
        title = "✅ Success",
        message = f"{SERIES}\n{EPISODE}"
    )
else:
    notification.notify(
        title = "⚠️ failed",
        message = f"{SERIES}\n{EPISODE}"
    )

# print(SERIES)
# print(EPISODE)
# print(LINK)

# print(SET_MEMBER)
# print(SET_PLATFORM)
# print(SET_SELECTOR)
# print(SET_SCRAPER)