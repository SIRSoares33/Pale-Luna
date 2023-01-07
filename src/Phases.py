from functions import Configs

class Phase_one:
    __slots__ = ("question", "dict_class", "list_objects", "inventory") #Armazenando os atributos da classe na memória

    def __init__(self) -> None:
        self.question = [] #Lista que vai armazenar as perguntas
        self.inventory = {"Items": []} #Dicionario que vai funcionar como um inventario
        self.dict_class = {"Functions": [Configs()]} #dicionario com os objetos de cada classe
        self.list_objects = ["pegar ouro", "pegar corda", "pegar pá"] #Lista de cada item da fase 1

    def room(self):
        with open("src/questions.txt", "r", encoding="utf-8") as archive: #Abrindo o arquivo questions.txt
            for i in archive.readlines(): #Lendo linha por linha
                self.question.append(i.replace("[1] - ", "")) #Retirando os caracteres [1] - da frase, para poder adicionar na lista self.questions
            
            for phase1 in self.question: #Passando pela lista self.question
                self.dict_class["Functions"][0].animation(phase1) #Usando a função de animação nas perguntas armazenadas em self.question

        command = str(input("\n==> ")).lower()

        if command in self.list_objects: #Verificando se o usuario digitou algo que esta dentro da lista de objetos
            self.inventory["Items"] = command #Armazenando item que o usuario pegou, dentro do inventario dele
            self.dict_class["Functions"][0].animation("Você Pegou") #Função de animação

obj_class = Phase_one()
obj_class.room()