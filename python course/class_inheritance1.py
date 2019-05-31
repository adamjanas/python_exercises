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

class Cat(Mammal):
    def __init__(self):
        Mammal.__init__(self)
        print("cat")
    def purr(self):
        print("purr")






mammal_1 = Mammal()
mammal_1.introduce_yourself()
mammal_1.increase_age()


cat_1 = Cat()
cat_1.purr()
cat_1.increase_age()
cat_1.introduce_yourself()

