from sys import argv

script, filename = argv

print(f"we're going to erase {filename}")
print("If you don't want that, hit CTRL-C.")
print(f"If you do want that, hit (enter)")
input("Continue?\t")

print("Opening the file...")

target = open(filename, 'r+')



print("Truncating the file.")
target.truncate()

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")



target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

target.seek(0)
print(target.read())

print("I'm going to write these to the file...")

print("Finally we close it")
target.close()

