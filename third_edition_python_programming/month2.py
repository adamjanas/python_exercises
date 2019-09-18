#A program toprint the month abbreviation, given its number.


def main():
    months = ["Jan", "Feb", "March", "April", "May", "June",
              "July", "August", "Sep", "Oct", "Nov", "Dec"]

    n = int(input("Enter a month number (1-12):  "))

    print(f"The month abbreviation is {months[n-1]}.")

main()


