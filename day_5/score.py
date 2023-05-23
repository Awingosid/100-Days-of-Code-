#!/usr/bin/env python3

scores = input("Enter student scores(separated by spaces): ").split()
scores = [int(score) for score in scores ]

highest_score = 0
for score in scores:
    if score > highest_score:
        highest_score = score
print(f"\nHighest score in the class is {highest_score}")
