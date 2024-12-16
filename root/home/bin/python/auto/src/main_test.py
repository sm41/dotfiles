import func_main
import os
import sys

func_main.check_arg()
data_env_var = "XDG_STATE_HOME"
filepath = os.getenv(data_env_var)
arg_str  = sys.argv[1]

# json_dict_set = [ 'array_audio.json', 'array_video.json' ]
yaml_dict_set = [ 'array_audio.yaml', 'array_video.yaml' ]

y_dow_symbol = func_main.dow_yesterday(1)
# j_dict_set   = func_main.json_kit(filepath, json_dict_set, "dow", y_dow_symbol)
# get_arg_set  = func_main.json_kit(filepath, json_dict_set, "var", arg_str)

y_dict_set   = func_main.yaml_kit(filepath, yaml_dict_set, "dow", y_dow_symbol)


if   arg_str == "dow":
  func_main.sub(y_dict_set, y_dow_symbol)
# elif get_arg_set == []:
#   print("No")

sys.exit()
# if   arg_str == "dow":
#   func_main.main(j_dict_set, filepath)
# elif get_arg_set == []:
#   print("No")
# elif arg_str == get_arg_set[0]["var"]:
#   func_main.main(get_arg_set, filepath)

