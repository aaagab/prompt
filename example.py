#!/usr/bin/env python3
import prompt as prompt
import modules.message.message as msg

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
prompt.get_path("Choose path (autocomplete with tab)")
