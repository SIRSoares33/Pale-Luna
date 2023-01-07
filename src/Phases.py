from functions import Configs
from colorama import Fore
from re import search
import time
import os

class Phase_one:
    __slots__ = ("question", "dict_class", "list_objects", "inventory") #Armazenando os atributos da classe na memória

    def __init__(self) -> None:
        self.question = {} # dict: {fase_atual: [questions]}Lista que vai armazenar as perguntas
        self.inventory = {"Items": []} #Dicionario que vai funcionar como um inventario
        self.dict_class = {"Functions": [Configs()]} #dicionario com os objetos de cada classe
        self.list_objects = {"1": ["pegar ouro", "pegar corda", "pegar pá"]} #Lista de cada item da fase

    def validate_room(self, phase) -> None:
        try:
            self.question[phase] = []
            with open("src\questions.txt", "r", encoding="utf-8") as archive: #Abrindo o arquivo questions.txt
                for i in archive.readlines(): #Lendo linha por linha
                    if search(f"[{phase}]", i):
                        self.question[phase].append(i.replace(f"[{phase}] - ", "")) #Retirando os caracteres [1] - da frase, para poder adicionar na lista self.questions

                for count in range(len(self.question[phase])): #Passando pela lista self.question
                    self.dict_class["Functions"][0].animation(str(self.question[phase][count])) #Usando a função de animação nas perguntas armazenadas em self.question

            x = 0 
            while x != 3:
                
                command = str(input("\n==> ")).lower()

                if command in self.list_objects[phase]: #Verificando se o usuario digitou algo que esta dentro da lista de objetos
                    x += 1
                    self.list_objects[phase].remove(command)
                    self.inventory["Items"] = command #Armazenando item que o usuario pegou, dentro do inventario dele
                    self.dict_class["Functions"][0].animation("Pegou.") #Função de animação
                    print("\n")
                
                else:
                    quit()
            
            open_door = str(input("\n==> ")).lower()
            if open_door == "abrir porta":
                self.dict_class["Functions"][0].animation("Abriu.")
                time.sleep(3)
                os.system("cls")

        except KeyboardInterrupt:
            print(f"{Fore.RED}Programa Interrompido{Fore.RESET}")

obj_class = Phase_one()
obj_class.validate_room("1")
