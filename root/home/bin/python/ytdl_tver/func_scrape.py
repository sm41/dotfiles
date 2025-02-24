from selenium import webdriver
from bs4  import BeautifulSoup
from time import sleep
from re   import compile
from datetime import date, timedelta
from locale   import setlocale, LC_TIME


def dow_yesterday(day_int:int):
  setlocale(LC_TIME, 'ja_JP.UTF-8')

  d_today      = date.today()
  d_yesterday  = d_today - timedelta( days = day_int )
  y_dow_str:str = d_yesterday.strftime('%a')
  return y_dow_str


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


def tver(bouillon):

  url     = bouillon.find(class_ = compile("episode-row_container")).attrs['href']
  url_mod = "https://tver.jp" + url
  return url_mod

