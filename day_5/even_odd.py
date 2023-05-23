#!/usr/bin/env python3

number_range = input("Input the range(separated by a comma): ").split(",")  # User input for number range
number_range = [int(number) for number in number_range]  # Convert input to a list of integers

x = number_range[0]  # Lower bound of number range
y = number_range[1]  # Upper bound of number range
z = int(input("Even or Odd numbers? (2 for even, 3 for odd): "))  # User input for selecting even or odd numbers
numbers_total = 0  # Variable to store the total sum of numbers

if z == 2:  # If even numbers are selected
    if x % 2 != 0:  # If the lower bound is odd, increment it by 1 to start with an even number
        x += 1

for number in range(x, y + 1, z):  # Iterate over the numbers in the range with the specified step (even or odd)
    numbers_total += number  # Add the number to the total sum

if z == 2:  # If even numbers were selected
    print(f"Total of even numbers from {x-1} to {y}: {numbers_total}")
else:  #if odd numbers were selected
    print(f"Total of odd numbers from {x} to {y}: {numbers_total}")

