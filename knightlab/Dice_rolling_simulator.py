import random


def dice():
    while True:
        number = random.randint(1, 6)
        a = str(input('press roll to generate digit or write (close) to quit \n\n'))
        if a == 'roll':
            print('your number is', number)
        if a == 'close':
            break


dice()
