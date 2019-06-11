from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())          #it reads all file

def rewind(f):
    f.seek(0)                #it moves pointer to zero

def print_a_line(line_count, f):
    print(line_count, f.readline())         #it displays number of line and reads next lines of file

current_file = open(input_file)

print_all(current_file)

rewind(current_file)

current_line = 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)

current_file.close()


