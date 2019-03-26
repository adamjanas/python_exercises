num = int(input("Please choose a number to divide:"))
list_range = list(range(1, num+1))
divisor_list = [number for number in list_range if num % number == 0]
print(divisor_list)


