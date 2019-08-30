# Fibonacci row 1 1 2 3 5 8 13 21...
def fib_gen():
    times = int(input("how many fibonacci number would you like to generate\t"))
    i = 1
    if times == 0:
        fib = []
    elif times == 1:
        fib = [1]
    elif times == 2:
        fib = [1, 1]
    elif times > 2:
        fib = [1, 1]
        while i < (times - 1):      #number of elements in list fib
            fib.append(fib[i] + fib[i-1])
            i += 1
    print(fib)

def fib_gen1():
    times = int(input('xd'))
    a, b = 0, 1
    while times:
        a, b = b, a+b

        times -= 1
        print(a)
fib_gen1()

def fib():
    times = int(input("how many fib numbers would you like to generate"))
    i = 1
    if times ==0:
        fib = []
    elif times == 1:
        fib = [1]
    elif times == 2:
        fib = [1,1]
    elif times > 2:
        fib = [1,1]
        while i < (times -1):
            fib.append(fib[i] + fib[i-1])
            i +=1
    print(fib)

fib()