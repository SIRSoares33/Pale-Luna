from termcolor import colored
from colorama import Fore, init
from time import sleep
from sys import stdout
from re import search

class Configs:
    # __slots__ = ("colors")
    
    def __init__(self) -> None:
        pass

    init(convert=True)
    def animation(self, var: str) -> None:
        if var == "Você Perdeu":
            color = Fore.RED
        elif search("Pegou", var):
            color = Fore.GREEN
        else:
            color = Fore.WHITE

        list_var = [broken for broken in var]
        for n in list_var:
            stdout.write(colored(f"{color}{n}{Fore.RESET}"))
            stdout.flush()
            sleep(.1)