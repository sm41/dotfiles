from re import compile
import func

class hoge:
  def __init__(self):
    pass

  def yamato(self):
    self.website = "南房総 やまと寿司"
    self.url     = "https://yamato-f.jp/tabeho"
    self.soup    = func.selenium(self.url)
    self.article = self.soup.find(class_ = compile("el_articleCard_title")).text.strip()
    self.page    = self.soup.find(class_ = compile("el_articleCard")).attrs['href']


  # def nhk(self):
  #   self.website = "NHK"
  #   self.url     = "https://www3.nhk.or.jp/news/catnew.html"
  #   self.soup    = func.selenium(self.url)
  #   self.article = self.soup.find(class_ = "title").text.strip()
  #   self.page    = "https://www3.nhk.or.jp" + self.soup.select_one('ul > li > dl > dd > a').attrs['href']


  def dariaartificial(self):
    self.website = "DariaArtificial"
    self.url     = "https://twstalker.com/DariaArtificial"
    self.soup    = func.selenium(self.url)
    self.article = self.website
    self.page    = "https://twstalker.com" + self.soup.select_one("div > span > a").attrs['href']
    # https://x.com/i/user/1690092058055233536


  def mnemosynekoto(self):
    self.website = "mnemosynekoto"
    self.url     = "https://kemono.cr/patreon/user/86508534"
    self.soup    = func.selenium(self.url)
    self.article = self.website
    self.page    = "https://kemono.cr" + self.soup.select_one("div > article > a").attrs['href']