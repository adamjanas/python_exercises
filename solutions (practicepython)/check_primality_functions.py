while True:
    number = int(input("enter number please to check primality\n\n"))
    divisor_list = []
    range_list = list(range(1, number+1))
    for x in range_list:
        if number % x == 0:
            divisor_list.append(x)
    print(divisor_list, "thats the divisors")
    if divisor_list == [1, number]:
        print("its a prime number")
        break
