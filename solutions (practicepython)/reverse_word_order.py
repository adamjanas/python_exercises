''' #exercises
teststring = "this is a test"
result = teststring.split("t") #removes from string t
print(result)
teststring1 = "this has a lot of spaces and tabs"
result1 = teststring1.split()  #makes one string sigle with many strings
print(result1[::-1])
print(result1)
list_of_strings = ['a', 'b', 'c', 'd']
result2 = "**".join(list_of_strings) #adds string between other strings
print(result2)'''




ask_for_string = str(input("write some sentence\n"))
reverse = ask_for_string.split()
print(reverse[::-1])