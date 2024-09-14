
import re
import __main__

def apple_podcast(bouillon):
    ROW_SERIES   = bouillon.select_one(__main__.SET_SELECTOR["series"]).get_text()
    ROW_EPISODE  = bouillon.select_one(__main__.SET_SELECTOR["episode"]).get_text()
    ROW_LINK     = bouillon.select_one(__main__.SET_SELECTOR["link"]).attrs['href']

    return ROW_SERIES, ROW_EPISODE, ROW_LINK


def megaphone_fm(FFF):
    bouillon = FFF.find("title", string=re.compile(__main__.SET_MEMBER["anchor"])).parent

    ROW_SERIES   =      FFF.select_one(__main__.SET_SELECTOR["series"]).get_text()
    ROW_EPISODE  = bouillon.select_one(__main__.SET_SELECTOR["episode"]).get_text()
    ROW_LINK     = bouillon.select_one(__main__.SET_SELECTOR["link"]).attrs['url']

    return ROW_SERIES, ROW_EPISODE, ROW_LINK


def tver(bouillon):
    ROW_SERIES   = bouillon.select_one(__main__.SET_SELECTOR["series"]).get_text()
    ROW_EPISODE  = bouillon.select_one(__main__.SET_SELECTOR["episode"]).get_text()
    ROW_LINK     = bouillon.select_one(__main__.SET_SELECTOR["link"]).attrs['href']
    ROW_LINK_MOD = "https://tver.jp" + ROW_LINK

    return ROW_SERIES, ROW_EPISODE, ROW_LINK_MOD


def radiko(soup):
    bouillon = soup.find(string=re.compile(__main__.SET_MEMBER["title"])).parent.parent

    ROW_SERIES   = bouillon.select_one(__main__.SET_SELECTOR["series"]).get_text()
    ROW_EPISODE  = bouillon.select_one(__main__.SET_SELECTOR["episode"]).get_text()
    ROW_LINK     = bouillon.select_one(__main__.SET_SELECTOR["link"]).attrs['url']

    return ROW_SERIES, ROW_EPISODE, ROW_LINK
