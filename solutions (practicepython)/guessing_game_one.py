'''import random
while True:

    a = int(input("enter a digit from 1 to 9\n\n"))
    b = random.randint(1, 9)
    if a not in list(range(1,10)): #float('-inf') < a < 1 or 9 < a < float('inf')
        print("fault")
    elif a > b:
        print("too high")
    elif a < b:
        print("too low")
    else:
        print("good that s the same number congrats")
    print(b)'''

import random
number = random.randint(1,9)
guess = 0
count = 0
while guess != number:
    guess = int(input("what s your guess?"))
    if guess == -1:
        break
    count += 1
    if guess < number:
        print("too low")
    if guess > number:
        print("too high")

    else:
        print("you got it")
        print("it took you only", count, "tries")

