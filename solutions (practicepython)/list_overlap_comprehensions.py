a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
'''for x in a:
    for y in b:
        if x == y:
            c.append(x)
print(c)
print([x for x in a if x in a and x in b])

print(set(a) & set(b)) # return wihout duplicats
x = [1, 2, 3]
y = [5, 10, 15]
allproducts = [a*b for a in x for b in y]
print(allproducts)
print([a/b for a in x for b in y])

print([a+b for a in x for b in y])
'''
numbers = [1, 2, 3, 4, 5]
a = []
for x in numbers:
    if x % 2 == 1:
        a.append(x*2)
print(a)

a = [x*2 for x in numbers if x % 2 == 1]    #alternative version by list_comprehensions
print(a)