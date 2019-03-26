import random

def cows_and_bulls():
    random_number = random.randint(1000,9999)
    while True:
        guess = input('Guess a number:\n\n')
        if len(guess) != 4:
            print("Must be 4-digit")
            continue
        if guess == random_number:
            return f'Guessed correctly, {guess} == {random_number}'
        checking(random_number, guess)


def checking(random_number, guess):
    random_number, guess = str(random_number), str(guess)
    cows = len([cow for index, cow in enumerate(random_number) if guess[index] == cow])
    bulls = len(set([bull for bull in guess if bull in random_number])) - cows
    print(f'Cows: {cows}, bulls: {bulls}')


cows_and_bulls()
checking()








