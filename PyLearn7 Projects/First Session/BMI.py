# Input Weight in Kg
weight = float(input("Weight in Kg = "))

# Input Height in Meter
height = float(input("Height in Meter = "))

# Handling Improper values for Height and Weight
if height >= 2.2 or height <= 0.25 or weight <= 0.5 or weight >= 220:
    print("Please Insert Correct Height and Weight")

else:
    BMI = weight / (height ** 2)

    if BMI <= 18.5:
        print(f"Your BMI is {round(BMI, 3)} and You are Underweight")
    elif 18.5 < BMI <= 24.9:
        print(f"Your BMI is {round(BMI, 3)} and You are Normal")
    elif 25 < BMI <= 29.9:
        print(f"Your BMI is {round(BMI, 3)} and You are Overweight")
    elif 30 < BMI <= 34.9:
        print(f"Your BMI is {round(BMI, 3)} and You have Obesity")
    elif 35 < BMI <= 39.9:
        print(f"Your BMI is {round(BMI, 3)} and You have Extreme Obesity")
