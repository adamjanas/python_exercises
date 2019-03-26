"""years_of_birth = [1999, 1992, 1998, 2000, 1987]
ages = []
for year in years_of_birth:
    ages.append(2019-year)
print(ages)"""
year_of_birth = [1999, 2000, 2001, 1999, 1987, 1988]
ages = [2019 - year for year in year_of_birth]
print(ages)
#list comprehensions

a = [1, 4, 5, 6, 7, 8, 9]
b = [0 - digit for digit in a]
print(b)

c = [2, 3, 5, 6, 8, 9, 10, 19, 20, 22]
d = [number for number in c if number % 2 == 0]
print(d)

