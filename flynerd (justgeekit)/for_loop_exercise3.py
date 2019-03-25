"""Write program which will ask user about how many timesthe loop will go and  additionally
about number and check whether this number
is divisible by 3 and 4, only 3 and only 4. if number is not divisible print *"""

times = int(input('How many times the loop will work?\t'))

for i in range(1, times + 1):
    n1 = int(input('Enter the number\t'))
    if n1 % 4 == 0 and n1 % 3 == 0:
        print("divisible by 3 and 4")
    elif n1 % 3 == 0:
        print("dvisible by 3")
    elif n1 % 4 == 0:
        print("divisible by 4")
    else:
        print("*")