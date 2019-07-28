def main():
    print("Change counter\n")
    print("Please enter the count of each coin type.")
    quarters = int(input("Quarters:\t"))
    dimes = int(input("Dimes:\t"))
    nickels = int(input("Nickles:\t"))
    pennies = int(input("Pennies:\t"))

    total = float(.25*quarters + .10*dimes + .05*nickels + .01*pennies)

    print(f"The total value of your change is {round(total,2)}")

main()