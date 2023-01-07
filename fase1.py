from perguntas import perguntas
from animation_function import animation

class fase1:
    def sala(self):

        animation(perguntas[0])
        print("\n")
        self.comando = input("  Comando? ").lower()

        self.lista_objetos = ["pegar ouro", "pegar corda", "pegar pá"]

        if self.comando in self.lista_objetos:
            print("\n")
            print(f"Pegou.")



fase = fase1()
fase.sala()