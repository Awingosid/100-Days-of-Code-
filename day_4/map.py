#!/usr/bin/env python3

# Treasure Map
row1 = ['O', 'O', 'O']  
row2 = ['O', 'O', 'O']  
row3 = ['O', 'O', 'O']  

treasure_map = [row1, row2, row3]  # Treasure map consisting of three rows

print(f"{row1}\n{row2}\n{row3}")  # Print the initial state of the treasure map

position = input("Where do you want to put the treasure? (e.g., 2,3): ")  # Get user input for the treasure position

column = int(position[0])
row = int(position[2])  

treasure_map[row - 1][column - 1] = 'X'  # Place the treasure ('X') at the specified position in the treasure map

print(f"{row1}\n{row2}\n{row3}")  # Print the updated treasure map with the treasure placed

