"""Next part of the bmi_calculator. We are going to make the interpretation of the bmi_index result.
Underweight     <18.5
Normal weight   18.5 - 24
Slight overweight 24 - 26.5
Overweight          26.5 - 30
Obesity  I          30-35
Obesity II          35-40
Obesity III         >40
"""

height = float(input("Enter your height (in meters):\t"))
weight = float(input("Enter your weight (in kg):\t"))
bmi = weight/(height**2)
print("Your BMI index is:\t", bmi)
if bmi <= 18.5:
    print("it is underweight")
elif 18.5 < bmi <= 24:
    print("Normal weight")
elif 24 < bmi <= 26.5:
    print("Slight overweight")
elif 26.5 < bmi <= 30:
    print("Overweight")
elif 30 < bmi < 35:
    print("Obesity I level")
elif 35 < bmi < 40:
    print("Obesity II level")
else:
    print("Obesity III level")