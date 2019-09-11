#Simple string processing program to generate usernames

def main():
    print("This program generates computer usernames.\n")


    #get user's first and last names
    first = str(input("Please enter your fist name (all lowercase):\t"))
    last = str(input("Please enter your last name (all lowercase):\t"))

    #concatenate first initial with 7 chars of the last name.

    uname = first[0] + last[:7]

    print(f"Your username is {uname}")

main()
