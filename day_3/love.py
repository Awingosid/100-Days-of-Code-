#!/usr/bin/env python3

# name and convert it to lowercase
name1 = input("Your name: ").lower()
name2 = input("Their name: ").lower()

# Concatenate the two names Count the occurrences of each letter for "true" and "love"
combined_names = name1 + name2

count_true = combined_names.count("t") + combined_names.count("r") + combined_names.count("u") + combined_names.count("e")

count_love = combined_names.count("l") + combined_names.count("o") + combined_names.count("v") + combined_names.count("e")

# concatenate the counts as strings and converting to an integer
love_score = int(str(count_true) + str(count_love))

# message based on the love score
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")

