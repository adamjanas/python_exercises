"""On base of three length a,b,c - check
1) Whether these length are the arms of the triangle
2) Whether it is pythagorean triangle
3) Whether it is egyptian triangle

Pythagorean triangles: [3, 4, 5], [6, 8, 10], [5, 12, 13], [9, 40, 41], [8, 15, 17]
Egyptian triangles: [9, 12, 15], [3, 4, 5], [15, 20, 25], [6, 8, 10]"""

a = int(input("Enter first length -\t"))
b = int(input("Enter second length -\t"))
c = int(input("Enter third length -\t"))

if (a + b > c) and (a + c > b) and (c + b > a):
    print("These lengths will create the triangle")
    if (c ** 2 == a ** 2 + b ** 2):
        print("Pythagorean triangle")
        if (a / 3 == b / 4 == c / 5):
            print("Egyptian triangle")
    else:
        print("Thats not the pythagorean triangle")
else:
    print("Fault, Wrong values")

