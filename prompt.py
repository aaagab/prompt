#!/usr/bin/env python3
# author: Gabriel Auger
# version: 0.2.0
# name: prompt
# license: MIT

import sys
import os
import shlex

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
import modules.message.message as msg
del sys.path[0:2]

def prompt(txt, allow_empty=False):
    tmp_var=""
    while not tmp_var:
        tmp_var = input("  "+txt +" [q to quit]: ")
        if tmp_var.lower() == "q":
            sys.exit(1)
        if allow_empty:
            if not tmp_var:
                return ""

    return tmp_var.strip()

def prompt_multiple(choices):
    prompt_text="\n"
    space="    "
    for i ,item in enumerate(choices["items"]):
        prompt_text+="{}{} - {}\n".format(space, i+1, item)

    print(prompt_text)
    if choices.get("title"):
        prompt_text="{}{}".format(space, choices["title"])
    else:
        prompt_text="{}select entry".format(space)

    user_input=""
    while not user_input:
        user_input = input(prompt_text+" [q to quit]: ")
        if user_input.lower() == "q":
            sys.exit(1)

        if user_input.isdigit():
            if int(user_input) >= 1 and int(user_input) <= len(choices["items"]):
                print()
                if choices.get("values"):
                    return choices["values"][int(user_input)-1]
                else:
                    return choices["items"][int(user_input)-1]
            else:
                user_input=""
        else:
            user_input=""

def prompt_boolean(txt, Y_N="y"):
    tmp_var=""
    while not tmp_var:
        if Y_N.lower() == "y":
            tmp_var = input("  "+txt +" [Ynq]? ")
            if tmp_var.lower() == "":
                return True
        elif Y_N.lower() == "n":
            tmp_var = input("  "+txt +" [yNq]? ")
            if tmp_var.lower() == "":
                return False
        else:
            msg.app_error("Wrong Value for prompt_boolean: "+Y_N )
            sys.exit(1)

        if tmp_var.lower() == "q":
            sys.exit(1)
        elif tmp_var.lower() == "y":
            return True
        elif tmp_var.lower() == "n":
            return False

def get_path(txt, allow_empty=False):
    import subprocess
    filenpa_get_path=os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "get_path.sh"
    )
    txt="  "+txt +" [q]: "
    path=""
    while not path:
        path=subprocess.check_output(shlex.split("bash -c 'read -e -p \"{}\" text; echo \"$text\"'".format(txt))).decode("utf-8").rstrip()

        if path.lower() == "q":
            sys.exit(1)
        if allow_empty:
            if not path:
                return ""

    return path
    
