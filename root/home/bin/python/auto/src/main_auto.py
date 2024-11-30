# import array_element
import func_main
import os


mnt_env_var = "XDG_STATE_HOME"
jsonpath = os.getenv(mnt_env_var)


y_dow_symbol = func_main.dow_yesterday(1)
json_set     = [ 'array_audio.json', 'array_video.json' ]
element_set  = [ 'array_element.json' ]
y_dict_set   = func_main.json_kit(jsonpath, json_set, "dow", y_dow_symbol)


func_main.main(y_dict_set, jsonpath, element_set)