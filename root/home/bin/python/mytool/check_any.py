from sys  import argv, exit


class check_any:
  @staticmethod
  def check_arg():
    if len(argv) <= 1:
      exit('You need args!')

  @staticmethod
  def check_status_code(subject):
    if subject.getcode() != 200:
      print(f"Status Code is {subject.getcode()} !!")
      exit()
