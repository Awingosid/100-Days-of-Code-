#!/usr/bin/env python3

# Prompt the user to enter the size of the pizza (S/M/L)
pizza_size = input("Size (S/M/L): ").upper()

# Calculate the initial bill based on the pizza size
if pizza_size == "S":
    bill = 15
elif pizza_size == "M":
    bill = 20
else:
    bill = 25

# Prompt the user to add pepperoni (Y/N)
add_pepperoni = input("Add pepperoni? (Y/N): ").upper()

# Add the cost of pepperoni based on the pizza size
if add_pepperoni == "Y":
    if pizza_size == "S":
        bill += 2
    else:
        bill += 3

# Prompt the user to add extra cheese (Y/N)
extra_cheese = input("Extra cheese? (Y/N): ").upper()

# Add the cost of extra cheese if selected
if extra_cheese == "Y":
    bill += 1

# Print the final bill to the console
print(f"Your final bill is ${bill}")

