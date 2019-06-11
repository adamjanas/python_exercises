from sys import argv

'''script, arg1, arg2 = argv

def print_two(arg1, arg2):                                  #for two arguments

    print(f"argument1 --> {arg1}, argument2 --> {arg2}")
'''


#for more arguments
script, *args = argv

def print1(*args):
    x = 0
    for arg in args:
        x += 1
        print(f"argument{x} ----> {arg}")


print1(*args)
