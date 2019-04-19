a = "python"
print(a.swapcase())    #small to bigger/ big to smaller
print(a.lower())
print(a.upper())
print(a.capitalize())  #first into bigger
print(a.title())
print("hello world".strip("h"))  #removing left/right sings
print(len(a))
print(a.count("a"))
print(a.count("a", 3,10))  #counting "a" behind third and tenth place
print(a.find("k"))    # or rfind it works by the end of strings of characters
print(a.replace("","-"))
print("*".join(a))
print(a.isalpha())      #print true if string of characters is a letter
print(a.isalnum())      # print true if (aplhanumeric sings)
print(a.isdigit())      # print true if (all digit)
print(a.islower())      #print true if (all low letters)
print(a.isspace())      #print true if ( only empty sings in string)
print(a.istitle())      #print true if string is a title
print(a.isupper())      #print true if the string includes one big letter
print(a.replace("p", "l"))
print(a.endswith("a"))  #print true  if strings end with "a" letter
print(a.startswith("a")) # --/-- which begins with letter "a"
print(a.strip("a"))    #it deletes letter "a" on the left and right side [we can use lstrip to left and rstrip to right side]
print(r"without functions like \n \t")
print(a.split(","))    #it divides string in base of (,), split() divides every word in string
print(sorted([1, 6, 2, 9, 3, 5, 2, 7], reverse = True))
print(round(12.3141592326, 2)) #it rounds places after point
print(format(b, '.50f'))        #it displays amount of numbers after point
print("%.50f" % b)              #the same (alternative)