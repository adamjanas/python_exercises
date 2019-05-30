import math

class Fraction:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik


    def wypisz(self):
        print(f"({self.licznik})/({self.mianownik})")

    def skroc(self):
        nwd = math.gcd(self.licznik, self.mianownik)
        self.licznik //= nwd
        self.mianownik //= nwd
        print(f"({self.licznik})/({self.mianownik})")
def main():
    f1 = Fraction(10, 24)
    f1.wypisz()
    f1.skroc()


main()