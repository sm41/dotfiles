#!/usr/bin/python3

from array_dir import array_audio, array_video, array_element
import func_main
import sys


func_main.check_arg()
arg_str      = sys.argv[1]
module_set   = [ array_video, array_audio ]
element_set  = [ array_element ]
vvvv = func_main.get_tuple(module_set, "var", arg_str)


func_main.main(vvvv)