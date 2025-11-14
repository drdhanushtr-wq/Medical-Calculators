eye = int(input("Eye Response (1–4): "))
verbal = int(input("Verbal Response (1–5): "))
motor = int(input("Motor Response (1–6): "))

total = eye + verbal + motor

print("GCS Score:", total)

if total <= 8:
    print("Severe Head Injury")
elif total <= 12:
    print("Moderate Head Injury")
else:
    print("Mild Head Injury")
