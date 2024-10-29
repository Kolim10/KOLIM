class Person:
    def __init__(self, name):
        self.name = name

    def move(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе.")

class Adilet(Person):
    def move(self):
        return f"{self.name} не сделал дз!"

class Atay(Person):
    def move(self):
        return f"{self.name} лучший студент!"

class Arafat(Person):
    def move(self):
        return f"{self.name} едет в Казахстан!"

def perform_move(character):
    print(character.move())

adilet = Adilet("Адилет")
atay = Atay("Атай")
arafat = Arafat("Арафат")

perform_move(adilet)  
perform_move(atay)   
perform_move(arafat) 
