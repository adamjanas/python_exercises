''''#key symbols
#with-as statement
with open("test.txt") as ifile:
....print(infile.read())      #with-as statement allows us to not closing the file
#assert
def power(x,y):
    assert x > 0, f'x must be a positive number not {x}'
    assert y > 0, f'y must be a positive number not {y}'    #kind of AssertionError
    return x ** y

print(power(2,-2))

#conitnue in loops
for i in "python":
    if i == "h":
        continue
    print("current letter:", i)
var = 10
while var > 0:
   var -= 1
   if var == 5:
      continue
   print('Current variable value :', var)
print("Good bye!")
#del in dictionary
student = {'name':'adam', 'phone':'123-123-123'}
del student['phone']
print(student)
#exceptions example from /exceptions1.py
x = input("Enter first number:")
y = input("Enter second number:")
try:
    z = int(x)/int(y)
except ZeroDivisionError as e:
    print("exception occured", e)
    z = None
except Exception as e:
    print('exception type:', type(e).__name__)
    z = None
print(f"Division is {z}")
#exec ~ run a string as Python (dynamic performing code in python)
prog = 'print("The sum of 5 and 4 is",(5+4))'
exec(prog)
#finally  ~ Exceptions or not, finally do this no matter what
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        print(f"divison by zero !, {e}")
    else:
        print(f"result is {result}")
    finally:
        print("Excecutting finally closed")'''
# lamda ~ create a  short anonymous function
f = lambda arg1, arg2: arg1* arg2
print(f(3,4))

#or lambda into another function

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

