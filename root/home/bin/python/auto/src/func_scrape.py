
from selenium import webdriver
import urllib.request
import time
import bs4


def selenium(url):
  # set webdriver option
  fx_options = webdriver.FirefoxOptions()
  fx_options.add_argument("--headless")

  # get source
  driver = webdriver.Firefox(options = fx_options)
  driver.get(url)
  time.sleep(5)

  # scraping
  get_html = driver.page_source
  soup = bs4.BeautifulSoup(get_html, "html.parser")
  driver.quit()

  return soup


def xml(url):
  # scraping
  get_xml = urllib.request.urlopen(url)
  soup = bs4.BeautifulSoup(get_xml, "xml")

  return soup


def hhh(scraper, url):

  if   scraper == "selenium":
    return selenium(url)
  elif scraper == "xml":
    return xml(url)
