#A program that computes the real roots of quadratic equation.
#Illustrates use of the math library.
#Note: The program crashes if th program has no roots.


import math


def main():
    print("This program finds the solutions of a quadratic equation\n\n")

    a = float(input("Enter a coefficient:\t\t"))
    b = float(input("Enter b coefficient:\t\t"))
    c = float(input("Enter c coefficient:\t\t"))

    delta_root = math.sqrt(b**2 - 4 * a * c)

    root1 = (-b - delta_root) / 2 * a
    root2 = (-b + delta_root) / 2 * a

    print(f"\nThe solutions of given coefficients are: {root1}, {root2}")

main()


