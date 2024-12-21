import func_main
# import os
import sys

func_main.check_arg()
arg_str  = sys.argv[1]

data_env_var = "XDG_STATE_HOME"
storage_path = "CLIENT_LOCAL_STORAGE"
yaml_files_list = [ 'audio.yaml', 'video.yaml' ]

yaml_dict_str = func_main.anlys(yaml_files_list, data_env_var)
y_dow_symbol  = func_main.dow_yesterday(1)
dow_dict_set  = func_main.alt_dow(yaml_dict_str, "dow", y_dow_symbol)
arg_dict_set  = func_main.alt_arg(yaml_dict_str, "contents", arg_str)

# print(dow_dict_set)
# print(arg_dict_set)
# sys.exit()

if   arg_str == "dow":
  func_main.sub(dow_dict_set, y_dow_symbol, storage_path)
elif arg_str == arg_dict_set[0]["yyyy"]:
  func_main.sub(arg_dict_set, y_dow_symbol, storage_path)
