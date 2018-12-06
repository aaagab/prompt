#!/usr/bin/env python3
# author: Gabriel Auger
# version: 1.0.0-draft-1543082164
# name: prompt
# license: MIT


import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
import prompt as prompt
import modules.message.message as msg
del sys.path[0:2]

msg.info("Basic Input, type empty to see the results")
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
