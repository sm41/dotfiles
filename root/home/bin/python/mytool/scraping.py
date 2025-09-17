from bs4       import BeautifulSoup
from re        import compile
from time      import sleep
from selenium  import webdriver
from urllib    import request
from sys       import exit
from http.client import HTTPResponse


class scrp:
  def __init__(self):
    pass


  def check_status_code(self, url):
    self.url = url
    self.response: HTTPResponse = request.urlopen(url)
    if self.response.getcode() != 200:
      print(f"Status Code is {self.response.getcode()} !!")
      exit()

    return self


  def make2soup(self):
    __fx_options = webdriver.FirefoxOptions()
    __fx_options.add_argument("--headless")
    __driver = webdriver.Firefox(options = __fx_options)
    __driver.get(self.url)
    sleep(5)
    __get_html = __driver.page_source
    self.response = __get_html
    __driver.quit()
    return self


  def simple(self, markup_type):
    self.soup = BeautifulSoup(self.response, markup_type)
    return self


  def tver(self, soup:BeautifulSoup):
    self.url = "https://tver.jp" + soup.find(class_ = compile("episode-row_container")).attrs['href']