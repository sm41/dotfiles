import func_main
import os
import sys

json_env_var = "XDG_STATE_HOME"
jsonpath = os.getenv(json_env_var)

func_main.check_arg()
arg_str      = sys.argv[1]
json_dict_set  = [ 'array_audio.json', 'array_video.json' ]
json_elem_set  = [ 'array_element.json' ]
get_arg_set  = func_main.json_kit(jsonpath, json_dict_set, "var", arg_str)


func_main.main(get_arg_set, jsonpath, json_elem_set)