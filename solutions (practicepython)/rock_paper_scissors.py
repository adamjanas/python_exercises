
user1 = input("please choose rock,paper or scissors\n\n")
user2 = input("please choose rock paper or scissors\n\n")

choices = ["paper", "rock","scissors"]
p1 = choices.index(user1)
p2 = choices.index(user2)
if p1 == p2:
    print("its a draw")
elif p2 == (p1 + 1) % 3:
    print("user 1 won")
elif p1 == (p2 + 1) % 3:
    print("user 2 won")




