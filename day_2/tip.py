#!/usr/bin/env python3

#tip calculator
print("Welcome to the Tip calculator.")
bill = float(input("what was the total bill?: $"))

tip_percentage = float(input("What percentage tip would you like to give? (%): ")) / 100
num_people = int(input("How many people to split the bill? "))

total_bill = bill + (bill * tip_percentage)
split_bill = total_bill / num_people

split_bill = "{:.2f}".format(split_bill) #format the split bill to 2-decimal place

print(f"Each person should pay: ${split_bill}")
