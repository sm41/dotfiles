import func_main
import os
import sys

mnt_env_var = "XDG_STATE_HOME"
jsonpath = os.getenv(mnt_env_var)

func_main.check_arg()
arg_str      = sys.argv[1]
json_set     = [ 'array_audio.json', 'array_video.json' ]
element_set  = [ 'array_element.json' ]
get_arg_set  = func_main.json_kit(jsonpath, json_set, "var", arg_str)


func_main.main(get_arg_set, jsonpath, element_set)