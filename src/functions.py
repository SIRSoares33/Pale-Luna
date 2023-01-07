from time import sleep
from sys import stdout

class Configs:
    __slots__ = ("colors")
    
    def __init__(self) -> None:
        self.colors = {"red": "\033[01;31m",
                        "white": "\033[1;37m",
                        "endcolor": "\033[0m"
                        }

    def animation(self, var: str) -> str:
        if var == "You Lost":
            color = self.colors["red"]
        else:
            color = self.colors["white"]

        list_var = [broken for broken in var]
        for n in list_var:
            stdout.write(f"{color}{n}{self.colors['endcolor']}")
            stdout.flush()
            sleep(.1)

obj_class = Configs()
obj_class.animation("You Lost")
