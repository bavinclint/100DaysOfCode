# BMI Challenge

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / (height ** 2)

if bmi > 18.5:
    print(f"Your BMI is {round(bmi)}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {round(bmi)}, you have normal weight")
elif bmi < 30:
    print(f"Your BMI is {round(bmi)}, you are overweight")
elif bmi < 35:
    print(f"Your BMI is {round(bmi)}, you are obese")
else:
    print(f"Your BMI is {round(bmi)}, you are clinically obese")
