x = input("Enter first number:")
y = input("Enter second number:")
try:
    z = int(x)/int(y)
except ZeroDivisionError as e:
    print("exception occured", e)
    z = None
except Exception as e:
    print('exception type:', type(e).__name__)
    z = None
print(f"Division is {z}")



