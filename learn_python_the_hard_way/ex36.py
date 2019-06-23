from sys import exit


def start():
    print("You're in the dark room. There are a three door. Which one do you take? (left/straight/right)")
    choice = str(input("> "))
    if choice == "left":
        minotaur_room()
    elif choice == "straight":
        spider_room()
    elif choice == "right":
        hydra_room()
    else:
        print("You stumble around the room until you starve.")
        start()

def minotaur_room():
    print("This is a minotaur there!")
    print("What are you gonna to do? \nSing a song to put him to the sleep? or fight with him?")
    choice = str(input("> "))

    if choice == "sing a song":
        print("Great he sleeps. There is a secret door behind him.\nDo you wanna move him to open them?\nyes or no")
        decision = input(">")
        if decision == "yes":
            diamond_room()
        elif decision == "no":
            print("Minotaur woke up and killed you!")
            dead("minotaur")
        else:
            print("Learn how to type man, it took to many time! Minotaur woke up. You have to  run away.")
            start()

def diamond_room():
    print("You are in the diamond room! How many diamonds do you take?")

    how_many = input("> ")


    if how_many.isalpha() is True:
        print("learn how to type number man\nso again...")
        diamond_room()
    else:
        how_many1 = int(how_many)
        if how_many1 <= 10:
            print("Okay you won. You're not greedy")
        else:
            print("You are greedy bastard! You fall to the dark room!")
            start()
def dead(why):
    print(f"You died because of {why}")
    exit(0)

#optionallities
def spider_room():
    print("There is a big spider in this room? Do you wanna fight or go back?")

    choice = input("> ")

    if choice == "go back":
        start()
    elif choice == "fight":
        dead("spider")
def hydra_room():
    print("There is a hydra in this room. What are going to do?\nstay or go back?")

    choice = input("> ")

    if choice == "stay":
        dead("hydra")
    elif choice == "go back":
        start()
start()