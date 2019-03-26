'''import random
def password_generator():
    s = 'ABCDEFGHIJKMNOPRSTUWabcdefghijkmnoprstuw123456789!@#$%^&*()'
    ask = str(input("choose level of password\n weak medium or hard\n\n"))
    if ask == 'weak':
        pass_length = 5
    elif ask == 'medium':
        pass_length = 10
    elif ask == 'hard':
       pass_length = 15
    else:
        print("choose the level again bro")
    password = "".join(random.sample(s, pass_length))
    print(password)
password_generator()'''

import string
import random
#the variable a is the length of the password

def pass_word(a):
    password = ""

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    special = string.punctuation
    number = string.digits
    all = upper + lower + special + number
    password = random.sample(all, a)
    b = ''.join(password)

    print(b)


pass_word(30)



