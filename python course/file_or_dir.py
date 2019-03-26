import os

lista = os.listdir(".")
for item in lista:
    if os.path.isfile(item):
        "{} jest plikiem".format(item)
    else:
        print("{} jest folderem".format(item))