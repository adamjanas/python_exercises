import os
a = open("justcreated.py", "w")
a.write("i am adam\n")
print(a.read(10))



os.rename("Obsługa plików.py", "file support.py")
os.remove("justcreated.py")
os.mkdir("nazwa")
import os
filename = 'writing variables in classes.py'
new_filename = filename.replace(' ', '_')
os.rename(filename, new_filename)
print(os.getcwd())   #gdzie sie znajduje na dysku aktualnie

'''for item in os.listdir(".")
        if os.path.isfile(item):
            print("{} jest plikiem".format(item))
            
        if os.path.isdir(item):
            print("{} jest folderem".format(item)''' #dir or file