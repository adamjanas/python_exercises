class Parent():
    def __init__(self):
        print("Parent init")             #wykonuje sie to bo deklarujemy nowa instancje klasy

    def parent(self):
        print("Parent parent")

    def poke(self):
        print("Parent poked")

class Child(Parent):

    def __init__(self):
        super().__init__()
        print("child init")

    def poke(self):
        print("child poked przed")
        super().poke()            #kolejnosc wykonywania funkcji(przechodzi do klasy parent (funkcji poke))
        print("child poked po")

child = Child()       #tworzacnowa instancje klasy wykonuje sie init zas super przenosi nas na poczatek klasy
child.poke()
child.parent()

'''class Klasa1():
    def wypisz1(self):
        print("klasa1")
class Klasa2(Klasa1):
    def wypisz2(self):
       print("Klasa potomna")






obiekt = Klasa2()
obiekt.wypisz1()
obiekt.wypisz2()
'''


