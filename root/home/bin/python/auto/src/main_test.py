import func_main
import os
import sys

func_main.check_arg()
data_env_var = "XDG_STATE_HOME"
filepath = os.getenv(data_env_var)
arg_str  = sys.argv[1]

yaml_files_list = [ 'audio.yaml', 'video.yaml' ]

yaml_dict_strings = func_main.tgtg(filepath, yaml_files_list)
y_dow_symbol = func_main.dow_yesterday(1)
dow_dict_set = func_main.alt_dow(yaml_dict_strings, "dow", y_dow_symbol)
arg_dict_set = func_main.alt_arg(yaml_dict_strings, "contents", arg_str)

# print(dow_dict_set)
# print(arg_dict_set)
# sys.exit()

if   arg_str == "dow":
  func_main.sub(dow_dict_set, y_dow_symbol)
elif arg_str == arg_dict_set[0]["yyyy"]:
  func_main.sub(arg_dict_set, y_dow_symbol)
