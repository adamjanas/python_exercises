word = str(input("enter your word wheter its palindrome:"))
reversal = word[::-1]
print(reversal)
if reversal == word:
    print("its palindrome")
else:
    print("it inst palindrome")
    