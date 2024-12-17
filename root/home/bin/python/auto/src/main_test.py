import func_main
import os
import sys

func_main.check_arg()
data_env_var = "XDG_STATE_HOME"
filepath = os.getenv(data_env_var)
arg_str  = sys.argv[1]

yaml_dict_set = [ 'array_audio.yaml', 'array_video.yaml' ]

yaml_dict_strings = func_main.tgtg(filepath, yaml_dict_set)
y_dow_symbol = func_main.dow_yesterday(1)
y_dict_set   = func_main.alt_dow(yaml_dict_strings, "dow", y_dow_symbol)
get_arg_set  = func_main.alt_arg(yaml_dict_strings, "contents", arg_str)

# print(y_dict_set)
# print(get_arg_set)
# sys.exit()

if   arg_str == "dow":
  func_main.sub(y_dict_set, y_dow_symbol)
elif get_arg_set == []:
  print("No")
elif arg_str == get_arg_set[0]["yyyy"]:
  func_main.sub(get_arg_set, y_dow_symbol)
