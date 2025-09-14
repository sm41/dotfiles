from locale import setlocale, LC_TIME, LC_ALL
from datetime import datetime, date, timedelta



class ctrl_date:
  def __init__(self, day_int:int):
    setlocale(LC_TIME, 'ja_JP.UTF-8')
    self.d_today     = date.today()
    self.d_yesterday = self.d_today - timedelta( days = day_int )
    self.y_dow       = self.d_yesterday.strftime('%a')
    self.q_date      = (self.d_yesterday.month - 1) // 3 + 1


  # def __init__(self, day_int:int):
  #   setlocale(LC_TIME, 'ja_JP.UTF-8')

  #   self.today_now  = datetime.now()
  #   self.today_date = self.today_now.date()
  #   self.today_dow  = self.today_date.strftime('%a')

  #   self.yesterday_now  = self.today_now - timedelta(day_int)
  #   self.yesterday_date = self.yesterday_now.date()
  #   self.yesterday_dow  = self.yesterday_date.strftime('%a')


  #   self.hoge = self.today_now.strftime('%Y%m%d%H%M')+'00'
  #   self.fuga = self.yesterday_now.strftime('%Y%m%d%H%M')+'00'

  #   self.q_date      = (self.yesterday_date.month - 1) // 3 + 1