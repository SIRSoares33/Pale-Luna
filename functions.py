from time import sleep
from sys import stdout

class Configs:
    def __init__(self) -> None:
        pass

    def animation(var: str) -> str:
        list_var = [broken for broken in var]
        for n in list_var:
            stdout.write(n)
            stdout.flush()
            sleep(.1)

obj_class = Configs.animation("Pedro Donato")
