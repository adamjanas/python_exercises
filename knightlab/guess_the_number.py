import random
number = random.randint(1,9)
count = 0
guess = 0
while guess != number:
    guess = int(input('Guess the number\n\n'))
    if guess == -1:
        break
    count += 1
    if guess < number:
        print('too low')
    elif guess > number:
        print('too high')
    else:
        print('you got it\n\n', 'it took you only', count, 'tries')


