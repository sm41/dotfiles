from locale import setlocale, LC_TIME, LC_ALL
from datetime import datetime, timedelta



class ctrl_date:
  def __init__(self):
    setlocale(LC_TIME, 'ja_JP.UTF-8')
    self.today_now  = datetime.now().replace(second=0, microsecond=0)
    self.today_date = self.today_now.date()
    self.today_dow  = self.today_date.strftime('%a')

  def yesterday(self, day_int:int):
    self.n_days_ago_now  = self.today_now - timedelta(day_int)
    self.n_days_ago_date = self.n_days_ago_now.date()
    self.n_days_ago_dow  = self.n_days_ago_date.strftime('%a')
    return self

  def format(self, someday_now:datetime):
    self.format_time  = someday_now.strftime('%Y%m%d%H%M')+'00'
    return self

  def quarte(self):
    self.quarte_date  = (self.n_days_ago_date.month - 1) // 3 + 1
    return self