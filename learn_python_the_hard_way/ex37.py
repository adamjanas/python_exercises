#key symbols
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