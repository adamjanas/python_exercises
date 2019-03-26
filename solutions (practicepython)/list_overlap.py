a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [2, 4, 6, 8, 9, 10]
c = []
for x in a:
    for y in b:
        if x == y:
            c.append(x)
print(c)
