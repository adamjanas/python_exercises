name = input("give ur name please:")
print("your name is " + name)   # return ur name

age = int(input("enter your age please:"))

print("thats your age " + str(age))



if age >= 18:
    print("correct")

elif 12 <= age <= 18:
    print("sorry dude")
else:
    print("too young")