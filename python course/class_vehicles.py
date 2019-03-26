class Mojaklasa:
    zmienna = "xd"
    def funkcja(self):
        print("the message insise class")
    def __init__(self):
        print("start")
    def __del__(self):
        print("end")


mojobiekt = Mojaklasa()
print(mojobiekt.funkcja())

class Pojazd():
    name = ""
    color = ""
    type = ""
    value = int()
    def opis(self):
        opis = "{} is {} {} with value {} zl.".format(self.name, self.color, self.type, self.value)
        print(opis)
auto1 = Pojazd()
auto1.name = 'mazda'
auto1.color = 'black'
auto1.type = "hatchback"
auto1.value = 20000
print(auto1.opis())
auto2 = Pojazd()
auto2.name = 'bmw'
auto2.color = 'black'
auto2.type = 'combi'
auto2.value = 30000
print(auto2.opis())
