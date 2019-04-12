#!/usr/bin/env python3
# author: Gabriel Auger
# version: 1.0.0
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
print(prompt.prompt("Input your name"))

print(prompt.prompt_multiple(
    dict(
        title="Choose a fruit",
        items=[
            "banana",
            "raspberry",
            "pear"
        ],
        values=[
            "yellow",
            "red",
            "green"
        ]
    )))

print(prompt.prompt_multiple(
    dict(
        items=[
            "banana",
            "raspberry",
            "pear"
        ],
    )))
print(prompt.prompt_boolean("Are you busy"))
print(prompt.prompt_boolean("Are you busy",'n'))
print(prompt.get_path("Choose path (autocomplete with tab)"))
