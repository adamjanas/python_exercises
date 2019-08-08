import math


def sphere():
    radius = float(input("Enter the radius of sphere (in cm):\t"))

    v = 4/3 * math.pi * radius**3
    s = 4 * math.pi * radius**2

    print(f"Volume of sphere is {v} cm3, surface is {s} cm2")



def pizza_cost():
    print("Cost per square inch of pizza is 1.5$")

    radius = float(input("Enter the radius of pizza (in inches):"))

    s = math.pi * radius**2

    price = s * 1.5

    print(f"Price for the {s} inch2 of pizza is {price} $")

def thunder_distance():
    sec = float(input("How many seconds elapsed between the flash and the sound of thunder? : \t"))

    distance = 1100 * sec

    in_miles = distance / 5280

    print(f"The distance to thunder is {round(distance,4)} ft. It is about {round(in_miles, 4)} miles.")



def points_distance(x1,x2,y1,y2):
    distance = math.sqrt((x2-x1)**2 + (y2 - y1)**2)
    print(f"distance between points A{(x1,x2)} and B{(y1,y2)} is {distance}")


def lentgth_of_ladder():
    height = float(input("Enter the height of the house (in meters):\t"))
    angle = float(input("Enter the angle of the ladder:\t"))

    length = height / math.sin(angle)


    print(f"The length of the ladder will be {length} meters")

def sum_of_n():
    n = int(input("Write number to compute the sum of n natural numbers:\t"))
    sum = 0
    for i in range(1, n+1):
        sum = i + sum
    print(f"The sum of n numbers will be {sum}")



def sum_of_given_inputs():
    how = int(input("How many numbers do you want to sum?\t"))

    list = []
    count = 0
    s = 0

    while count != how:
        number = float(input("Enter number to sum:\t"))
        list.append(number)
        count += 1

    for i in list:
        s = s + i
    print(s)
sum_of_given_inputs()



