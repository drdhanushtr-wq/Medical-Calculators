height = float(input("Enter height (meters): "))
weight = float(input("Enter weight (kg): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    status = "Underweight"
elif bmi < 25:
    status = "Normal"
elif bmi < 30:
    status = "Overweight"
else:
    status = "Obese"

print("BMI:", round(bmi, 2))
print("Status:", status)
