import func_main
import os


json_env_var = "XDG_STATE_HOME"
jsonpath = os.getenv(json_env_var)


y_dow_symbol = func_main.dow_yesterday(1)
json_dict_set  = [ 'array_audio.json', 'array_video.json' ]
json_elem_set  = [ 'array_element.json' ]
y_dict_set   = func_main.json_kit(jsonpath, json_dict_set, "dow", y_dow_symbol)


func_main.main(y_dict_set, jsonpath, json_elem_set)