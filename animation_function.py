from time import sleep
from sys import stdout

def animation(var: str) -> str:
    list_var = [broken for broken in var]
    for n in list_var:
        stdout.write(n)
        stdout.flush()
        sleep(.1)

animation("Jogo De Enigma")