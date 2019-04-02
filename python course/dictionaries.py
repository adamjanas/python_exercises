student = {'name':'Adam', 'age':20, 'courses':['Math','Science']}
student['phone'] = '555-555-555'
student['name'] = 'Jane'       #update
student.update({'name':'John', 'age': 21})     #update
print(student['courses'])
print(student)
print(len(student))
print(student.keys())     #print the keys of dictionary
print(student.values())    #print values
print(student.items())      # The items are all parts: (key - value) etc.
for key, value in student.items():
    print(key, value)




