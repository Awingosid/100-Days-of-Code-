#!/usr/bin/env python3

# Rock Paper Game
import random

# ASCII art representations of Rock, Paper, and Scissors
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# List of choices
choices = [rock, paper, scissors]

# User input for their choice and Randomly generate computer's choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
computer_choice = random.randint(0, 2)

# Print the computer's and user's choices (displaying the ASCII art)
print("Computer:")
print(choices[computer_choice])
print("You:")
print(choices[user_choice])

# Determine the winner or if it's a draw
if computer_choice == user_choice:
    print("Draw")
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose")

