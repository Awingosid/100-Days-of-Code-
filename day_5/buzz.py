#!/usr/bin/env python3

import random
# fizz buzz
number_range = input("Input number range (separated by a comma): ").split(",")  # User input for number range
number_range = [int(number) for number in number_range]  # Convert input to a list of integers

x = number_range[0]  # Lower bound of number range
y = number_range[1]  # Upper bound of number range

# Iterate over the numbers in the range
for number in range(x, y + 1):
    if number % 3 == 0 and number % 5 == 0:
        number = 'FizzBuzz' 
    elif number % 3 == 0:
        number = 'Fizz' 
    elif number % 5 == 0:  
        number = 'Buzz'  
    print(number)  

