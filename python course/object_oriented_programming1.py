#quadratic function


import math

class QuadraticFunction():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    #methods of class

    def write_form(self):
        print(f"{self.a}*x^2+{self.b}*x+{self.c}")

    def count_value(self, x):
        return self.a * x * x + self.b * x + self.c

    def solve(self):
        if self.a == 0 and self.b == 0:
            if self.c == 0:
                return float("inf"), float("inf")

            else:
                return float("nan"), float("nan")

        if self.a == 0:
            return -self.c/self.b, -self.c/-self.b


        delta = self.b**2 - 4*self.a*self.c

        if delta < 0:
            return float("nan"), float("nan")
        return(-self.b - math.sqrt(delta))/(2*self.a), (-self.b + math.sqrt(delta))/(2*self.a),

def main():
    f1 = QuadraticFunction(2, 3, 1)        #creating object
    f1.write_form()
    print(f1.count_value(0))
    print(f1.count_value(1))

    print(QuadraticFunction(0, 0, 0).solve())
    print(QuadraticFunction(0, 0, 1).solve())
    print(QuadraticFunction(0, 2, 3).solve())
    print(QuadraticFunction(1, -5, 6).solve())
    print(QuadraticFunction(1, 4, 4).solve())


main()


