class Person():
    def __init__(self, name, surname):   # wykonuje sie przy inicjalizacji instancji
        self.name = name
        self.surname = surname
        self.age = 25
        print('wykonanie sie przy ogarnieciu pierwszej instancji')
    def xddd(self):
        print("poczatek")


class Employee(Person):
    def __init__(self, name, surname, position):       #wykonuje sie przy inicjalizacji instancji
        super().__init__(name, surname)                # przepisuje funkcje z klasy do ktorej dziedzicze
        self.position = position
        print("druga instancja")
    def xddd(self):
        super().xddd()
        print('nadpisana')


xdd = Person("adam", "JANAS")
print(xdd.name)
print(xdd.surname)
haha = Employee('imie','nazwisko','pozycja')
print(haha.position)
haha2 = Employee('xd', 'xd', 'xd2')
print(haha.name)
print(haha2.name)
print(haha2.age)
print(haha.xddd())



import os

os.rename("objected_oriented_programming1.py", "object_oriented_programming1.py")