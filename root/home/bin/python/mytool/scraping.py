from bs4      import BeautifulSoup
from re       import compile
from time     import sleep
from selenium import webdriver
import requests

class scrp:
  def __init__(self):
    pass

  def get_response(self, url):
    self.url           = url
    self.response_text = requests.get(self.url).text
    return self

  def make2soup(self):
    fx_options = webdriver.FirefoxOptions()
    fx_options.add_argument("--headless")
    driver = webdriver.Firefox(options = fx_options)
    driver.get(self.url)
    sleep(5)
    get_html = driver.page_source
    self.response_text = get_html
    driver.quit()
    return self

  def simple(self, markup_type):
    self.soup = BeautifulSoup(self.response_text, markup_type)
    return self

  def tver(self, soup:BeautifulSoup):
    self.url = "https://tver.jp" + soup.find(class_ = compile("episode-row_container")).attrs['href']