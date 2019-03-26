a = [1, 2, 3, 3, 4, 5, 6, 7, 7]
b = a
print(b)
print(set(a) & set(b))


names = ["aaa", "bbb", "ccc", "aaa"]
names1 = list(names)
names2 = set(names)
print(names1, names2)

x = [2, 3, 3, 4]
y = set(x)
print(y)