#!/usr/bin/env python3

import random

# Prompt the user to enter names separated by commas
names = input("Enter names separated by a comma: ")

# Split the input string into a list of names
names_split = names.split(", ")

# Generate a random index within the range of the list
random_name = random.randint(0, len(names_split) - 1)

# Select a name at the random index
names_taken = names_split[random_name]

# Print the randomly chosen name as the one who will pay for the bill
print(f"{names_taken} will pay for the bill")

