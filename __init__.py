#!/usr/bin/env python3
# author: Gabriel Auger
# version: 1.2.2
# name: prompt
# license: MIT
__version__ = "1.2.2"

from .dev.prompt import prompt, prompt_multiple, prompt_boolean, get_path
__all__ = [
    "prompt",
    "prompt_multiple",
    "prompt_boolean",
    "get_path",
]

from .gpkgs import message as msg
