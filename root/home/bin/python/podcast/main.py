from sys import argv, exit
from mytool  import ctrl_string, ctrl_date
import func, tenpai


def main():
  ctrl_string.ctrl_arg.check_arg(argv[1])
  variable = func.gen_var()
  branch   = func.check_arg()
  time     = ctrl_date.ctrl_date().yesterday(1)

  if variable.arg == "dow":
    branch.today_list(variable.loaded_yaml, time.n_days_ago_dow)
  else:
    branch.series_name(variable.loaded_yaml, variable.arg)

  if not branch.reserve_list:
    print("⚠️  No matching podcast found")
    exit()

  tenpai.ddwwnn(branch, variable)

