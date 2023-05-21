#!/usr/bin/env python3

import random

# Generate a random integer between 1 and 10 (inclusive) and print it
random_integer = random.randint(1, 10)
print(random_integer)

# Generate a random float between 0 and 1 and multiply it by 2, then print the result
random_float = random.random()
print(random_float * 2)

# Prompt the user to enter their guess for the coin toss (head or tail)
guess = input("Head or Tail?: ").lower()

# Generate a random integer (0 or 1) to simulate the coin toss
random_toss = random.randint(0, 1)

# Check the result of the coin toss and print "Head" or "Tail" accordingly
if random_toss == 1:
    print("Head")
else:
    print("Tail")

