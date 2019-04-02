times = int(input("enter number to count factorial\t\t"))
l = [1]
for x in range(2,times+1):
    l.append(l[-1]*x)
print(l)










