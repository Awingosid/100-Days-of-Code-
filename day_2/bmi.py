#!/usr/bin/env python3

#this program calculates the Body Mass Index from user's weight and height
weight = float(input("Weight(kg): "))
height = float(input("Height(m): "))

bmi = (weight / (height ** 2))

print(f"Body Mass Index (kg/m^2): {round(bmi)}") #round bmi to a whole number
