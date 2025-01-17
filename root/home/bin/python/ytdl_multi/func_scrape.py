
from selenium import webdriver
from time import sleep
from bs4  import BeautifulSoup
# from urllib import request


def selenium(url):
  fx_options = webdriver.FirefoxOptions()
  fx_options.add_argument("--headless")

  driver = webdriver.Firefox(options = fx_options)
  driver.get(url)
  sleep(5)

  get_html = driver.page_source
  soup = BeautifulSoup(get_html, "html.parser")
  driver.quit()

  return soup


# def hhh(scraper, url):

#   if   scraper == "selenium":
#     return selenium(url)

