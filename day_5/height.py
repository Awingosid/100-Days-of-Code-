#!/usr/bin/env python3

# Prompt the user to input a list of student heights separated by spaces
student_heights = input("Input a list of student heights (separate numbers by spaces): ").split()

# Convert the input values to integers using a list comprehension
student_heights = [int(height) for height in student_heights]

# Initialize the variable to store the total height
total_height = 0

# Calculate the total height by iterating over each student height in the list
for student_height in student_heights:
    total_height += student_height

# Initialize the variable to store the number of students
number_of_students = 0

# Calculate the number of students by iterating over each element in the list
for student in student_heights:
    number_of_students += 1

# Calculate the average height by dividing the total height by the number of students
average_height = round(total_height / number_of_students)

# Print the average height of the students
print(f"Average height of students: {average_height}")

