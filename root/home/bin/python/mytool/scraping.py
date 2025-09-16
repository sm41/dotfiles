from bs4       import BeautifulSoup
from re        import compile
from time      import sleep
from selenium  import webdriver
from urllib  import request
from mytool  import check_any


class selenium:
  def __init__(self):
    pass

  def make_soup(self, url):
    __fx_options = webdriver.FirefoxOptions()
    __fx_options.add_argument("--headless")
    __driver = webdriver.Firefox(options = __fx_options)
    __driver.get(url)
    sleep(5)
    __get_html = __driver.page_source
    self.soup  = BeautifulSoup(__get_html, "html.parser")
    __driver.quit()
    return self.soup


  def tver(self, soup:BeautifulSoup):
    __url    = soup.find(class_ = compile("episode-row_container")).attrs['href']
    self.url = "https://tver.jp" + __url





class hoge:
  def __init__(self, url):
    self.url = url
    self.response = request.urlopen(url)
    check_any.check_any.check_status_code(self.response)


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


  def simple(self, response, markup_type):
    self.soup = BeautifulSoup(response, markup_type)
    return self


