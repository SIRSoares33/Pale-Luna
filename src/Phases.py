from functions import Configs

class Phase_one:
    __slots__ = ("question", "dict_class", "list_objects", "inventory")

    def __init__(self) -> None:
        self.question = []
        self.inventory = {"Items": []}
        self.dict_class = {"Functions": [Configs()]}
        self.list_objects = ["pegar ouro", "pegar corda", "pegar pá"]

    def room(self):
        with open("src/questions.txt", "r", encoding="utf-8") as archive:
            for i in archive.readlines():
                self.question.append(i.replace("[1] - ", ""))
            
            for phase1 in self.question:
                self.dict_class["Functions"][0].animation(phase1)

        command = str(input("\n==> ")).lower()

        if command in self.list_objects:
            self.inventory["Items"] = command
            self.dict_class["Functions"][0].animation("Você Pegou")

obj_class = Phase_one()
obj_class.room()