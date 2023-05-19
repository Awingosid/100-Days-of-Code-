#!/usr/bin/env python3

#tip calculator
print("Welcome to the Tip calculator.")
bill = float(input("what was the total bill?: $"))

per = float(input("What percentage tip would you like to give? (%): "))
per /= 100

num = int(input("How many people to split the bill? "))

total_bill = bill + (bill * per)
split_bill = round(total_bill / num, 2)

print(f"Each person should pay: ${split_bill}")
