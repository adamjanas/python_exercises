f = open("plik.txt","r+")
f.write("i am adam \n")
print(f.read(10))
f.seek(10)                 #przechodzi dalej o ilosc znaków
print(f.read(10))
for line in f.readlines():
    print(line.rstrip())  #strip usuwa biale znaki
# r read, a+ all
f.close()



import os
lista = os.listdir(".")
for item in lista:
    if os.path.isfile(item):
        print("{} jest plikiem".format(item))
    if os.path.isdir(item):
        print("{} jest folderem".format(item))
os.remove("plik.txt")
