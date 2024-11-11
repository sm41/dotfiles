
import array_audio, array_video, array_element
import func_main




y_dow_symbol = func_main.dow_yesterday(1)
module_set   = [ array_video, array_audio ]
element_set  = [ array_element ]
y_dict_set   = func_main.get_tuple(module_set, "dow", y_dow_symbol)


func_main.main(y_dict_set)