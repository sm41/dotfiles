from locale import setlocale, LC_TIME, LC_ALL
from datetime import datetime, timedelta


class Ctrl_Date:
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

  def format(self, someday_now:datetime, format):
    self.format_time  = someday_now.strftime(format)
    return self

  def quarte(self, any_month):
    self.quarte_date  = (any_month - 1) // 3 + 1
    return self

  def change_format(self, input_string, format_string, output_string):
    setlocale(LC_TIME, (None,None))

    dt_tz = datetime.strptime(input_string, format_string)
    self.formatted_date = dt_tz.strftime(output_string)
    return self
