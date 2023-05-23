#!/usr/bin/env python3

import random

print("Welcome to the password generator")
choose_number = int(input("How many number(s)?: "))  # User input for the number of numbers in the password
choose_symbol = int(input("How many symbol(s)?: "))  # User input for the number of symbols in the password
choose_letter = int(input("How many letter(s)?: "))  # User input for the number of letters in the password

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',
           '+', '=', '`', '~', '[', '{', ']', '}', '\\', '|', ';', ':',
           "'", '"', ',', '<', '.', '>', '/', '?']

password = []

# Generate random numbers, symbols and letters based on user input and add them to the password list
password.extend(random.sample(numbers, choose_number))
password.extend(random.sample(symbols, choose_symbol))
password.extend(random.sample(letters, choose_letter))

random.shuffle(password)  # Shuffle the elements in the password list randomly

# Convert each element in the password list to a string and join them together to form the final password
password_str = ''.join(str(element) for element in password)

print(f"Password: {password_str}")  # Print the generated password

