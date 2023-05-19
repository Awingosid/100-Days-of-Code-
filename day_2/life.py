#!/usr/bin/env python3

#this program tells how many days, weeks and months one has left if s/he live until 90 years old
age = int(input("age: "))
years_left = 90 - age

days_left =  (years_left * 365)
weeks_left = (years_left * 52)
months_left = (years_left * 12)

print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left")
