class Calculator():
    def __init__(self):
        self.ostatni_wynik = 0

    def dodaj(self, a, b):
        wynik = a + b
        self.ostatni_wynik = wynik
        print(wynik)
    def odejmij(self, a, b):
        wynik = a - b
        self.ostatni_wynik = wynik
        print(wynik)




calc = Calculator()
calc.dodaj(2, 3)
calc.dodaj(3, 4)
calc.odejmij(10, 5)

calc2 = Calculator()
calc2.dodaj(40, 40)
calc2.dodaj(150, 20)
import os
print("ostatni wynik calc : {}".format(calc.ostatni_wynik))
print("ostatni wynik calc2: {}".format(calc2.ostatni_wynik))