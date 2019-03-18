"""Create script which will ask user about name,surname,phone_number
1) Check whether the regularity of name,surname,number is right
2) The first letter of name,surname should be big letter
3) Display all variables (name, surname, number) in one string "personal"
4) Check whether the user is woman
5) Display the phone-number without spaces
6) Count the whole sings in variable "personal"
7) Count the all letters in variable "personal" """

name = str(input("Enter your name\t\t"))
surname = str(input("Enter your surname\t\t"))
phone_number = input("Enter your phone-number\t\t")

print("Does the name include only letters?\t\t", name.isalnum())
print("Does the surname include only letters?\t\t", surname.isalnum())
print("Does the number include only digits?\t\t", phone_number.isdigit())

name = name.capitalize()
surname = surname.capitalize()
print(name, surname)

personal = name + " " + surname + " " + phone_number
print(personal)

print("The female name\t\t", name.endswith("a"))

phone_number = phone_number.replace(" ","").replace("-","")
print(phone_number)

print(len(personal))                        #amount of sings
print(len(personal)-personal.count(" "))    #amount of letters