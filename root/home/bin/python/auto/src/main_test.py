import func_main
import os
import sys

func_main.check_arg()
json_env_var = "XDG_STATE_HOME"
jsonpath = os.getenv(json_env_var)
arg_str  = sys.argv[1]

json_dict_set  = [ 'array_audio.json', 'array_video.json' ]

y_dow_symbol = func_main.dow_yesterday(1)
y_dict_set   = func_main.json_kit(jsonpath, json_dict_set, "dow", y_dow_symbol)
get_arg_set  = func_main.json_kit(jsonpath, json_dict_set, "var", arg_str)


if   arg_str == "dow":
  func_main.main(y_dict_set, jsonpath)
elif get_arg_set == []:
  print("No")
elif arg_str == get_arg_set[0]["var"]:
  func_main.main(get_arg_set, jsonpath)

