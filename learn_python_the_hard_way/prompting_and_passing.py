import sys

from sys import argv

print(sys.argv[0]) #name of the script

print(sys.argv[1]) #name of the argument

print(len(sys.argv)) #number of arguments

script, user_name = argv

print(f"Hi {user_name}, it is {script}")

