'''  Notes about for_loop:
 for i in range(0,3):
    print("xd")
for m in "hehehehe":
    print("krok:", m)
for i in range(1,10):
    print(i * "#")
for s in range(0,3):
    for j in range(1,6):
        print(j * "#") '''

"""Write program which for given number will display sum of the all previous numbers"""
number = int(input("Enter number\t"))
s = 0
for i in range(1, number+1):
    s = s + i
    print(s)

