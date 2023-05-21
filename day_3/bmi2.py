#!/usr/bin/env python3

#this program calculates the Body Mass Index from user's weight and height and the corresponding interpretation

# Prompt the user to enter weight and height
weight = float(input("Weight(kg): "))
height = float(input("Height(m): "))

# Calculate BMI
bmi = round(weight / (height ** 2), 1)

# Interpret BMI and provide suggestions
if bmi < 18.5:
    interpretation = "You are underweight. Consider consulting a healthcare professional."
elif bmi < 25:
    interpretation = "You have a normal weight. Maintain a healthy lifestyle."
elif bmi < 30:
    interpretation = "You are overweight. Focus on exercise and a balanced diet."
elif bmi < 35:
    interpretation = "You are obese. It is recommended to seek medical advice."
else:
    interpretation = "You are clinically obese. Consult a healthcare professional for guidance."

# Print BMI and interpretation
print(f"Body Mass Index (kg/m^2): {bmi}")
print(interpretation)

