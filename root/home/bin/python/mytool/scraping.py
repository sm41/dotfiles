from bs4       import BeautifulSoup
from re        import compile
from time      import sleep
from selenium  import webdriver




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
    self.soup = BeautifulSoup(__get_html, "html.parser")
    __driver.quit()
    return self.soup


  def tver(self, soup:BeautifulSoup):
    __url    = soup.find(class_ = compile("episode-row_container")).attrs['href']
    self.url = "https://tver.jp" + __url