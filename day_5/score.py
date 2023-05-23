#!/usr/bin/env python3

scores = input("Enter student scores(separated by spaces): ").split()  # User input for student scores
scores = [int(score) for score in scores]  # Convert input to a list of integers

highest_score = 0  # Variable to store the highest score

for score in scores:  # Iterate over the scores
    if score > highest_score:  # If the current score is greater than the highest score
        highest_score = score  # Update the highest score

print(f"\nHighest score in the class is {highest_score}")  # Print the highest score

