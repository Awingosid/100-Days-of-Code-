#!/usr/bin/env python3

# fizz buzz
number_range = input("Input number range (separated by a comma): ").split(",")
number_range = [int(number) for number in number_range]

x = number_range[0]
y = number_range[1]

for number in range(x, y+1):
    if number % 3 == 0 and number % 5 == 0:
        number = 'FizzBuzz'
    elif number % 3 == 0:
        number = 'Fizz'
    elif number % 5 == 0:
        number = 'Buzz'
    print(number)
