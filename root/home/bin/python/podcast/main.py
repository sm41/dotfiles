from sys import argv, exit
from mytool  import ctrl_string as cs, ctrl_date as cd
import func, tenpai


def main():
  cs.Argument.check_arg(argv[1])
  variable = func.Set_Variable()
  branch   = func.Check_Argument()
  time     = cd.Date().yesterday(1)

  if variable.arg == "dow":
    branch.check_today_list(variable.loaded_yaml, time.n_days_ago_dow)
  else:
    branch.check_series_name(variable.loaded_yaml, variable.arg)

  if not branch.reserve_list:
    print("⚠️  No matching podcast found")
    exit()

  tenpai.ddwwnn(branch, variable)

