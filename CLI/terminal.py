from typing import Self
from prolog.CLI.console import console

class CLI:
    def __init__(self: Self):
        self._console = console
        console.clear()

    #TODO: use key arrows to reuse previous commands
    def prompt(self: Self):
        return self._console.input(">>> ")