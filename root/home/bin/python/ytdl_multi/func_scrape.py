
from selenium import webdriver
from urllib import request
from time import sleep
from bs4  import BeautifulSoup


def selenium(url):
  # set webdriver option
  fx_options = webdriver.FirefoxOptions()
  fx_options.add_argument("--headless")

  # get source
  driver = webdriver.Firefox(options = fx_options)
  driver.get(url)
  sleep(5)

  # scraping
  get_html = driver.page_source
  soup = BeautifulSoup(get_html, "html.parser")
  driver.quit()

  return soup


# def xml(url):
#   # scraping
#   get_xml = request.urlopen(url)
#   soup = BeautifulSoup(get_xml, "xml")

#   return soup


def hhh(scraper, url):

  if   scraper == "selenium":
    return selenium(url)
  # elif scraper == "xml":
  #   return xml(url)
