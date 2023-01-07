from functions import Configs
from colorama import Fore
from re import search

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

            command = str(input("\n==> ")).lower()

            if command in self.list_objects[phase]: #Verificando se o usuario digitou algo que esta dentro da lista de objetos
                self.inventory["Items"] = command #Armazenando item que o usuario pegou, dentro do inventario dele
                self.dict_class["Functions"][0].animation("Você Pegou") #Função de animação
                print("\n")
        except KeyboardInterrupt:
            print(f"{Fore.RED}Programa Interrompido{Fore.RESET}")

obj_class = Phase_one()
obj_class.validate_room("1")
obj_class.validate_room("2")