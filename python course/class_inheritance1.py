class Animal:
    def __init__(self):
        print("animal")
    def increase_age(self):
        print("increase_age")

class Mammal(Animal):
    def __init__(self):
        Animal.__init__(self)      #inicjalizacja zmiennych z klasy bazowej (wywołujemy konstruktor klasy bazowej)
        print("mammal")
    def introduce_yourself(self):
        print("introduce yourself")

mammal_1 = Mammal()
mammal_1.introduce_yourself()
mammal_1.increase_age()


import os

os.rename("test.py", "class_inheritance1.py")