from sys import argv

script, filename = argv        #filename will be argument which you will write in command-prompt after name of the file

txt = open(filename)

print(f"Here is your file {filename}")

print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
print(txt_again.read())

txt_again.close()

