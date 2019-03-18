height = float(input("Enter your height (in cm):\t"))
weight = float(input("Enter your weight (in kg):\t"))
age = int(input("Enter your age:\t"))
gender = str(input("Define your gender:\t"))
if gender == "man":
    s, index = 5,1.6
elif gender == "woman":
    s, index = -161,1.2
ppm = (10*weight + 6.25*height + 5*age + s)*index
print("Your daily caloric demand equals", ppm, "kcal")