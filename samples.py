#!/usr/bin/env python3
# author: Gabriel Auger
# version: 3.2.2
# name: prompt
# license: MIT

import sys, os
import importlib
direpa_script_parent=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
module_name=os.path.basename(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, direpa_script_parent)
prompt = importlib.import_module(module_name)
del sys.path[0]

prompt.msg.info("Basic Input, type empty to see the results")
print(prompt.prompt_multiple(["a", "b", "c", "d", "e", "f", "g", "h", "l", "m", "n", "o"], error_on_quit=False))
print(prompt.prompt_multiple(["banana", "apple"], error_on_quit=False))

print(prompt.prompt("Input your name"))
print()
print(prompt.prompt("Input your name:", exclude=["mike", "tom"]))

print(prompt.prompt("default input empty", default=""))
print()
print(prompt.prompt("default input with value", default="myvalue"))
print()

input("Press Enter to continue")

names=[ "banana", "raspberry", "pea" ]
values=["yellow", "red", "green"]

# print(prompt.prompt_multiple(names))

print(prompt.prompt_multiple(names,
    add_none=True,
    allow_duplicates=True,
    bullet=" # ",
    clear_error=True,
    clear_start=True,
    default="None",
    indent="  ___   ",
    return_list=True,    
    sort=False,
    title="Choose a fruit", 
    values=values,
))

# names,
# add_none=False,
# allow_duplicates=False,
# bullet=" - ",
# clear=False,
# default=None, 
# indent=" "*4, 
# index_only=False,
# return_list=False, 
# show_item_info=True,
# show_numbers=True, 
# sort=True, 
# title=None,
# values=[],

# print(prompt.prompt_boolean("Are you busy"))
# print(prompt.prompt_boolean("Are you busy",'n'))
# print(prompt.get_path("Choose path (autocomplete with tab)"))
prompt.msg.info("Hidden Field")
print(prompt.prompt("password", hidden=True))
prompt.pause()
