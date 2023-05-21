#!/usr/bin/env python3

# Treasure Island Game

print('''
    _______  _______  _______  _______    _______           _______  _______ 
   (  __   )(  ____ \(  ___  )(  ____ \  (  __   )|\     /|(  ____ \(  ____ )
   | (  )  || (    \/| (   ) || (    \/  | (  )  || )   ( || (    \/| (    )|
   | | /   || (__    | (___) || |        | | /   || |   | || (__    | (____)|
   | (/ /) ||  __)   |  ___  || | ____   | (/ /) || |   | ||  __)   |     __)
   |   / | || (      | (   ) || | \_  )  |   / | || |   | || (      | (\ (   
   |  (__) || (____/\| )   ( || (___) |  |  (__) || (___) || (____/\| ) \ \__
   (_______)(_______/|/     \|(_______)  (_______)(_______)(_______/|/   \__/

''')

print("""
Welcome to Treasure Island!!
Your mission is to find the hidden treasure.
You find yourself on an island full of mysteries and dangers.
Choose your path wisely and proceed with caution.
""")

direction = input("Left or Right?: ").lower()

# Check the chosen direction
if direction == "left":
    move = input("You come across a wide river. Swim across or Wait for a boat?: ").lower()

    # Check the chosen action at the river
    if move == "wait":
        door_color = input("You reach the shore and come across three doors: Red, Yellow, and Blue. Which door do you choose?: ").lower()

        # Check the chosen door color
        if door_color == "yellow":
            print("Congratulations! You have chosen the right door and found the hidden treasure!")
        elif door_color == "red":
            print("Oh no! You open the door and are engulfed in flames. Game Over.")
        elif door_color == "blue":
            print("Oops! You open the door and are swept away by a strong gust of wind. Game Over.")
        else:
            print("You hesitate and can't decide which door to choose. Time runs out. Game Over.")
    else:
        print("Uh-oh! You jump into the river and are attacked by a school of hungry piranhas. Game Over.")
else:
    move = input("You stumble upon a dense forest. Climb a tree or Walk around?: ").lower()

    # Check the chosen action in the forest
    if move == "climb":
        print("Great choice! From the top of the tree, you spot a hidden path that leads directly to the treasure. You successfully find the hidden treasure! Congratulations!")
    elif move == "walk":
        print("You decide to walk around the forest, but unfortunately, you get lost and wander deeper into the wilderness. Game Over.")
AOA    else:
        print("You freeze, unable to make a decision. Time passes, and night falls. Game Over.")

