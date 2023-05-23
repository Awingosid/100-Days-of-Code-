#!/usr/bin/env python3

number_range = input("Input the range(separated by a comma): ").split(",")
number_range = [int(number) for number in number_range]

x = number_range[0]
y = number_range[1]
z = int(input("Even or Odd numbers? (2 for even, 3 for odd): "))
numbers_total = 0
if z == 2:
    if x % 2 != 0:
        x += 1

for number in range(x, y + 1, z):
        numbers_total += number

if z == 2:
    print(f"Total of even numbers from {x-1} to {y}: {numbers_total}")
else:
    print(f"Total of odd numbers from {x} to {y}: {numbers_total}")
