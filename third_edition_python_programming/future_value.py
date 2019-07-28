#A program to compute the value of an investment
#carried 10 years into the future
def main():
    amount = float(input("Enter amount of money for investment\t\t"))
    percentage = float(input("Enter percentage of investment\t\t"))
    years = int(input("For how many years?\t\t"))

    for i in range(1, years+1):
        amount = amount*(1 + percentage)
        print(round(amount, 2))

    print(f"Amount of money after {years} years is {round(amount,2)}")



main()

