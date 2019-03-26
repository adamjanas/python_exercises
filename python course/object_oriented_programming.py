class Calculator():

    def __init__(self):
        print("init")     #printuje cos gdy program sie rozpoczyna

    def __del__(self):     #printuje cos gdy program sie konczy
        print("del")

    def __str__(self):
        return "xdxdxd"

    def __int__(self):
        return 10

    def __len__(self):      # dlugosc kalkulatora
        return 22

    def __bool__(self):     #jezeli calculator to true
        return True

    def dodaj(self, a, b):
        wynik = a + b
        print(wynik)

    def odejmij(self, a, b):
        wynik = a - b
        print(wynik)


calc = Calculator()

calc2 = Calculator()

wynik = int(calc) + 50
print(wynik)