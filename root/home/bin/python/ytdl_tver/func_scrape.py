
from selenium import webdriver
from bs4  import BeautifulSoup
from time import sleep
from re   import compile


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


def tver(soup:BeautifulSoup):

  url     = soup.find(class_ = compile("episode-row_container")).attrs['href']
  url_mod = "https://tver.jp" + url
  return url_mod

