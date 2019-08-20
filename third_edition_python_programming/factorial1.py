#Program to compute the factorial of a number


def main():
    n = int(input("Enter number to count factorial:\t"))
    fact = 1
    for factor in range(n, 1, -1):
        fact = fact * factor
    print(f"The factorial of {n} is {fact}")


main()

