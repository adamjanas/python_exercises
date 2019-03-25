""" Write program which will display cubed every 10 numbers"""
number = int(input("Enter the number\t\t"))
for i in range(1,number + 1):
    print(i*i*i)

"Let the user write some names in one string. Write code which wil greet every person (by name)"
names = str(input("Write a few names\n"))
for i in names.split():
    print('hi ' + i)
