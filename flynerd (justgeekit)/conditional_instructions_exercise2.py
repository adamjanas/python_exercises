""" Three default numbers save to three variables.
1) Find the largest number
2) Display numbers from the largest to smallest"""

print("Write three different numbers")
x = int(input("Enter x number\t\t"))
y = int(input("Enter y number\t\t"))
z = int(input("Enter z number\t\t"))

if (x > y) and (x > z):
    print("x = ", x, " ~ maximum")
elif (y > x) and (y > z):
    print("x = ", y, " ~ maximum")
else:
    print("z = ", z, " ~ maximum")

sequence = []

if x > y and x > z:
    sequence.append(x)
    if y > z:
        sequence.append(y)
        sequence.append(z)
    else:
        sequence.append(z)
        sequence.append(y)
    print(sequence)

if y > z and y > x:
    sequence.append(y)
    if z > x:
        sequence.append(z)
        sequence.append(x)
    else:
        sequence.append(x)
        sequence.append(z)
    print(sequence)

if z > y and z > x:
    sequence.append(z)
    if y > x:
        sequence.append(y)
        sequence.append(x)
    else:
        sequence.append(x)
        sequence.append(y)
    print(sequence)