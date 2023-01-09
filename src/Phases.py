from functions import Configs
from colorama import Fore
from re import search
import time
import os

class Phases:
    __slots__ = ("question", "dict_class", "list_objects", "inventory") #Armazenando os atributos da classe na memória

    def __init__(self) -> None:
        self.question = {} # dict: {fase_atual: [questions]}Lista que vai armazenar as perguntas
        self.inventory = {"Items": []} #Dicionario que vai funcionar como um inventario
        self.dict_class = {"Functions": [Configs()]} #dicionario com os objetos de cada classe
        self.list_objects = {"1": ["pegar ouro", "pegar corda", "pegar pá",],
                             "3": ["cavar", "esconder ouro", "tapar buraco"],
                             "2": ["norte", "sul", "oeste"]} #Lista de cada item da fase

    def validate_room(self, phase) -> None:
        try:
            self.question[phase] = []
            with open("src\questions.txt", "r", encoding="utf-8") as archive: #Abrindo o arquivo questions.txt
                for i in archive.readlines(): #Lendo linha por linha
                    if search(f"[{phase}]", i):
                        self.question[phase].append(i.replace(f"[{phase}] - ", "")) #Retirando os caracteres [1] - da frase, para poder adicionar na lista self.questions

                for count in range(len(self.question[phase])): #Passando pela lista self.question
                    self.dict_class["Functions"][0].animation(str(self.question[phase][count])) #Usando a função de animação nas perguntas armazenadas em self.question

        
            for i in range(3):
                
                command = str(input("\nComando? ")).lower()

                if command in self.list_objects[phase]: #Verificando se o usuario digitou algo que esta dentro da lista de objeto
                    self.list_objects[phase].remove(command)
                    self.inventory["Items"] = command #Armazenando item que o usuario pegou, dentro do inventario dele
                    
                    if phase == "1":
                        self.dict_class["Functions"][0].animation("Pegou.") #Função de animação
                    elif phase == "3":
                        self.dict_class["Functions"][0].animation("Feito.")
                    
                    print("\n")
                
                else:
                    quit()
            
            if phase == "1":
                os.system('cls')
                self.dict_class["Functions"][0].animation("Você pegou todos os itens... \nA luz da Lua infiltra-se por de baixo da porta...\n")
                
                open_door = str(input("\nComando? ")).lower()
                if open_door == "abrir porta":
                    self.dict_class["Functions"][0].animation("\nAbriu.")
                    time.sleep(3)
                    os.system("cls")
                else:
                    quit()
            
            if phase == "3":
                os.system("cls")
                while True:
                    print("       --PARABÉNS--")
                    print("--19°56'56.96″S, 69°38'1.83″W-- \n \n")
                    time.sleep(1)

        except KeyboardInterrupt:
            print(f"{Fore.RED}Programa Interrompido{Fore.RESET}")
    
    def florest_phase(self, phase):
        
        self.dict_class["Functions"][0].animation("Você dá de cara com a floresta. A Lua está sorrindo para você...\
        \nParece que o LESTE não é o único lugar para você ir.\n")

        for i in range(3):
            
            command = str(input("\nComando? ")).lower()

            if command in self.list_objects[phase]: #Verificando se o usuario digitou algo que esta dentro da lista de objeto
                self.list_objects[phase].remove(command)
            else:
                quit()
        
        os.system('cls')
            
    
obj_class = Phases()
