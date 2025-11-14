weight = float(input("Enter weight (kg): "))

dose_mg_per_kg = float(input("Enter dose (mg/kg): "))

total_dose = weight * dose_mg_per_kg

print("Recommended Dose (mg):", round(total_dose, 2))
